from django.http import HttpResponse
from django.shortcuts import render, redirect
import json
import requests
from django.template.response import TemplateResponse

tracks_uris = {"uris": []}
access_token = None


def home(request):

        return render(request, 'SpotifyLector/homepage.html')


def creator(request):
        return render(request, 'SpotifyLector/creator.html')


def creatorauth(request):

        request.session['code'] = request.GET.get('code', 'err')

        values = {
            'code': str(request.session['code']),
            'grant_type': 'authorization_code',
            'redirect_uri': "http://localhost:8000/SpotifyPlCreator/creator/auth",
            'client_id': 'b7594f99e8ae44ccbbfc546c6377cb10',
            'client_secret': '426562a740d1404b870541967b060229',
                }

        # headers = {'Authorization':
        #            "Basic Yjc1OTRmOTllOGFlNDRjY2JiZmM1NDZjNjM3N2NiMTA6NDI2NTYyYTc0MGQxNDA0Yjg3MDU0MTk2N2IwNjAyMjk="}
        # headers=headers


        result = requests.post('https://accounts.spotify.com/api/token', data=values,)
        # print(result.content)
        response = json.loads(result.content)
        access_token = response["access_token"]
        refresh_token = response["refresh_token"]
        request.session['access_token'] = access_token
        request.session['refresh_token'] = refresh_token
        # print(request.session['access_token'])
        # print(request.session['refresh_token'])
        # print(response["expires_in"])
        return redirect('creator', permanent=True)


def postForm(request):

        if request.method == 'POST':

                tracks_uris['uris'].clear()
                genre1 = request.POST.get('genre1', "")
                genre2 = request.POST.get('genre2', "")
                genre3 = request.POST.get('genre3', "")
                numberSongs = request.POST.get('numberSongs', "")
                acousticness = request.POST.get('acousticness', "")
                danceability = request.POST.get('danceability', "")
                energy = request.POST.get('energy', "")
                instrumentalness = request.POST.get('instrumentalness', "")
                popularity = request.POST.get('popularity', "")
                valence = request.POST.get('valence', "")
                genrespost = None

                if genre1:
                        genrespost = '&seed_genres='+genre1
                        if genre2:
                                genrespost = '&seed_genres='+genre1+";"+genre2
                                if genre3:
                                        genrespost = '&seed_genres='+genre1+";"+genre2+";"+genre3

                authorization_header = {"Authorization": "Bearer {}".format(request.session['access_token'])}

                body = '?limit='+numberSongs \
                       + genrespost +\
                       '&acousticness='+acousticness \
                       + '&danceability='+danceability \
                       + '&energy='+energy \
                       + '&instrumentalness='+instrumentalness \
                       + '&popularity='+popularity \
                       + '&valence='+valence

                r = getPlaylist(body, authorization_header)
                # print(r)
                datajson = r.json()
                # print(datajson)
                if 'error' in datajson:
                    values = {
                        'grant_type': 'refresh_token',
                        'refresh_token': request.session['refresh_token']
                    }
                    headers = {'Authorization':
                                        "Basic Yjc1OTRmOTllOGFlNDRjY2JiZmM1NDZjNjM3N2NiMTA6NDI2NTYyYTc0MGQxNDA0Yjg3MDU0MTk2N2IwNjAyMjk="}

                    result = requests.post("https://accounts.spotify.com/api/token", data=values, headers=headers)
                    response = json.loads(result.content)
                    request.session['access_token'] = response['access_token']

                    authorization_header = {"Authorization": "Bearer {}".format(request.session['access_token'])}
                    # print(authorization_header)
                    r = getPlaylist(body, authorization_header)
                # print(body)
                datajson = r.json()
                # print(datajson)



                song_name = []
                artist_name = []
                album_name = []
                album_cover = []
                preview_url = []

                for tracks in datajson['tracks']:
                    # Tracks names
                    # print('Chanson : ' + tracks['name'])
                    song_name.append(tracks['name'])
                    # Artists names
                    # print('Artiste : ' + tracks['artists'][0]['name'])
                    artist_name.append(tracks['artists'][0]['name'])
                    # Albums names
                    # print('Album : ' + tracks['album']['name'] )
                    album_name.append(tracks['album']['name'])
                    # Albums cover
                    try:
                        if tracks['album']['images'][2]:
                            # print(tracks['album']['images'][2]['url'] + '\n')
                            album_cover.append(tracks['album']['images'][2]['url'])
                        else:
                            album_cover.append(None)
                    except IndexError:
                        album_cover.append(None)
                    preview_url.append(tracks['preview_url'])

                    tracks_uris['uris'].append(tracks['uri'])
                    # print(tracks_uris)

                total = zip(song_name, artist_name, album_name, album_cover, preview_url)

        return render(request, 'SpotifyLector/PlaylistView.html', {'total': total, 'song_name': song_name, 'artist_name': artist_name, 'album_name': album_name, 'album_cover': album_cover})


def playlistView(request):
    return TemplateResponse(request, 'SpotifyLector/PlaylistView.html', locals())


def getPlaylist(body, authorization_header):
    r = requests.get('https://api.spotify.com/v1/recommendations'
                     + body
                     , headers=authorization_header)
    return r


def createPlaylist(request):
    print(tracks_uris)
    print(request.session['access_token'])

    authorization_header = {"Authorization": "Bearer {}".format(request.session['access_token']),
                            'content-type': "application/json",}

    # Get the user ID
    r = requests.get('https://api.spotify.com/v1/me', headers=authorization_header)
    user_id = r.json()['id']

    if request.method == 'POST':

        playlist_name = request.POST.get('playlist_name', "")

    body = {'name': playlist_name,
            'public': 'false',}

    # Create the playlist
    create_playlist = requests.post(
        'https://api.spotify.com/v1/users/'+user_id+'/playlists',
        data=json.dumps(body),
        headers=authorization_header
    )

    playlist_id = create_playlist.json()['id']
    print(playlist_id)

    # Add musics to the playlist
    add_music = requests.post(
        'https://api.spotify.com/v1/users/'
        + user_id +
        '/playlists/'+
        playlist_id+'/tracks',
    headers=authorization_header,
    data=json.dumps(tracks_uris))

    print(add_music.status_code)
    if add_music.status_code == 201:
        playlist_snapshot_id = add_music.json()['snapshot_id']

    else:
        playlist_snapshot_id = 400
    print(playlist_snapshot_id)

    return render(request, 'SpotifyLector/end.html',
                  {'playlist_snapshot_id': playlist_snapshot_id,
                   'playlist_name': playlist_name,
                   'user_id': user_id,
                   'playlist_id': playlist_id})


def end(request):
    return render(request, 'SpotifyLector/end.html', locals())

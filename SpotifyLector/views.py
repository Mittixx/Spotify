from django.http import HttpResponse
from django.shortcuts import render, redirect
import json, base64

def home(request):

        return render(request, 'SpotifyLector/homepage.html')


def creator(request):
        return render(request, 'SpotifyLector/creator.html')

# Stocke le code dans une variable de session
def creatorauth(request):
        request.session['code'] = request.GET.get('code', 'err')
        print(request.session['code'])
        print(request.path)

        # body = {'grant_type': 'authorization_code',
        #        'code': request.session['code'],
        #        'redirect_ui': "http://localhost:8000"+request.path,
        #        'client_id': 'b7594f99e8ae44ccbbfc546c6377cb10',
        #        'client-secret': '426562a740d1404b870541967b060229'}
        # r = request.POST.get('https://accounts.spotify.com/api/token', data=body)
        # print(r.text)
        # jsonBody = json.loads(json.dumps(body))
        return redirect('creator', permanent=True)



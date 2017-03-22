from django import forms

class PlaylistForm(forms.Form):
    genre1 = forms.CharField()
    genre2 = forms.CharField()
    genre3 = forms.CharField()
    numberSongs = forms.IntegerField()
    acousticness = forms.IntegerField()
    danceability = forms.IntegerField()
    energy = forms.IntegerField()
    instrumentalness = forms.IntegerField()
    popularity = forms.IntegerField()
    valence = forms.IntegerField()
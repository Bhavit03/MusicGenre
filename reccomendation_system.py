import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from collections import defaultdict

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="401a7bab28ff4124beb5525faa565fb1", client_secret="0d8ffc82840544d6a9084a279215ca8f"))
def recomend_artists(genres):
    dict={}
    recommendations = sp.recommendations(seed_genres=genres, limit=5)
    for i in range(len(recommendations['tracks'])):
      link=recommendations['tracks'][i]['album']['artists'][0]['external_urls']['spotify']
      artist=recommendations['tracks'][i]['album']['artists'][0]['name']
      dict[artist]=link
    return dict
def search_music(song_name):
  res=sp.search(song_name, limit=5, offset=0, type='track',market=None)
  return res['tracks']['items'][0]['external_urls']['spotify']


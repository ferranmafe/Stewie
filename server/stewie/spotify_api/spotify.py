
import requests
import json
from pprint import pprint

def get_list_playlists_call(token):
    url = 'https://api.spotify.com/v1/me/playlists'
    headers  = { 'Authorization': 'Bearer ' + token }
    response = requests.post(url, headers=headers)

    return response.text

def get_tracks_from_playlist_call(id, token):
    url = 'https://api.spotify.com/v1/playlists/'+ id + '/tracks'
    headers  = { 'Authorization': 'Bearer ' + token, 'Accept': 'application/json', 'Content-Type': 'application/json' }
    response = requests.get(url, headers=headers )
    return response.text

def get_track_info_call(id,token):
    url = 'https://api.spotify.com/v1/audio-features?ids=' + id
    headers  = { 'Authorization': 'Bearer ' + token, 'cache-control': "no-cache", 'Content-type': 'application/json', 'Accept': 'application/json' }
    response = requests.get(url,data='', headers=headers)
    return response.text
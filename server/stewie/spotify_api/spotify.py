from server.utils import log
import requests

def get_list_playlists(token):
    url = 'https://api.spotify.com/v1/me/playlists'
    headers  = { 'Authorization': 'Bearer ' + token }
    response = requests.post(url, headers=headers)

    result = []
    for playlist in response.items:
        result.insert({
            'id': playlist.id,
            'images': playlist.images,
            'name': playlist.name
        })
    return result

def get_tracks_from_playlist(id, token):
    url = 'https://api.spotify.com/v1/playlists/'+ id + '/tracks'
    headers  = { 'Authorization': 'Bearer ' + token }
    response = requests.post(url, headers=headers)
    return response

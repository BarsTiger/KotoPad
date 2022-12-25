import requests
from urllib.parse import urlencode
from urllib.request import urlopen
from urllib.error import HTTPError
import re
from base64 import b64encode
from modules.spotify.config import SpotifyConfig
import pafy


def reencode(text: str):
    return b64encode(text.encode()).decode()


class Song(object):
    def __init__(self, artist: str, name: str):
        self.artist = artist
        self.name = name


class Spotify(object):
    def __init__(self):
        try:
            headers = {
                'Authorization': f'Basic '
                                 f'{reencode(f"{SpotifyConfig.get().client_id}:{SpotifyConfig.get().client_secret}")}',
            }

            data = {
                'grant_type': 'client_credentials'
            }

            r = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)

            self.token = r.json()['access_token']
        except Exception as e:
            print(e)

    def get_song(self, url) -> Song | None:
        if "spotify" in url:
            track_id = url.split('/')[-1].split('?')[0]
            r = requests.get(f"https://api.spotify.com/v1/tracks/{track_id}",
                             headers={'Authorization': f'Bearer {self.token}'})

            if r.status_code == 400 or r.status_code == 401:
                return None

            track = r.json()

            song_name = track['name']
            artists = []

            for artist in track['artists']:
                artists.append(artist['name'])
            artist_name = ' '.join(artists)

            return Song(artist_name, song_name)
        else:
            video = pafy.new(url)
            return Song(video.author, video.title)

    def get_youtube_url(self, url) -> str | None:
        song = self.get_song(url)

        try:
            query_string = urlencode({'search_query': song.artist + ' ' + song.name})
            htm_content = urlopen('http://www.youtube.com/results?' + query_string)
            search_results = re.findall(r'/watch\?v=(.{11})', htm_content.read().decode())

            return f'http://www.youtube.com/watch?v={search_results[0]}'

        except HTTPError:
            return None

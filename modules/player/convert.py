import pydub
import validators
from modules.config import Config
from rich import print
import pafy
import hashlib
import os
from modules.spotify.spotify_dl import Spotify
import requests


def get_raw_link(url):
    if validators.url(url):
        if 'spotify' in url:
            url = Spotify().get_youtube_url(url)
        if 'youtu' in url:
            url = pafy.new(url).getbestaudio().url

    return url


def get_ready_media(original: str) -> str | None:
    if not os.path.isdir('temp'):
        os.mkdir('temp')

    try:
        namehash = 'temp\\' + hashlib.md5(original.encode('utf-8')).hexdigest()
        if os.path.isfile(namehash):
            return namehash

        if not os.path.isfile(original):
            if validators.url(original):
                if not Config.get().direct_stream:
                    with open('tempsound', 'wb') as f:
                        f.write(requests.get(get_raw_link(original)).content)
                        original = 'tempsound'
                else:
                    original = get_raw_link(original)

        if Config.get().direct_stream:
            return original

        (pydub.AudioSegment.from_file(original) + pydub.AudioSegment.silent(1500))\
            .export(namehash, format='mp3')

        if os.path.isfile('tempsound'):
            os.remove('tempsound')

        return namehash

    except Exception as e:
        print(e)
        return None

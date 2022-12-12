import pydub
import validators
from io import BytesIO
from rich import print
import pafy
import hashlib
import os
from modules.spotify.spotify_dl import Spotify
from gui.modules.core.popup import popup
import requests


def get_raw_link(url):
    if validators.url(url):
        if 'spotify' in url:
            url = Spotify().get_youtube_url(url)
        if 'youtu' in url:
            url = pafy.new(url).audiostreams[0].url
    else:
        url = None

    return url


def get_silenced_media(original: str) -> str | None:
    if not os.path.isdir('temp'):
        os.mkdir('temp')

    try:
        namehash = 'temp\\' + hashlib.md5(original.encode('utf-8')).hexdigest()
        if not os.path.isfile(original):
            if validators.url(original):
                original = BytesIO(requests.get(get_raw_link(original)).content)

        (pydub.AudioSegment.from_file(original) + pydub.AudioSegment.silent(1500))\
            .export(namehash, format='mp3')
        return namehash

    except Exception as e:
        raise e
        print(e)
        return None

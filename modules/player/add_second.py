import pydub
import validators
from urllib.request import urlopen
from io import BytesIO
from rich import print
import pafy
import hashlib
import os


def get_silenced_media(original: str) -> str | None:
    if not os.path.isdir('temp'):
        os.mkdir('temp')

    try:
        name = original
        namehash = 'temp\\' + hashlib.md5(name.encode('utf-8')).hexdigest()
        if not os.path.isfile(namehash):
            if validators.url(original):
                if 'youtu' in original:
                    original = pafy.new(original).getbestaudio().url
                original = BytesIO(urlopen(original).read())

            (pydub.AudioSegment.from_file(original) + pydub.AudioSegment.silent(1500))\
                .export(namehash, format='mp3')
        return namehash

    except Exception as e:
        print(e)
        raise e
        return None

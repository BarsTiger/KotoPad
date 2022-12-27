import time

import validators
from ezzthread import threaded
from gui.modules.core.qt_updater import call
from gui.gui import Ui_MainWindow
from modules.player import convert
from modules.spotify.spotify_dl import Spotify
from urllib.request import urlopen
from functools import partial
import os


@threaded
def download_track(ui: Ui_MainWindow):
    try:
        url = ui.download_url_box.text()

        if not validators.url(url):
            call(ui.download_track_logs.append, f"{url} is not valid URL, skipping")
            return

        call(ui.download_track_logs.append, f"Downloading {url}")

        name = (lambda song: song.artist + " - " + song.name + ".mp3")(Spotify().get_song(url)) \
            if "spotify" in url or "youtu" in url else url.split('/')[-1]

        url = convert.get_raw_link(url)

        call(ui.download_track_button.setEnabled, False)

        response = urlopen(url)
        call(ui.download_track_progress.setValue, 0)
        size = int(response.info()["Content-length"])
        downloaded = 0
        with open(os.path.join(ui.download_to_path_box.text(), name), "wb") as dest_file:
            for data in iter(partial(response.read, 4096), b""):
                downloaded += len(data)
                dest_file.write(data)
                call(ui.download_track_progress.setValue, int(downloaded / size * 100))

        call(ui.download_track_button.setEnabled, True)
        call(ui.download_track_logs.append, f"Downloaded to {os.path.join(ui.download_to_path_box.text(), name)}")
    except Exception as e:
        print(e)
        call(ui.download_track_button.setEnabled, True)
        call(ui.download_track_logs.append, f"Failed")

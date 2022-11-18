import vlc
from gui.gui import Ui_MainWindow


def get_instance() -> vlc.Instance:
    return vlc.Instance()


def get_player(instance: vlc.Instance) -> vlc.MediaPlayer:
    return instance.media_player_new()


def get_devices(mediaplayer: vlc.MediaPlayer) -> dict:
    devices = dict()

    device = mediaplayer.audio_output_device_enum()
    while device:
        devices[device.contents.description.decode("utf-8")] = device.contents.device
        device = device.contents.next

    return devices


class Player(object):
    def __init__(self):
        self.instance = get_instance()
        self.mediaplayer_preview = get_player(self.instance)
        self.mediaplayer_preview.audio_output_device_set(None, get_devices(self.mediaplayer_preview)['Default'])
        self.mediaplayer_out = get_player(self.instance)
        self.mediaplayer_out.audio_output_device_set(None, get_devices(
            self.mediaplayer_out)['CABLE Input (VB-Audio Virtual Cable)'])
        self.is_paused = False

    def set_media(self, media: str) -> None:
        self.mediaplayer_preview.set_media(self.instance.media_new(media))
        self.mediaplayer_out.set_media(self.instance.media_new(media))

    def play(self, ui: Ui_MainWindow):
        self.mediaplayer_preview.play()
        self.mediaplayer_out.play()

    def get_length(self) -> int:
        return int(self.mediaplayer_preview.get_length() / 1000)

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

    def set_media(self, media: str) -> None:
        self.mediaplayer_preview.set_media(self.instance.media_new(media))
        self.mediaplayer_out.set_media(self.instance.media_new(media))

    def set_volume(self, volume: int):
        self.mediaplayer_preview.audio_set_volume(volume)
        self.mediaplayer_out.audio_set_volume(volume)

    def play(self, ui: Ui_MainWindow):
        self.mediaplayer_preview.play()
        self.mediaplayer_out.play()
        self.set_volume(ui.volume_box.value())

    def playpause(self, ui: Ui_MainWindow):
        from PyQt5 import QtGui
        play_icon = QtGui.QIcon()
        play_icon.addPixmap(QtGui.QPixmap(":/img/img/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pause_icon = QtGui.QIcon()
        pause_icon.addPixmap(QtGui.QPixmap(":/img/img/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        if self.mediaplayer_out.is_playing():
            self.mediaplayer_preview.pause()
            self.mediaplayer_out.pause()
            ui.play_pause_button.setIcon(play_icon)
        else:
            self.mediaplayer_preview.play()
            self.mediaplayer_out.play()
            ui.play_pause_button.setIcon(pause_icon)

    def get_length(self) -> int:
        return int(self.mediaplayer_preview.get_length() / 1000)

    def get_position(self) -> int:
        return int(self.mediaplayer_preview.get_position() * 100)

    def set_position(self, pos: float):
        self.mediaplayer_preview.set_position(pos)
        self.mediaplayer_out.set_position(pos)

    def update_devices(self):
        pass

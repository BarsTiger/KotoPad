import vlc
from gui.gui import Ui_MainWindow
from gui.modules.core import popup
from modules.player.convert import get_silenced_media


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
    def __init__(self, ui: Ui_MainWindow):
        self.instance_preview = get_instance()
        self.instance_out = get_instance()
        self.mediaplayer_preview = get_player(self.instance_preview)
        self.mediaplayer_preview.audio_output_device_set(None, get_devices(self.mediaplayer_preview)[
            ui.preview_device_play_box.currentText()
        ])
        self.mediaplayer_out = get_player(self.instance_out)
        self.mediaplayer_out.audio_output_device_set(None, get_devices(
            self.mediaplayer_out)[ui.output_device_play_box.currentText()])

    def set_media(self, media: str) -> None:
        if get_silenced_media(media):
            self.mediaplayer_preview.set_media(self.instance_preview.media_new(get_silenced_media(media)))
            self.mediaplayer_out.set_media(self.instance_out.media_new(get_silenced_media(media)))
        else:
            popup.popup('Error', 'Error playing this media. \nIf it uses link, check is this link valid.')
            self.mediaplayer_preview.set_media(None)
            self.mediaplayer_out.set_media(None)

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

    def update_devices(self, ui: Ui_MainWindow):
        self.mediaplayer_preview.audio_output_device_set(None, get_devices(self.mediaplayer_preview)[
            ui.preview_device_play_box.currentText()
        ])
        self.mediaplayer_out.audio_output_device_set(None, get_devices(self.mediaplayer_out)[
            ui.output_device_play_box.currentText()
        ])

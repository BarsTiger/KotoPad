from gui.gui import Ui_MainWindow
from PyQt5 import QtGui
from modules.player.player import Player
from modules.config import Config


def register_handlers(ui: Ui_MainWindow, p: Player):
    play_icon = QtGui.QIcon()
    play_icon.addPixmap(QtGui.QPixmap(":/img/img/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    pause_icon = QtGui.QIcon()
    pause_icon.addPixmap(QtGui.QPixmap(":/img/img/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    ui.volume_box.valueChanged.connect(lambda: (p.set_volume(ui.volume_box.value()),
                                                Config.update('volume', ui.volume_box.value())))
    ui.play_pause_button.clicked.connect(lambda: p.playpause(ui))
    ui.timer.timeout.connect(lambda: (ui.player_time_slider.setValue(p.get_position()),
                                      ui.play_pause_button.setIcon(play_icon) if not p.mediaplayer_out.is_playing()
                             else ui.play_pause_button.setIcon(pause_icon)))
    ui.player_time_slider.sliderPressed.connect(lambda: p.set_position(ui.player_time_slider.value() / 100.0))
    ui.output_device_play_box.currentTextChanged.connect(lambda: p.update_devices(ui))
    ui.preview_device_play_box.currentTextChanged.connect(lambda: p.update_devices(ui))

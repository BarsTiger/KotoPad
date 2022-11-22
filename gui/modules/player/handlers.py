from gui.gui import Ui_MainWindow
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from modules.player.player import Player


def register_handlers(ui: Ui_MainWindow, MainWindow: QMainWindow, p: Player):
    """
    Register this module handlers
    :param p:
    :param ui:
    :param MainWindow:
    :return:
    """

    play_icon = QtGui.QIcon()
    play_icon.addPixmap(QtGui.QPixmap(":/img/img/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    ui.volume_box.valueChanged.connect(lambda: p.set_volume(ui.volume_box.value()))
    ui.play_pause_button.clicked.connect(lambda: p.playpause(ui))
    ui.timer.timeout.connect(lambda: (ui.player_time_slider.setValue(p.get_position()),
                                      ui.play_pause_button.setIcon(play_icon) if not p.mediaplayer_out.is_playing()
                             else None))
    ui.player_time_slider.sliderPressed.connect(lambda: p.set_position(ui.player_time_slider.value() / 100.0))

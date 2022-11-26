from gui.gui import Ui_MainWindow
from gui.modules.core.blur import GlobalBlur
from gui.modules.initialize import styles
from gui.modules.handlers import register
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from modules.config import Config
from modules.player.player import Player


def on_load(ui: Ui_MainWindow, MainWindow: QMainWindow):
    """
    Setup all UI elements
    :param ui:
    :param MainWindow:
    :return:
    """
    ui.content.setCurrentIndex(0)

    MainWindow.setStyleSheet(styles.centralwidget())
    ui.menu.setStyleSheet(styles.menupage())
    if 'acrylic' in Config.get().theme:
        GlobalBlur(MainWindow.winId(), acrylic=True)

    ui.timer = QtCore.QTimer(MainWindow)
    ui.timer.start(100)

    p = Player()

    register.register_handlers(ui, MainWindow, p)

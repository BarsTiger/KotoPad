from gui.gui import Ui_MainWindow
from gui.modules.core.blur import GlobalBlur
from gui.modules.initialize import styles
from gui.modules.initialize import fill_settings
from gui.modules.handlers import register
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from modules.config import Config
from modules.player.player import Player
from modules.restream.restream import Restreamer
from gui.modules.explorer import initialize


def on_load(ui: Ui_MainWindow, MainWindow: QMainWindow):
    ui.content.setCurrentIndex(0)

    MainWindow.setStyleSheet(styles.centralwidget())
    ui.menu.setStyleSheet(styles.menupage())
    if 'acrylic' in Config.get().theme:
        GlobalBlur(MainWindow.winId(), acrylic=True)

    ui.timer = QtCore.QTimer(MainWindow)
    ui.timer.start(100)

    fill_settings.fill_settings(ui)

    p = Player(ui)
    rs = Restreamer()

    initialize.init_explorer(ui)

    (lambda: rs.restart(ui) if ui.restream_micro_checkbox.isChecked() else rs.stop())()

    register.register_handlers(ui, MainWindow, p, rs)

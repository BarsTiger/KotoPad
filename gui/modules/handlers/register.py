from gui.gui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from gui.modules import menu
from gui.modules import pads
from gui.modules import player
from gui.modules import settings
from gui.modules import restreammic
from gui.modules import explorer
from gui.modules import collections
from gui.modules import stream
from gui.modules import download
from gui.modules import collab
from modules.player.player import Player
from modules.restream.restream import Restreamer


def register_handlers(ui: Ui_MainWindow, MainWindow: QMainWindow, p: Player, rs: Restreamer):
    menu.register_handlers(ui)
    pads.register_handlers(ui, MainWindow, p)
    player.register_handlers(ui, p)
    settings.register_handlers(ui)
    restreammic.register_handlers(ui, MainWindow, rs)
    explorer.register_handlers(ui, p)
    collections.register_handlers(ui, p)
    stream.register_handlers(ui, p)
    download.register_handlers(ui)
    collab.register_handlers(ui, p)

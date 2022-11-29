from gui.gui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from gui.modules import menu
from gui.modules import pads
from gui.modules import player
from gui.modules import settings
from modules.player.player import Player


def register_handlers(ui: Ui_MainWindow, MainWindow: QMainWindow, p: Player):
    """
    Register all handlers
    :param ui:
    :param MainWindow:
    :param p:
    :return:
    """
    menu.register_handlers(ui)
    pads.register_handlers(ui, MainWindow, p)
    player.register_handlers(ui, MainWindow, p)
    settings.register_handlers(ui)

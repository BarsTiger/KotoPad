from gui.gui import Ui_MainWindow
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

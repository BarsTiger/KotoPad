from gui.gui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from gui.modules import menu
from gui.modules import pads


def register_handlers(ui: Ui_MainWindow, MainWindow: QMainWindow):
    """
    Register all handlers
    :param ui:
    :param MainWindow:
    :return:
    """
    menu.register_handlers(ui)
    pads.register_handlers(ui, MainWindow)

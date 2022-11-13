from gui.gui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from .initialize_pads_settings import *
from .fill_pads_from_settings import *


def register_handlers(ui: Ui_MainWindow, MainWindow: QMainWindow):
    """
    Register this module handlers
    :param ui:
    :param MainWindow:
    :return:
    """
    fill_settings(ui)
    fill_pads(ui, MainWindow)
    ui.edit_first_pads_collection_list.itemChanged.connect(lambda: fill_pads(ui, MainWindow))
    ui.edit_second_pads_collection_list.itemChanged.connect(lambda: fill_pads(ui, MainWindow))

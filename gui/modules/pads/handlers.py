from gui.gui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from .initialize_pads_settings import *
from .fill_pads_from_settings import *
from modules.player.player import Player


def register_handlers(ui: Ui_MainWindow, MainWindow: QMainWindow, p: Player):
    fill_settings(ui)
    fill_pads(ui, MainWindow, p)
    ui.edit_first_pads_collection_list.itemChanged.connect(lambda: fill_pads(ui, MainWindow, p))
    ui.edit_second_pads_collection_list.itemChanged.connect(lambda: fill_pads(ui, MainWindow, p))

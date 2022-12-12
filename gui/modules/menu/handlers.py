from gui.gui import Ui_MainWindow
from .menu import handle_menu_click


def register_handlers(ui: Ui_MainWindow):
    ui.menu.itemClicked.connect(lambda: handle_menu_click(ui.menu.currentItem().text(), ui))

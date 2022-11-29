from gui.gui import Ui_MainWindow
from modules.config import Config


def register_handlers(ui: Ui_MainWindow):
    """
    Register this module handlers
    :param ui:
    :return:
    """

    ui.theme_box.setCurrentText(Config.get().theme)

    ui.theme_box.currentTextChanged.connect(lambda: Config.update("theme", ui.theme_box.currentText()))

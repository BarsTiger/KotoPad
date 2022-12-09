from gui.gui import Ui_MainWindow
from modules.config import Config


def register_handlers(ui: Ui_MainWindow):
    """
    Register this module handlers
    :param ui:
    :return:
    """

    ui.theme_box.currentTextChanged.connect(lambda: Config.update("theme", ui.theme_box.currentText()))
    ui.restream_micro_checkbox.clicked.connect(lambda: Config.update("restream",
                                                                     ui.restream_micro_checkbox.isChecked()))

    ui.output_device_restream_box.currentTextChanged.connect(
        lambda: Config.update("out_micro", ui.output_device_restream_box.currentText())
    )
    ui.input_device_restream_box.currentTextChanged.connect(
        lambda: Config.update("in_micro", ui.input_device_restream_box.currentText())
    )

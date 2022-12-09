from gui.gui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from modules.restream.restream import Restreamer


def register_handlers(ui: Ui_MainWindow, MainWindow: QMainWindow, rs: Restreamer):
    ui.restream_micro_checkbox.clicked.connect(
        lambda: rs.restart(ui) if ui.restream_micro_checkbox.isChecked() else rs.stop()
    )

    ui.output_device_restream_box.currentTextChanged.connect(lambda: rs.restart(ui))
    ui.input_device_restream_box.currentTextChanged.connect(lambda: rs.restart(ui))

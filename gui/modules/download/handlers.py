from gui.gui import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
from gui.modules.download import downloader


def register_handlers(ui: Ui_MainWindow):
    ui.choose_download_path_button.clicked.connect(
        lambda: ui.download_to_path_box.setText(
            QFileDialog.getExistingDirectory(caption="Select where to download file")
        )
    )

    ui.download_track_button.clicked.connect(lambda: downloader.download_track(ui))

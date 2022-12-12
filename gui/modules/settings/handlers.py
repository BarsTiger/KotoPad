from gui.gui import Ui_MainWindow
from modules.config import Config
from modules.spotify.config import SpotifyConfig
import shutil


def register_handlers(ui: Ui_MainWindow):
    ui.theme_box.currentTextChanged.connect(lambda: Config.update("theme", ui.theme_box.currentText()))
    ui.restream_micro_checkbox.clicked.connect(lambda: Config.update("restream",
                                                                     ui.restream_micro_checkbox.isChecked()))

    ui.output_device_restream_box.currentTextChanged.connect(
        lambda: Config.update("out_micro", ui.output_device_restream_box.currentText())
    )
    ui.input_device_restream_box.currentTextChanged.connect(
        lambda: Config.update("in_micro", ui.input_device_restream_box.currentText())
    )

    ui.output_device_play_box.currentTextChanged.connect(
        lambda: Config.update("out_device", ui.output_device_play_box.currentText())
    )
    ui.preview_device_play_box.currentTextChanged.connect(
        lambda: Config.update("preview_device", ui.preview_device_play_box.currentText())
    )

    ui.spotify_client_id_box.textChanged.connect(
        lambda: SpotifyConfig.update("client_id", ui.spotify_client_id_box.text())
    )
    ui.spotify_client_secret_box.textChanged.connect(
        lambda: SpotifyConfig.update("client_secret", ui.spotify_client_secret_box.text())
    )

    ui.clear_temp_button.clicked.connect(
        lambda: shutil.rmtree('temp', ignore_errors=True)
    )

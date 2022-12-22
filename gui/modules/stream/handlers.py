from gui.gui import Ui_MainWindow
from modules.player.player import Player


def register_handlers(ui: Ui_MainWindow, p: Player):
    ui.play_stream_button.clicked.connect(
        lambda: (
            p.set_media(ui.to_stream_url_box.text()),
            ui.stream_logs_box.append(f"Playing {ui.to_stream_url_box.text()}"),
            p.play(ui)
        )
    )

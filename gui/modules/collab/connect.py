from gui.gui import Ui_MainWindow
import json
import pysher
from gui.modules.core.popup import popup
import base64
from modules.player.player import Player


def on_url_music(url: str, p: Player, ui: Ui_MainWindow):
    ui.collab_connect_logs.append(f"Received {url}")
    p.set_media(url)
    p.play(ui)


def handle_connection_to_server(ui: Ui_MainWindow, p: Player):
    ui.collab_connect_logs.append(f'Connected to {ui.receiver_creds["name"]}')
    channel = ui.receiver.subscribe(ui.collab_session_key_box.text())
    channel.bind('sound', lambda _: on_url_music(_, p, ui))
    channel.bind('stop', lambda _: (p.mediaplayer_preview.stop(),
                                    p.mediaplayer_out.stop()))


def on_connect_clicked(ui: Ui_MainWindow, p: Player):
    try:
        creds = dict(json.loads(
            base64.decodebytes(bytes(ui.collab_session_key_box.text().replace('-', '\n'), encoding='utf-8')
                               ).decode('utf-8').replace("'", '"')
        ))
        ui.collab_connect_logs.append(f'Loaded {creds["name"]}')
    except Exception as e:
        print(e)
        popup("Error", 'Invalid connection key')
        return

    ui.receiver_creds = creds

    ui.receiver = pysher.Pusher(
        key=creds["key"],
        cluster=creds["cluster"]
    )
    ui.receiver.connection.bind('pusher:connection_established', lambda _: handle_connection_to_server(ui, p))
    ui.receiver.connect()
    ui.collab_disconnect_button.setEnabled(True)

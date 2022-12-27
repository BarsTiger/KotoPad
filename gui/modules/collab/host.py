from gui.gui import Ui_MainWindow
import pusher
import base64
import json
from gui.modules.core.popup import popup


def connect_to_host_admin(ui: Ui_MainWindow):
    try:
        creds = dict(json.loads(
            base64.decodebytes(bytes(ui.collab_session_admin_key_box.text().replace('-', '\n'), encoding='utf-8')
                               ).decode('utf-8').replace("'", '"')
        ))
        creds_from_connection = dict(json.loads(
            base64.decodebytes(bytes(creds['connection_key'].replace('-', '\n'), encoding='utf-8')
                               ).decode('utf-8').replace("'", '"')
        ))
        creds |= creds_from_connection
        ui.control_admin_logs.append(f'Loaded {creds["name"]}')
    except Exception as e:
        print(e)
        popup("Error", 'Invalid admin key')
        return

    ui.sender_creds = creds

    ui.sender = pusher.Pusher(
        app_id=creds["app_id"],
        key=creds["key"],
        secret=creds["secret"],
        cluster=creds["cluster"]
    )
    ui.send_to_users_admin_button.setEnabled(True)
    ui.stop_all_button_admin.setEnabled(True)


def on_send_sound_button(ui: Ui_MainWindow):
    ui.sender.trigger(ui.sender_creds["connection_key"], 'sound',
                      ui.url_to_send_admin_box.text())
    ui.control_admin_logs.append(f'Sent {ui.url_to_send_admin_box.text()}')


def on_stop_sound_button(ui: Ui_MainWindow):
    ui.sender.trigger(ui.sender_creds["connection_key"], 'stop', None)
    ui.control_admin_logs.append(f'Stopped sounds')

from gui.gui import Ui_MainWindow
from modules.config.pusher import PusherConfig
from gui.modules.core.popup import popup
import base64
from gui.modules.collab.host import connect_to_host_admin


def on_create_session_clicked(ui: Ui_MainWindow):
    if ui.create_session_name_box.text() == "":
        popup("Error", "Specify room name")
        return

    connection_key = base64.encodebytes(
        bytes(str(
            {
                "name": ui.create_session_name_box.text(),
                "key": PusherConfig.get().key,
                "cluster": PusherConfig.get().cluster
            }
        ), encoding='utf-8')).decode('utf-8').strip().replace('\n', '-')

    ui.new_connection_key_copy_box.setText(connection_key)

    admin_key = base64.encodebytes(
        bytes(str(
            {
                "connection_key": connection_key,
                "app_id": PusherConfig.get().app_id,
                "secret": PusherConfig.get().secret
            }
        ), encoding='utf-8')).decode('utf-8').strip().replace('\n', '-')
    ui.new_connection_admin_key_copy_box.setText(admin_key)
    ui.collab_session_admin_key_box.setText(admin_key)
    connect_to_host_admin(ui)

from gui.gui import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
from modules.player.player import Player
from modules.anonfiles.anonfiles import Anonfiles
from ezzthread import threaded
from gui.modules.core.qt_updater import call
from gui.modules.collab import create, host, connect


def register_handlers(ui: Ui_MainWindow, p: Player):
    ui.send_to_users_admin_button.setEnabled(False)
    ui.collab_disconnect_button.setEnabled(False)
    ui.stop_all_button_admin.setEnabled(False)

    ui.create_session_button.clicked.connect(
        lambda: create.on_create_session_clicked(ui)
    )


    ui.connect_to_admin_session_button.clicked.connect(
        lambda: host.connect_to_host_admin(ui)
    )
    ui.send_to_users_admin_button.clicked.connect(
        lambda: host.on_send_sound_button(ui)
    )
    ui.stop_all_button_admin.clicked.connect(
        lambda: host.on_stop_sound_button(ui)
    )


    ui.connect_to_session_button.clicked.connect(
        lambda: connect.on_connect_clicked(ui, p)
    )
    ui.collab_disconnect_button.clicked.connect(
        lambda: (ui.receiver.disconnect(),
                 ui.collab_disconnect_button.setEnabled(False),
                 ui.collab_connect_logs.append('Disconnected'))
    )


    ui.choose_upload_sound_button.clicked.connect(
        lambda: ui.filename_to_upload_box.setText(
            QFileDialog.getOpenFileName(caption='Choose file to upload')[0]
        )
    )
    ui.upload_sound_button.clicked.connect(
        lambda: threaded(
            call(ui.anonfiles_uploaded_url_box.setText, Anonfiles.upload(ui.filename_to_upload_box.text()).url)
        )
    )

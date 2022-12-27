from gui.gui import Ui_MainWindow
from modules.config import Config
from modules.config.pusher import PusherConfig
from modules.spotify.config import SpotifyConfig
from modules.restream import get_streaming_devices
from modules.player.player import get_devices, get_instance, get_player


def fill_settings(ui: Ui_MainWindow):
    ui.volume_box.setValue(Config.get().volume)

    ui.theme_box.setCurrentText(Config.get().theme)

    play_devices = get_devices(get_player(get_instance()))

    ui.output_device_play_box.addItems(play_devices)
    ui.preview_device_play_box.addItems(play_devices)

    if Config.get().out_device in play_devices.keys():
        ui.output_device_play_box.setCurrentText(Config.get().out_device)
    else:
        for item in play_devices.keys():
            if '(VB-Audio Virtual Cable)' in item:
                ui.output_device_play_box.setCurrentText(item)
                break

    if Config.get().preview_device in play_devices.keys():
        ui.preview_device_play_box.setCurrentText(Config.get().preview_device)
    elif 'Default' in play_devices.keys():
        ui.preview_device_play_box.setCurrentText('Default')

    ui.restream_micro_checkbox.setChecked(Config.get().restream)
    ui.input_device_restream_box.addItems(get_streaming_devices().in_l)
    ui.output_device_restream_box.addItems(get_streaming_devices().out_l)

    if Config.get().in_micro in get_streaming_devices().in_l:
        ui.input_device_restream_box.setCurrentText(Config.get().in_micro)

    if Config.get().out_micro in get_streaming_devices().out_l:
        ui.output_device_restream_box.setCurrentText(Config.get().out_micro)

    ui.spotify_client_id_box.setText(SpotifyConfig.get().client_id)
    ui.spotify_client_secret_box.setText(SpotifyConfig.get().client_secret)

    ui.pusher_app_id_box.setText(PusherConfig.get().app_id)
    ui.pusher_key_box.setText(PusherConfig.get().key)
    ui.pusher_secret_box.setText(PusherConfig.get().secret)
    ui.pusher_cluster_box.setText(PusherConfig.get().cluster)

    ui.use_original_streaming_method_check.setChecked(Config.get().direct_stream)

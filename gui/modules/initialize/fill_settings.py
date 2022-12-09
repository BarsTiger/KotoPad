from gui.gui import Ui_MainWindow
from modules.config import Config
from modules.restream import get_streaming_devices


def fill_settings(ui: Ui_MainWindow):
    ui.volume_box.setValue(Config.get().volume)

    ui.theme_box.setCurrentText(Config.get().theme)

    # ui.output_device_play_box.addItems()

    ui.restream_micro_checkbox.setChecked(Config.get().restream)
    ui.input_device_restream_box.addItems(get_streaming_devices().in_l)
    ui.output_device_restream_box.addItems(get_streaming_devices().out_l)

    if Config.get().in_micro in get_streaming_devices().in_l:
        ui.input_device_restream_box.setCurrentText(Config.get().in_micro)

    if Config.get().out_micro in get_streaming_devices().out_l:
        ui.output_device_restream_box.setCurrentText(Config.get().out_micro)

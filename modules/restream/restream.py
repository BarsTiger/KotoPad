from gui.gui import Ui_MainWindow
import sounddevice as sd
from . import get_streaming_devices


class Restreamer(object):
    def __init__(self):
        self.stream = sd.Stream()

    @staticmethod
    def callback(indata, outdata, frames, time, status):
        if status:
            print(status)
        outdata[:] = indata

    def restart(self, ui: Ui_MainWindow):
        self.stream.stop()
        self.stream = sd.Stream(device=(get_streaming_devices().input[ui.input_device_restream_box.currentText()],
                                        get_streaming_devices().output[ui.output_device_restream_box.currentText()]),
                                callback=Restreamer.callback)
        self.stream.start()

    def stop(self):
        self.stream.stop()

from dataclasses import dataclass
import sounddevice as sd


@dataclass
class StreamingDevices:
    output: dict
    out_l: list
    input: dict
    in_l: list


def get_streaming_devices() -> StreamingDevices:
    devices = StreamingDevices(dict(), list(), dict(), list())

    for device in sd.query_hostapis()[0]['devices']:
        if sd.query_devices(device)['max_output_channels'] == 0:
            devices.input[sd.query_devices(device)['name']] = sd.query_devices(device)['index']
            devices.in_l.append(sd.query_devices(device)['name'])
        else:
            devices.output[sd.query_devices(device)['name']] = sd.query_devices(device)['index']
            devices.out_l.append(sd.query_devices(device)['name'])

    return devices

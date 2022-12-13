from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(frozen=True)
class ConfigModel:
    theme: str
    volume: int
    out_device: str
    preview_device: str
    in_micro: str
    out_micro: str
    restream: bool
    direct_stream: bool

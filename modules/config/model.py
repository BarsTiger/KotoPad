from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List


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


@dataclass_json
@dataclass(frozen=True)
class PathsModel:
    first_browser_path: str
    second_browser_path: str
    collections_list: List[str]


@dataclass_json
@dataclass(frozen=True)
class PusherModel:
    app_id: str
    key: str
    secret: str
    cluster: str

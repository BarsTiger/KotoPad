from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Dict


@dataclass_json
@dataclass(frozen=True)
class PadsModel:
    first_pads: Dict[str, str]
    second_pads: Dict[str, str]

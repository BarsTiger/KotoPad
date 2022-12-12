import json
import os
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(frozen=True)
class SpotConfig:
    client_id: str
    client_secret: str


class SpotifyConfig:
    @staticmethod
    def default():
        return {
            "client_id": "5f573c9620494bae87890c0f08a60293",
            "client_secret": "212476d9b0f3472eaa762d90b19b0ba8"
        }

    @staticmethod
    def fix() -> None:
        try:
            with open("data/config.spotify", "w") as file:
                json.dump(SpotifyConfig.default(), file)
        except FileNotFoundError:
            if not os.path.exists('data'):
                os.mkdir('data')
            SpotifyConfig.fix()

    @staticmethod
    def get() -> SpotConfig:
        try:
            with open("data/config.spotify", "r") as file:
                return SpotConfig.from_dict(json.load(file))
        except:
            SpotifyConfig.fix()
            return SpotifyConfig.get()

    @staticmethod
    def update(key: str, value: str | None) -> dict:
        with open("data/config.spotify", "r") as file:
            settings = json.load(file)

        settings[key] = value

        with open("data/config.spotify", "w") as file:
            json.dump(settings, file)

        return settings

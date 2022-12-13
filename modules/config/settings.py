from modules.config.model import ConfigModel
import json
import os


class Config:
    @staticmethod
    def default():
        return {
            "theme": "Dark gray",
            "volume": 100,
            "out_device": str(),
            "preview_device": str(),
            "in_micro": str(),
            "out_micro": str(),
            "restream": False,
            "direct_stream": True
        }

    @staticmethod
    def fix() -> None:
        try:
            with open("data/config.cfg", "w") as file:
                json.dump(Config.default(), file)
        except FileNotFoundError:
            if not os.path.exists('data'):
                os.mkdir('data')
            Config.fix()

    @staticmethod
    def get() -> ConfigModel:
        try:
            with open("data/config.cfg", "r") as file:
                return ConfigModel.from_dict(json.load(file))
        except:
            Config.fix()
            return Config.get()

    @staticmethod
    def update(key: str, value: str | None) -> dict:
        with open("data/config.cfg", "r") as file:
            settings = json.load(file)

        settings[key] = value

        with open("data/config.cfg", "w") as file:
            json.dump(settings, file)

        return settings

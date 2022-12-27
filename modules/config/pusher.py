from modules.config.model import PusherModel
import json
import os


class PusherConfig:
    @staticmethod
    def default():
        return {
            "app_id": str(),
            "key": str(),
            "secret": str(),
            "cluster": str()
        }

    @staticmethod
    def fix() -> None:
        try:
            with open("data/config.pusher", "w") as file:
                json.dump(PusherConfig.default(), file)
        except FileNotFoundError:
            if not os.path.exists('data'):
                os.mkdir('data')
            PusherConfig.fix()

    @staticmethod
    def get() -> PusherModel:
        try:
            with open("data/config.pusher", "r") as file:
                return PusherModel.from_dict(json.load(file))
        except:
            PusherConfig.fix()
            return PusherConfig.get()

    @staticmethod
    def update(key: str, value: str | list | None) -> dict:
        with open("data/config.pusher", "r") as file:
            settings = json.load(file)

        settings[key] = value

        with open("data/config.pusher", "w") as file:
            json.dump(settings, file)

        return settings

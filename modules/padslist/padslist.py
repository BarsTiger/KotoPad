from modules.padslist.model import PadsModel
import json
import os


class Pads:
    @staticmethod
    def default():
        return {
            "first_pads": dict(),
            "second_pads": dict()
        }

    @staticmethod
    def fix() -> None:
        try:
            with open("data/config.pads", "w") as file:
                json.dump(Pads.default(), file)
        except FileNotFoundError:
            if not os.path.exists('data'):
                os.mkdir('data')
            Pads.fix()

    @staticmethod
    def get() -> PadsModel:
        try:
            with open("data/config.pads", "r") as file:
                return PadsModel.from_dict(json.load(file))
        except:
            Pads.fix()
            return Pads.get()

    @staticmethod
    def update(key: str, value: str | None) -> dict:
        with open("data/config.pads", "r") as file:
            settings = json.load(file)

        settings[key] = value

        with open("data/config.pads", "w") as file:
            json.dump(settings, file)

        return settings

from modules.config.model import PathsModel
import json
import os


class PathsConfig:
    @staticmethod
    def default():
        return {
            "first_browser_path": "",
            "second_browser_path": "",
            "collections_list": list()
        }

    @staticmethod
    def fix() -> None:
        try:
            with open("data/config.path", "w") as file:
                json.dump(PathsConfig.default(), file)
        except FileNotFoundError:
            if not os.path.exists('data'):
                os.mkdir('data')
            PathsConfig.fix()

    @staticmethod
    def get() -> PathsModel:
        try:
            with open("data/config.path", "r") as file:
                return PathsModel.from_dict(json.load(file))
        except:
            PathsConfig.fix()
            return PathsConfig.get()

    @staticmethod
    def update(key: str, value: str | list | None) -> dict:
        with open("data/config.path", "r") as file:
            settings = json.load(file)

        settings[key] = value

        with open("data/config.path", "w") as file:
            json.dump(settings, file)

        return settings

import requests
from dataclasses import dataclass
from Direct_Download import Direct


@dataclass
class File:
    url: str | None
    id: str | None
    name: str | None


class Anonfiles:
    @staticmethod
    def upload(path: str) -> File | None:
        try:
            r = requests.post("https://api.anonfiles.com/upload", files={'file': open(path, 'rb')}).json()
            if not r["status"]:
                return

            return File(url=r["data"]["file"]["url"]["full"],
                        id=r["data"]["file"]["metadata"]["id"],
                        name=r["data"]["file"]["metadata"]["name"])

        except Exception as e:
            print(e)
            return File(None, None, None)

    @staticmethod
    def get_direct(url: str) -> str | None:
        try:
            return Direct().anonfiles(url)['directDownload']

        except Exception as e:
            print(e)

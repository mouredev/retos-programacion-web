import json


class MiniChallenge:
    def __init__(
            self,
            title: str,
            id: str,
            file: str):

        self.title = title
        self.id = id
        self.file = file


with open("assets/data/mini.json") as file:
    app_data = json.load(file)

mini_challenges = [
    MiniChallenge(
        item["title"],
        item["id"],
        item["file"]
    )
    for item in reversed(app_data)
]

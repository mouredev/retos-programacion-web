import json


class Challenge:
    def __init__(
            self,
            title: str,
            code: list,
            url: str,
            solution: str = "",
            community: str = "",
            video: str = "",
            video_title: str = "",
            level: int = 0,
            date="",
            event=""):

        self.title = title
        self.code = "\n".join(code)
        self.url = url
        self.solution = solution
        self.community = community
        self.video = video
        self.video_title = video_title
        self.level = level
        self.date = date
        self.event = event


with open("assets/data/projects.json") as file:
    app_data = json.load(file)

projects_challenges = [
    Challenge(
        item["title"],
        item["code"],
        item["url"],
        item.get("solution", "")
    )
    for item in app_data
]

with open("assets/data/exercises.json") as file:
    exercises_data = json.load(file)

exercises_challenges = [
    Challenge(
        item["title"],
        item["code"],
        item["url"],
        item.get("solution", ""),
        item.get("community", ""),
        item.get("video", ""),
        item.get("video_title", ""),
        item.get("level", 0),
        item.get("date", "")
    )
    for item in exercises_data
]

with open("assets/data/roadmap.json") as file:
    roadmap_data = json.load(file)

roadmap_challenges = [
    Challenge(
        item["title"],
        item["code"],
        item.get("url", ""),
        item.get("solution", ""),
        item.get("community", ""),
        item.get("video", ""),
        item.get("video_title", ""),
        item.get("level", 0),
        item.get("date", ""),
        item.get("event", "")
    )
    for item in roadmap_data
]

# Penúltimo elemento correspondiente al último reto
# last_roadmap_challenge = roadmap_challenges[1]

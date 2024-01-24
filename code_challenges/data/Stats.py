import requests


class ChallengeRanking:
    def __init__(self, order: int, name: str, count: int):
        self.order = order
        self.name = name
        self.count = count


class LanguageRanking(ChallengeRanking):
    def __init__(self, order: int, name: str, count: int, percentage: float):
        super().__init__(order, name, count)
        self.percentage = percentage


class UserRanking(ChallengeRanking):
    def __init__(self, order: int, name: str, count: int, languages: int):
        super().__init__(order, name, count)
        self.languages = languages


class Stats:
    def __init__(
        self,
        challenges_total,
        languages_total,
        files_total,
        users_total,
        challenges_ranking,
        languages_ranking,
        users_ranking
    ):
        self.challenges_total = challenges_total
        self.languages_total = languages_total
        self.files_total = files_total
        self.users_total = users_total
        self.challenges_ranking = challenges_ranking
        self.languages_ranking = languages_ranking
        self.users_ranking = users_ranking


response = requests.get(
    "https://raw.githubusercontent.com/mouredev/roadmap-retos-programacion/main/Roadmap/stats.json"
)
stats_data = response.json()

challenges_ranking = [
    ChallengeRanking(**item)
    for item in stats_data["challenges_ranking"]
]

languages_ranking = [
    LanguageRanking(**item)
    for item in stats_data["languages_ranking"]
]

users_ranking = [
    UserRanking(**item)
    for item in stats_data["users_ranking"]
]

roadmap_stats = Stats(
    stats_data["challenges_total"],
    stats_data["languages_total"],
    stats_data["files_total"],
    stats_data["users_total"],
    challenges_ranking,
    languages_ranking,
    users_ranking
)

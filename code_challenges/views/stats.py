import reflex as rx
import code_challenges.styles.styles as styles
from code_challenges.routes import Route
from code_challenges.data.Stats import Stats, LanguageRanking, ChallengeRanking, UserRanking
from code_challenges.styles.styles import Spacing, TextColor
from code_challenges.components.milestone import milestone, Milestone
from code_challenges.components.button import button


def stats(stats: Stats) -> rx.Component:
    return rx.vstack(
        rx.link(
            rx.flex(
                milestone(
                    stats.languages_total,
                    "Lenguajes",
                    _languages(stats.languages_ranking),
                    TextColor.YELLOW
                ),
                milestone(
                    stats.files_total,
                    "Contribuciones",
                    _challenges(stats.challenges_ranking),
                    TextColor.GREEN
                ),
                milestone(
                    stats.users_total,
                    "Usuarios",
                    _users(stats.users_ranking),
                    TextColor.PINK
                ),
                spacing=Spacing.BIG.value,
                flex_direction=styles.FLEX_DIRECTION
            ),
            href=Route.ROADMAP_RANKING.value,
            width="100%"
        ),
        button(
            "Ver el ranking completo",
            Route.ROADMAP_RANKING.value,
            is_external=False
        ),
        spacing=Spacing.BIG.value,
        style=styles.max_width_style
    )


def _languages(languages: list[LanguageRanking]) -> list[Milestone]:
    milestones = []
    for index in range(5):
        language = languages[index]
        milestones.append(
            Milestone(
                f"devicon-{language.name}-plain",
                f"{language.name} ({language.count})",
                True
            )
        )
    return milestones


def _challenges(challenges: list[ChallengeRanking]) -> list[Milestone]:
    milestones = []
    for index in range(5):
        challenge = challenges[index]
        milestones.append(
            Milestone(
                "/icons/star.svg",
                f"#{challenge.name.split(' - ')[0]} ({challenge.count})"
            )
        )
    return milestones


def _users(users: list[UserRanking]) -> list[Milestone]:
    milestones = []
    for index in range(5):
        user = users[index]
        milestones.append(
            Milestone(
                "/icons/trophy.svg",
                f"#{user.order} {user.name} ({user.count})"
            )
        )
    return milestones

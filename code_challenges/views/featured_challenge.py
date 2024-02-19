import reflex as rx
import code_challenges.styles.styles as styles
from code_challenges.styles.styles import Spacing, TextColor
from code_challenges.components.card import card
from code_challenges.components.button import button
from code_challenges.data.Challenge import Challenge


def featured_challenge(url: str, challenge: Challenge) -> rx.Component:
    return rx.vstack(
        card(
            url,
            "Último ejercicio publicado en la ruta de estudio",
            challenge.title.capitalize(),
            TextColor.PURPLE,
            challenge.date,
            True
        ),
        rx.hstack(
            button(
                "Ver el reto",
                url,
                "/icons/dark/arrow.svg",
                False,
                False
            ),
            button(
                "Horario",
                challenge.event,
                "/icons/light/discord.svg",
                True
            ),
            spacing=Spacing.DEFAULT_BIG.value
        ),
        spacing=Spacing.BIG.value,
        style=styles.max_width_style
    )

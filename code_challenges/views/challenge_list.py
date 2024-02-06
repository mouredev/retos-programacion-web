import reflex as rx
import code_challenges.styles.styles as styles
from code_challenges.styles.styles import Size
from code_challenges.components.challenge import challenge
from code_challenges.data.Challenge import Challenge


def challenge_list(challenges: list[Challenge], roadmap=False) -> rx.Component:
    return rx.box(
        rx.accordion(
            *[
                challenge(
                    data,
                    "last" if (index == 0 and roadmap) else str(index),
                    roadmap,
                    index == len(challenges) - 1
                )
                for index, data in enumerate(challenges)
            ],
            allow_toggle=True,
            default_index=[1 if roadmap else None]
        ),
        style=styles.max_width_style
    )

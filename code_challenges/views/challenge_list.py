import reflex as rx
import code_challenges.styles.styles as styles
from code_challenges.styles.styles import Size
from code_challenges.components.challenge import challenge
from code_challenges.data.Challenge import Challenge


def challenge_list(challenges: list[Challenge], roadmap=False) -> rx.Component:
    return rx.box(
        rx.cond(
            roadmap,
            rx.vstack(
                *[
                    challenge(
                        data,
                        roadmap,
                        "last" if index == 1 and roadmap else None
                    )
                    for index, data in enumerate(challenges)
                ],
                spacing="6em",
            ),
            rx.vstack(
                *[
                    challenge(data)
                    for data in challenges
                ],
                spacing=Size.BIG.value,
            )
        ),
        style=styles.max_width_style
    )

import reflex as rx
import reflex_chakra as rc
import code_challenges.styles.styles as styles
from code_challenges.styles.styles import Size
from code_challenges.components.challenge import challenge
from code_challenges.data.Challenge import Challenge


def challenge_list(challenges: list[Challenge], in_progress=False) -> rx.Component:
    return rx.box(
        rc.accordion(
            *[
                challenge(
                    data,
                    "last" if (index == 0 and in_progress) else str(index),
                    in_progress,
                    index == len(challenges) - 1
                )
                for index, data in enumerate(challenges)
            ],
            allow_toggle=True,
            default_index=[0 if in_progress else None]
        ),
        style=styles.max_width_style
    )

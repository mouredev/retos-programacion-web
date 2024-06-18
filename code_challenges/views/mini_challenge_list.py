import reflex as rx
import code_challenges.styles.styles as styles
from code_challenges.styles.styles import Size
from code_challenges.data.MiniChallenge import MiniChallenge
from code_challenges.components.mini_challenge import mini_challenge


def mini_challenge_list(challenges: list[MiniChallenge]) -> rx.Component:
    return rx.vstack(
        rx.chakra.responsive_grid(
            *[
                mini_challenge(challenge)
                for challenge in challenges
            ],
            columns=[1, 2, 2, 2, 3],
            spacing=Size.BIG.value,
            width="100%"
        ),
        style=styles.max_width_style
    )

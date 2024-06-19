import reflex as rx
import code_challenges.styles.styles as styles
from code_challenges.styles.fonts import FontWeight
from code_challenges.styles.styles import Size, Spacing
from code_challenges.data.MiniChallenge import MiniChallenge


def mini_challenge(data: MiniChallenge) -> rx.Component:
    return rx.vstack(
        rx.video(
            url=f"https://www.youtube.com/embed/{data.id}",
            playing=True,
            light=True,
            width="100%",
            height="auto",
            aspect_ratio="9/16",
            border_radius=Size.SMALL.value,
            overflow="hidden"
        ),
        rx.text(
            data.title.upper(),
            font_size=styles.Size.DEFAULT_MEDIUM.value,
            font_weight=FontWeight.BOLD.value
        ),
        spacing=Spacing.DEFAULT.value,
        style=styles.container_style
    )

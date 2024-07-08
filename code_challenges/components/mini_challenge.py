import reflex as rx
import code_challenges.styles.styles as styles
from code_challenges.styles.colors import TextColor
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
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/light/github.svg",
                    width=Size.DEFAULT_BIG.value,
                    height=Size.DEFAULT_BIG.value,
                    alt=f"Icono que representa la navegación a GitHub"
                ),
                rx.text(
                    data.title.upper(),
                    font_size=styles.Size.DEFAULT_MEDIUM.value,
                    font_weight=FontWeight.BOLD.value,
                    color=TextColor.PRIMARY.value
                ),
                width="100%",
                align_items="top",
                spacing=Spacing.DEFAULT.value
            ),
            href=f"https://github.com/mouredev/retos-programacion-mini/blob/main/Mini/{data.file}",
            is_external=True
        ),
        spacing=Spacing.DEFAULT.value,
        style=styles.container_style
    )

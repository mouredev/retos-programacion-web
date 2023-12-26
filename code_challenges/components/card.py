import reflex as rx
import code_challenges.styles.styles as styles
from code_challenges.styles.styles import Size
from code_challenges.styles.colors import TextColor
from .heading import heading
from .badge import badge


def card(url: str, title: str, body="", color=TextColor.PRIMARY, badge_text="", featured=False) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.cond(
                badge_text != "",
                rx.box(
                    badge(badge_text),
                    width="100%"
                )
            ),
            rx.hstack(
                heading(
                    title,
                    color
                ),
                rx.image(
                    src="/icons/light/arrow.svg",
                    width=Size.BIG.value,
                    height=Size.BIG.value,
                    alt="Icono con una flecha hacia la derecha"
                ),
                width="100%"
            ),
            rx.cond(
                body != "",
                rx.text(
                    body,
                    font_size=Size.DEFAULT_BIG.value,
                    color=TextColor.SECONDARY.value,
                    width="100%"
                )
            ),
            height="100%",
            style=styles.featured_container_style if featured else styles.container_style
        ),
        href=url,
        width="100%"
    )

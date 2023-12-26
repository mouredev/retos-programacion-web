import reflex as rx
import code_challenges.styles.styles as styles
from code_challenges.styles.styles import Size


def button(text: str, url: str, image="/icons/dark/arrow.svg", secondary=False, is_external=True) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.cond(
                    text != "",
                    rx.text(text)
                ),
                rx.image(
                    src=image,
                    width=Size.DEFAULT.value,
                    height=Size.DEFAULT.value,
                    alt=f"Icono que representa la navegación a \"{text}\""
                )
            ),
            alt=f"Icono que representa la navegación a \"{text}\"",
            style=styles.button_secondary_style if secondary else styles.button_style
        ),
        href=url,
        is_external=is_external
    )

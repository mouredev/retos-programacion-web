import reflex as rx
import datetime
import code_challenges.constants as const
import code_challenges.styles.styles as styles
from code_challenges.styles.styles import Size, Color, TextColor, Font


def footer() -> rx.Component:
    return rx.stack(
        rx.hstack(
            rx.image(
                src="/logo.png",
                height=Size.BIG.value,
                width=Size.BIG.value,
                alt="Logotipo de MoureDev. Una \"eme\" entre llaves."
            ),
            rx.link(
                rx.box(
                    "Creado con 🤍 (y gracias a ti) por ",
                    rx.span("MoureDev by Brais Moure",
                            color=TextColor.BLUE.value),
                    "."
                ),
                href=const.MOUREDEV_URL,
                is_external=True,
                font_family=Font.NEON.value
            ),
            spacing=Size.DEFAULT.value
        ),
        rx.spacer(),
        rx.link(
            rx.text(
                f"© 2022-{datetime.date.today().year}. v3.0.",
                font_family=Font.KRYPTON.value,
                color=TextColor.SECONDARY.value
            ),
            href=const.GITHUB_WEB_REPO_URL,
            is_external=True,
            text_align="end"
        ),
        direction=styles.STACK_DIRECTION,
        border_top=f"1px solid {Color.SECONDARY.value}",
        padding=Size.BIG.value,
        width="100%"
    )

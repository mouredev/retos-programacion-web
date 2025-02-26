import reflex as rx
import datetime
import code_challenges.constants as const
import code_challenges.styles.styles as styles
from code_challenges.styles.styles import Size, Spacing, Color, TextColor, Font


def footer() -> rx.Component:
    return rx.flex(
        rx.flex(
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
                        rx.text(
                            "MoureDev by Brais Moure",
                            color=TextColor.BLUE.value,
                            as_="span"
                        ),
                        ".",
                        color=TextColor.PRIMARY.value
                    ),
                    href=const.MOUREDEV_URL,
                    is_external=True,
                    font_family=Font.NEON.value
                ),
                spacing=Spacing.DEFAULT.value,
                align="center"
            ),
            rx.text(
                "Con el apoyo de",
                rx.image(
                    src=f"/raiola_networks.svg",
                    on_click=rx.redirect(
                        const.RAIOLA_NETWORKS_URL,
                        is_external=True
                    ),
                    width="200px",
                    height="100%",
                    cursor="pointer",
                    padding_x=Size.MEDIUM.value,
                    alt="Logo Raiola Networks"
                ),
                font_family=Font.NEON.value,
                display="flex",
                align_items="center"
            ),
            spacing=Spacing.SMALL.value,
            flex_direction=styles.FLEX_DIRECTION
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
        spacing=Spacing.SMALL.value,
        flex_direction=styles.FLEX_DIRECTION,
        border_top=f"1px solid {Color.SECONDARY.value}",
        padding=Size.BIG.value,
        width="100%"
    )

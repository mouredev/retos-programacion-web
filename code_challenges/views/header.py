import reflex as rx
import code_challenges.constants as constants
import code_challenges.styles.styles as styles
from code_challenges.styles.styles import Size
from code_challenges.styles.fonts import Font, FontWeight
from code_challenges.styles.colors import TextColor
from code_challenges.components.title import title
from code_challenges.components.button import button

TITLE_SIZE = ["2.2em", Size.VERY_BIG.value]
SUBTITLE_SIZE = [Size.DEFAULT_BIG.value, Size.BIG.value]


def header(
    subtitle=".com",
    body="Ejercicios y proyectos para mejorar tu lógica de programación",
    github=constants.GITHUB_URL
) -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                title(
                    "{",
                    Font.ARGON,
                    FontWeight.BOLD,
                    TITLE_SIZE,
                    TextColor.GREEN
                ),
                rx.vstack(
                    title(
                        "Retos",
                        Font.NEON,
                        FontWeight.BOLD,
                        TITLE_SIZE,
                        TextColor.BLUE
                    ),
                    title(
                        "de",
                        Font.RADON,
                        FontWeight.BOLD,
                        TITLE_SIZE,
                        TextColor.PURPLE
                    ),
                    title(
                        "Programación",
                        Font.NEON,
                        FontWeight.BOLD,
                        TITLE_SIZE,
                        TextColor.BLUE
                    ),
                    title(
                        subtitle,
                        Font.KRYPTON,
                        FontWeight.BOLD,
                        SUBTITLE_SIZE,
                        TextColor.PINK
                    ),
                    spacing=f"-{Size.VERY_SMALL.value}",
                    padding_left=Size.VERY_BIG.value,
                    align_items="start"
                ),
                title(
                    "}",
                    Font.ARGON,
                    FontWeight.BOLD,
                    TITLE_SIZE,
                    TextColor.GREEN
                ),
                rx.link(
                    title(
                        "by mouredev",
                        Font.MOUREDEV,
                        FontWeight.MEDIUM,
                        SUBTITLE_SIZE,
                        TextColor.PRIMARY
                    ),
                    href=constants.MOUREDEV_URL,
                    is_external=True,
                    text_align="right",
                    width="100%"
                ),
                rx.center(
                    rx.vstack(
                        rx.text(
                            body,
                            font_size=SUBTITLE_SIZE,
                            font_weight=FontWeight.BOLD.value,
                            padding_top=Size.BIG.value,
                            text_align="center",
                        ),
                        rx.tablet_and_desktop(
                            _social_buttons(github)
                        ),
                        rx.mobile_only(
                            _social_buttons(github, True)
                        ),
                        spacing=Size.BIG.value
                    ),
                    width="100%"
                ),
                spacing=f"-{Size.VERY_SMALL.value}",
                padding_y=Size.VERY_BIG.value,
                style=styles.max_width_style
            ),
            style=styles.background_gradient_style
        ),
        width="100%",
        style=styles.background_pattern_style
    )


def _social_buttons(github: str, mobile=False) -> rx.Component:
    return rx.hstack(
        button(
            "" if mobile else "GitHub",
            github,
            "/icons/dark/github.svg"
        ),
        button(
            "" if mobile else "Discord",
            constants.DISCORD_URL,
            "/icons/light/discord.svg",
            True
        ),
        button(
            "" if mobile else "Twitch",
            constants.TWITCH_URL,
            "/icons/light/twitch.svg",
            True
        ),
        spacing=Size.BIG.value
    )

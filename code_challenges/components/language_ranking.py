import reflex as rx
import code_challenges.styles.styles as styles
from code_challenges.styles.styles import Size, Spacing, TextColor, FontWeight
from code_challenges.data.Stats import LanguageRanking

DEVICON = {
    "c#": "csharp", "c++": "cplusplus", "sql": "azuresqldatabase", "cobol": "devicon",
    "mojo": "devicon", "pascal": "devicon", "vb.net": "visualbasic", "ada": "devicon",
    "racket": "devicon", "tcl": "devicon"
}


def language_ranking(language: LanguageRanking) -> rx.Component:
    return rx.box(
        rx.text(
            f"#{language.order}",
            font_size=Size.DEFAULT_MEDIUM.value,
            font_weight=FontWeight.BOLD.value,
            position="absolute",
            padding=Size.DEFAULT.value
        ),
        rx.vstack(
            rx.box(
                class_name=f"devicon-{DEVICON.get(language.name.lower(), language.name.lower())}-plain",
                font_size=Size.BIG.value,
                height="100%"
            ),
            rx.text(
                language.name.upper(),
                font_size=Size.DEFAULT_MEDIUM.value,
                font_weight=FontWeight.BOLD.value
            ),
            rx.text(
                f"{language.percentage}% | {language.count}",
                font_size=Size.MEDIUM.value,
                color=TextColor.SECONDARY.value
            ),
            height="100%",
            align="center",
            spacing=Spacing.VERY_SMALL.value,
            style=styles.featured_container_style if language.order <= 3 else styles.container_style
        )
    )

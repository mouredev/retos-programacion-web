import reflex as rx
import code_challenges.styles.styles as styles
from code_challenges.routes import Route
from code_challenges.styles.styles import Size, TextColor, Font, FontWeight
from code_challenges.components.share import share

langs: list[str] = [
    "Python", "Swift", "Kotlin", "Java", "C++", "PHP", "Rust", "Go", "JavaScript",
    "Dart", "Ruby", "C#", "TypeScript", "Cobol", "Lua", "C", "PowerShell", "Assembly",
    "R", "Objective-C", "F#", "Haskell", "Fortran", "Lisp", "Scala", "Perl", "Groovy",
    "Solidity", "Ada", "Plankalkül"
]

fonts: list[Font] = [
    Font.NEON, Font.ARGON, Font.XENON, Font.RADON, Font.KRYPTON
]
colors: list[TextColor] = [
    TextColor.PINK, TextColor.YELLOW, TextColor.GREEN, TextColor.BLUE, TextColor.PURPLE
]


def languages(route: Route) -> rx.Component:
    return rx.vstack(
        share(route),
        rx.box(
            rx.box(
                rx.text(
                    _language_start(
                        ">_"
                    ),
                    *[
                        _language(
                            index,
                            lang
                        )
                        for index, lang in enumerate(langs)
                    ],
                    font_weight=FontWeight.BOLD.value,
                    font_size=Size.BIG.value,
                ),
                rx.text(
                    _language_start(
                        ">_"
                    ),
                    *[
                        _language(
                            index,
                            lang
                        )
                        for index, lang in enumerate(langs)
                    ],
                    font_weight=FontWeight.BOLD.value,
                    font_size=Size.BIG.value,
                )
            ),
            class_name="marquee"
        ),
        spacing=Size.MEDIUM_BIG.value,
        width="100%"
    )


def _language_start(text: str) -> rx.Component:
    return rx.span(
        text,
        font_family=Font.KRYPTON.value,
        custom_attrs={
            styles.CustomAttrs.DATA_TEXT.value: text,
        },
        style=styles.glow_text_style
    )


def _language(index: int, text: str) -> rx.Component:
    return rx.span(
        text,
        font_family=fonts[index % len(fonts)].value,
        color=colors[index % len(colors)].value,
        custom_attrs={
            styles.CustomAttrs.DATA_TEXT.value: text,
        },
        style=styles.glow_text_style
    )

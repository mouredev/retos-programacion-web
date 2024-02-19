import reflex as rx
import code_challenges.styles.styles as styles
from code_challenges.styles.styles import Size, Spacing, Color, TextColor, FontWeight
from code_challenges.components.heading import heading


class FAQ:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


def faq(faq: list[FAQ]) -> rx.Component:
    return rx.vstack(
        rx.vstack(
            heading("Preguntas frecuentes"),
            rx.tablet_and_desktop(
                rx.grid(
                    *[
                        _faq_text(
                            data.question,
                            data.answer
                        )
                        for data in faq
                    ],
                    columns="2",
                    gap=Size.MEDIUM_BIG.value
                )
            ),
            rx.mobile_only(
                rx.grid(
                    *[
                        _faq_text(
                            data.question,
                            data.answer
                        )
                        for data in faq
                    ],
                    gap=Size.MEDIUM_BIG.value
                )
            ),
            spacing=Spacing.BIG.value,
            style=styles.max_width_style
        ),
        id="faq",
        background=Color.SECONDARY.value,
        padding_y=Size.VERY_BIG.value,
        align="center",
        width="100%"
    )


def _faq_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            font_size=Size.DEFAULT_MEDIUM.value,
            font_weight=FontWeight.BOLD.value,
            color=TextColor.PINK.value,
            padding_bottom=Size.DEFAULT.value
        ),
        rx.text(
            body,
            font_size=Size.DEFAULT.value,
            font_weight=FontWeight.BOLD.value,
        ),
        row_span=1,
        col_span=1
    )

import reflex as rx
import code_challenges.styles.styles as styles
from code_challenges.styles.styles import Size, TextColor, FontWeight
from .heading import heading


class Milestone:
    def __init__(self, icon: str, text: str, class_name=False):
        self.icon = icon
        self.text = text
        self.class_name = class_name


def milestone(number: int, title: str, body: list[Milestone], color=TextColor.PRIMARY) -> rx.Component:
    return rx.vstack(
        heading(
            number,
            color
        ),
        rx.text(
            title,
            font_size=Size.DEFAULT_BIG.value,
            color=TextColor.SECONDARY.value
        ),
        rx.vstack(
            *[
                rx.hstack(
                    rx.cond(
                        item.class_name,
                        rx.box(
                            class_name=item.icon,
                            height=Size.DEFAULT.value
                        ),
                        rx.image(
                            src=item.icon,
                            height=Size.DEFAULT.value
                        )
                    ),
                    rx.text(
                        item.text,
                        font_weight=FontWeight.BOLD.value
                    )
                )
                for item in body
            ],
            width="100%",
            align_items="start",
            spacing=Size.ZERO.value
        ),
        width="100%",
        align_items="start",
        style=styles.container_style
    )

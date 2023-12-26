import reflex as rx
from code_challenges.styles.styles import Size
from code_challenges.styles.fonts import FontWeight
from .heading import heading


def paragraph(title: str, body1="", body2="") -> rx.Component:
    return rx.vstack(
        heading(title),
        rx.grid(
            _paragraph_text(body1),
            _paragraph_text(body2),
            template_rows="repeat(1, 1fr)",
            template_columns="repeat(2, 1fr)",
            width="100%",
            gap=Size.MEDIUM_BIG.value
        ),
        spacing=Size.BIG.value,
        padding_x=Size.ZERO.value,
        width="100%"
    )


def _paragraph_text(text: str) -> rx.Component:
    return rx.grid_item(
        rx.text(
            text,
            font_size=Size.DEFAULT_MEDIUM.value,
            font_weight=FontWeight.BOLD.value
        ),
        row_span=1,
        col_span=1
    )

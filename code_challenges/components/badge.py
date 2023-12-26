import reflex as rx
from code_challenges.styles.styles import Size
from code_challenges.styles.colors import TextColor


def badge(text: str, color=TextColor.PINK, small=False) -> rx.Component:
    return rx.box(
        rx.badge(
            text,
            padding_x=Size.DEFAULT.value if small else Size.BIG.value,
            padding_y=Size.VERY_SMALL.value if small else Size.SMALL.value,
            background="transparent",
            color=color.value,
            border_color=color.value,
            border_width=1 if small else 2,
            border_radius=Size.BIG.value
        ),
        padding_bottom=Size.ZERO.value if small else Size.SMALL.value,
    )

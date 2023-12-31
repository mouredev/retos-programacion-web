import reflex as rx
from code_challenges.styles.styles import TextColor


def heading(text: str, color=TextColor.PRIMARY, size="2xl") -> rx.Component:
    return rx.heading(
        text,
        size=size,
        color=color.value,
        width="inherit"
    )

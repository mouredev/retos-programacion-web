import reflex as rx
from code_challenges.styles.styles import TextColor


def heading(text: str, color=TextColor.PRIMARY, size="2xl", auto=False) -> rx.Component:
    return rx.chakra.heading(
        text,
        size=size,
        color=color.value,
        width="auto" if auto else "inherit"
    )

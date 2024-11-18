import reflex as rx
import reflex_chakra as rc
from code_challenges.styles.styles import TextColor


def heading(text: str, color=TextColor.PRIMARY, size="2xl", auto=False) -> rx.Component:
    return rc.heading(
        text,
        size=size,
        color=color.value,
        width="auto" if auto else "inherit"
    )

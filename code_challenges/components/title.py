import reflex as rx
import code_challenges.styles.styles as styles
from code_challenges.styles.styles import Size
from code_challenges.styles.colors import TextColor
from code_challenges.styles.fonts import Font, FontWeight


def title(text: str, font=Font.DEFAULT, weight=FontWeight.BOLD, size=[Size.DEFAULT_BIG.value], color=TextColor.PRIMARY) -> rx.Component:
    return rx.text(
        text,
        font_family=font.value,
        font_weight=weight.value,
        font_size=size,
        color=color.value,
        custom_attrs={
            styles.CustomAttrs.DATA_TEXT.value: text,
        },
        style=styles.glow_text_style
    )

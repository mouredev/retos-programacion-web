import reflex as rx
import code_challenges.styles.styles as styles
from code_challenges.styles.styles import Size, Spacing, TextColor, FontWeight
from code_challenges.data.Stats import UserRanking


def user_ranking(user: UserRanking) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.cond(
                user.order <= 3,
                rx.image(
                    src="/icons/trophy.svg",
                    height=Size.DEFAULT_BIG.value
                )
            ),
            rx.text(
                f"#{user.order}",
                font_size=Size.DEFAULT_MEDIUM.value,
                font_weight=FontWeight.BOLD.value,
            ),
            position="absolute",
            padding=Size.DEFAULT.value
        ),
        rx.hstack(

            rx.cond(
                user.order <= 15,
                rx.image(
                    src=f"https://github.com/{user.name}.png?size=32",
                    width=Size.BIG.value,
                    height=Size.BIG.value,
                    border_radius="50%"
                )
            ),
            rx.vstack(
                rx.text(
                    user.name,
                    font_size=Size.DEFAULT_MEDIUM.value,
                    font_weight=FontWeight.BOLD.value
                ),
                rx.text(
                    f"{user.count} contribuciones | {user.languages} lenguajes",
                    font_size=Size.MEDIUM.value,
                    color=TextColor.SECONDARY.value
                ),
                align_items="start",
                spacing=Spacing.ZERO.value
            ),
            spacing=Spacing.DEFAULT.value,
            style=styles.featured_container_style if user.order <= 3 else styles.container_style
        ),
        href=f"https://github.com/{user.name}",
        is_external=True
    )

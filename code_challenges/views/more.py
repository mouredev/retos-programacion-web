import reflex as rx
import reflex_chakra as rc
import code_challenges.styles.styles as styles
from code_challenges.routes import Route
from code_challenges.styles.styles import Size, TextColor
from code_challenges.components.paragraph import paragraph
from code_challenges.components.card import card


def more(route: Route) -> rx.Component:
    return rx.vstack(
        paragraph(
            "Sigue practicando"
        ),
        rc.responsive_grid(
            rx.cond(
                route != Route.APPLIED_LOGIC,
                rx.box(
                    card(
                        Route.APPLIED_LOGIC.value,
                        "Lógica aplicada",
                        color=TextColor.PINK,
                        badge_text="2025"
                    )
                )
            ),
            rx.cond(
                route != Route.ROADMAP,
                rx.box(
                    card(
                        Route.ROADMAP.value,
                        "Roadmap de retos",
                        color=TextColor.PURPLE
                    )
                )
            ),
            rx.cond(
                route != Route.MINI,
                rx.box(
                    card(
                        Route.MINI.value,
                        "Mini ejercicios",
                        color=TextColor.BLUE
                    )
                )
            ),
            rx.cond(
                route != Route.EXERCISES,
                rx.box(
                    card(
                        Route.EXERCISES.value,
                        "Ejercicios lógicos",
                        color=TextColor.GREEN
                    )
                )
            ),
            rx.cond(
                route != Route.PROJECTS,
                rx.box(
                    card(
                        Route.PROJECTS.value,
                        "Proyectos completos",
                        color=TextColor.YELLOW
                    )
                )
            ),
            columns=[1, 1, 1, 2],
            spacing=Size.BIG.value,
            width="100%"
        ),
        style=styles.max_width_style
    )

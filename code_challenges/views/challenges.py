import reflex as rx
import reflex_chakra as rc
import code_challenges.styles.styles as styles
from code_challenges.routes import Route
from code_challenges.styles.styles import Spacing, TextColor
from code_challenges.components.paragraph import paragraph
from code_challenges.components.card import card


def challenges() -> rx.Component:
    return rx.vstack(
        paragraph(
            "Mejora tus habilidades.",
            "Resuelve a tu ritmo ejercicios inspirados en pruebas técnicas usando el lenguaje de programación que tú quieras.",
            "Totalmente gratis y en constante actualización, con correcciones en directo y el apoyo de la comunidad."
        ),
        rx.tablet_and_desktop(
            rc.grid(
                rc.grid_item(
                    _applied_login_card(),
                    col_span=5
                ),
                rc.grid_item(
                    _roadmap_card(),
                    col_span=3
                ),
                rc.grid_item(
                    _mini_card(),
                    col_span=2
                ),
                rc.grid_item(
                    _projects_card(),
                    col_span=2
                ),
                rc.grid_item(
                    _exercises_card(),
                    col_span=3
                ),
                template_rows="repeat(3, 1fr)",
                template_columns="repeat(5, 1fr)",
                gap=Spacing.BIG.value
            )
        ),
        rx.mobile_only(
            rx.vstack(
                _applied_login_card(),
                _roadmap_card(),
                _mini_card(),
                _exercises_card(),
                _projects_card(),
                spacing=Spacing.BIG.value
            )
        ),
        spacing=Spacing.VERY_BIG.value,
        style=styles.max_width_style
    )


def _applied_login_card() -> rx.Component:
    return card(
        Route.ROADMAP.value,
        "Lógica aplicada",
        "Proyectos para practicar lógica y aprender a implementar diferentes funcionalidades reales y habituales en todo tipo de aplicaciones.",
        TextColor.PINK,
        "2025"
    )


def _roadmap_card() -> rx.Component:
    return card(
        Route.ROADMAP.value,
        "Roadmap de retos",
        "51 ejercicios para aprender cualquier lenguaje de programación siguiendo una ruta de estudio de todos sus fundamentos desde cero. Pon a prueba tus conocimientos.",
        TextColor.PURPLE,
        "2024"
    )


def _mini_card() -> rx.Component:
    return card(
        Route.MINI.value,
        "Mini retos",
        "Ejercicios lógicos en formato vídeo corto de menos de un minuto.",
        TextColor.BLUE,
        "Shorts/Reels/TikTok"
    )


def _exercises_card() -> rx.Component:
    return card(
        Route.EXERCISES.value,
        "Ejercicios lógicos",
        "101 retos de código para practicar tus habilidades con cualquier lenguaje de programación.",
        TextColor.GREEN
    )


def _projects_card() -> rx.Component:
    return card(
        Route.PROJECTS.value,
        "Proyectos completos",
        "12 aplicaciones pensadas para añadir en tu portafolio personal.",
        TextColor.YELLOW
    )

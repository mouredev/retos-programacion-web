import reflex as rx
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
            rx.chakra.grid(
                rx.chakra.grid_item(
                    _roadmap_card(),
                    col_span=5
                ),
                rx.chakra.grid_item(
                    _exercises_card(),
                    col_span=3
                ),
                rx.chakra.grid_item(
                    _projects_card(),
                    col_span=2
                ),
                template_rows="repeat(2, 1fr)",
                template_columns="repeat(5, 1fr)",
                gap=Spacing.BIG.value
            )
        ),
        rx.mobile_only(
            rx.vstack(
                _roadmap_card(),
                _exercises_card(),
                _projects_card(),
                spacing=Spacing.BIG.value
            )
        ),
        spacing=Spacing.VERY_BIG.value,
        style=styles.max_width_style
    )


def _roadmap_card() -> rx.Component:
    return card(
        Route.ROADMAP.value,
        "Roadmap de retos",
        "Ejercicios para aprender cualquier lenguaje de programación siguiendo una ruta de estudio de todos sus fundamentos desde cero. Cada semana un nuevo reto para poner a prueba tus conocimientos.",
        TextColor.PURPLE,
        "Nuevo 2024"
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

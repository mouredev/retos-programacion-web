import reflex as rx
import code_challenges.styles.styles as styles
import code_challenges.utils as utils
import code_challenges.constants as constants
from code_challenges.routes import Route
from code_challenges.styles.styles import Size
from code_challenges.views.navbar import navbar
from code_challenges.views.header import header
from code_challenges.components.paragraph import paragraph
from code_challenges.views.challenge_list import challenge_list
from code_challenges.views.more import more
from code_challenges.views.languages import languages
from code_challenges.views.footer import footer
from code_challenges.data.Challenge import projects_challenges

ROUTE = Route.PROJECTS


@rx.page(
    route=ROUTE.value,
    title=utils.title_projects,
    description=utils.description_projects,
    image=utils.preview_projects,
    meta=utils.meta_projects
)
def projects() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(ROUTE),
        rx.center(
            rx.vstack(
                header(
                    "proyectos",
                    "12 aplicaciones pensadas para añadir a tu portafolio personal",
                    constants.GITHUB_PROJECTS_REPO_URL
                ),
                rx.vstack(
                    paragraph(
                        "Web o App. Tú eliges la tecnología.",
                        "Este es un listado de proyectos reales que pueden ayudarte a darte ideas y elaborar un portafolio personal que marque la diferencia. Cada aplicación está pensada para potenciar diferentes habilidades.",
                        "Con el apoyo de la comunidad. Encontrarás soluciones a los ejercicios en tecnologías como React, Angular, Flutter, Vue, Jetpack Compose, Android Views, SwiftUI, UIKit, React Native, Svelte…"
                    ),
                    style=styles.max_width_style
                ),
                challenge_list(projects_challenges),
                more(ROUTE),
                languages(ROUTE),
                footer(),
                spacing=Size.VERY_BIG.value,
                width="100%"
            )
        ),
    )

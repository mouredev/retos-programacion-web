import reflex as rx
import code_challenges.utils as utils
import code_challenges.constants as constants
from code_challenges.routes import Route
from code_challenges.styles.styles import Size
from code_challenges.views.navbar import navbar
from code_challenges.views.header import header
from code_challenges.views.languages import languages
from code_challenges.views.more import more
from code_challenges.views.footer import footer

ROUTE = Route.ROADMAP_RANKING
MAIN_ROUTE = Route.ROADMAP


@rx.page(
    route=ROUTE.value,
    title=utils.title_roadmap_ranking,
    description=utils.description_roadmap_ranking,
    image=utils.preview_roadmap,
    meta=utils.meta_roadmap
)
def roadmap_ranking() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(MAIN_ROUTE),
        rx.center(
            rx.vstack(
                header(
                    "ranking roadmap",
                    "Estadísticas y participación en la ruta de estudio",
                    constants.GITHUB_ROADMAP_REPO_URL
                ),
                more(MAIN_ROUTE),
                languages(MAIN_ROUTE),
                footer(),
                spacing=Size.VERY_BIG.value,
                width="100%"
            )
        )
    )

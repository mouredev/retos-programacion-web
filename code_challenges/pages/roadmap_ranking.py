import reflex as rx
import code_challenges.utils as utils
import code_challenges.constants as constants
import code_challenges.styles.styles as styles
from code_challenges.routes import Route
from code_challenges.styles.styles import Size, TextColor
from code_challenges.views.navbar import navbar
from code_challenges.views.header import header
from code_challenges.views.languages import languages
from code_challenges.views.more import more
from code_challenges.views.footer import footer
from code_challenges.components.heading import heading
from code_challenges.components.language_ranking import language_ranking
from code_challenges.components.user_ranking import user_ranking
from code_challenges.data.Stats import roadmap_stats

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
                rx.vstack(
                    rx.vstack(
                        heading(f"{roadmap_stats.languages_total} Lenguajes"),
                        heading(
                            f"{roadmap_stats.files_total} Contribuciones",
                            TextColor.YELLOW,
                            "lg"
                        ),
                        rx.text(
                            "* por % de uso y número de contribuciones",
                            color=TextColor.SECONDARY.value
                        ),
                        align_items="start",
                        spacing=Size.VERY_SMALL.value
                    ),
                    rx.responsive_grid(
                        *[
                            language_ranking(language)
                            for language in roadmap_stats.languages_ranking
                        ],
                        columns=[2, 2, 3, 4, 5],
                        spacing=Size.BIG.value,
                        width="100%"
                    ),
                    rx.vstack(
                        heading("Ranking"),
                        heading(
                            f"{roadmap_stats.users_total} Usuarios",
                            TextColor.PINK,
                            "lg"
                        ),
                        rx.text(
                            "* por número de contribuciones y lenguajes diferentes",
                            color=TextColor.SECONDARY.value
                        ),
                        align_items="start",
                        spacing=Size.VERY_SMALL.value
                    ),
                    rx.responsive_grid(
                        *[
                            user_ranking(user)
                            for user in roadmap_stats.users_ranking
                        ],
                        columns=[1, 2, 2, 2, 3],
                        spacing=Size.BIG.value,
                        width="100%"
                    ),
                    rx.text(
                        "* datos actualizados cada 24 horas",
                        color=TextColor.SECONDARY.value
                    ),
                    spacing=Size.VERY_BIG.value,
                    style=styles.max_width_style
                ),
                more(MAIN_ROUTE),
                languages(MAIN_ROUTE),
                footer(),
                spacing=Size.VERY_BIG.value,
                width="100%"
            )
        )
    )

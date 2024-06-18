import reflex as rx
from code_challenges import constants
import code_challenges.styles.styles as styles
import code_challenges.utils as utils
from code_challenges.routes import Route
from code_challenges.styles.styles import Spacing
from code_challenges.views.mini_challenge_list import mini_challenge_list
from code_challenges.views.navbar import navbar
from code_challenges.views.header import header
from code_challenges.components.button import button
from code_challenges.components.paragraph import paragraph
from code_challenges.views.more import more
from code_challenges.views.languages import languages
from code_challenges.views.footer import footer
from code_challenges.data.MiniChallenge import mini_challenges

ROUTE = Route.MINI


@rx.page(
    route=ROUTE.value,
    title=utils.title_mini,
    description=utils.description_mini,
    image=utils.preview_mini,
    meta=utils.meta_mini
)
def mini() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(ROUTE),
        rx.center(
            rx.vstack(
                header(
                    "mini",
                    "Pequeños ejercicios lógicos en menos de un minuto"
                ),
                rx.vstack(
                    paragraph(
                        "Shorts, Reels y TikToks",
                        "Este es un listado de vídeos cortos que puedes encontrar en YouTube, Instagram y Tiktok.",
                        "Aunque se resuelven en unos segundos, te servirán para practicar lógica de una manera rápida."
                    ),
                    rx.hstack(button(
                        "",
                        constants.YOUTUBE_URL,
                        "/icons/light/youtube.svg",
                        True
                    ),
                        button(
                        "",
                        constants.INSTAGRAM_URL,
                        "/icons/light/arrow.svg",
                        True
                    ), button(
                        "",
                        constants.TIKTOK_URL,
                        "/icons/light/arrow.svg",
                        True
                    ),
                        spacing=Spacing.BIG.value,
                    ),
                    spacing=Spacing.BIG.value,
                    style=styles.max_width_style
                ),
                mini_challenge_list(mini_challenges),
                more(ROUTE),
                languages(ROUTE),
                footer(),
                spacing=Spacing.VERY_BIG.value,
                align="center",
                width="100%"
            )
        ),
    )

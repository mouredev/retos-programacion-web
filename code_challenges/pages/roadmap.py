import reflex as rx
import code_challenges.styles.styles as styles
import code_challenges.utils as utils
import code_challenges.constants as constants
from code_challenges.routes import Route
from code_challenges.styles.styles import Spacing
from code_challenges.views.navbar import navbar
from code_challenges.views.header import header
from code_challenges.views.challenge_list import challenge_list
from code_challenges.views.stats import stats
from code_challenges.views.faq import faq, FAQ
from code_challenges.views.languages import languages
from code_challenges.views.more import more
from code_challenges.views.footer import footer
from code_challenges.components.heading import heading
from code_challenges.components.paragraph import paragraph
from code_challenges.components.button import button
from code_challenges.data.Challenge import roadmap_challenges
from code_challenges.data.Stats import roadmap_stats

ROUTE = Route.ROADMAP

FAQ_LIST = [
    FAQ(
        "¿Cómo puedo participar en los retos?",
        "A parte de poder consultar la corrección de los retos en código y vídeo, también puedes enviar tus propias soluciones. Consulta las instrucciones de participación en su repositorio de GitHub y pregunta a la comunidad en Discord."
    ),
    FAQ(
        "¿Puedo utilizar cualquier lenguaje de programación?",
        "Por supuesto. Lo bueno de los retos de lógica es que su principal valor es enseñarnos a pensar y seguir un razonamiento a la hora de resolver un problema. La manera de enfocarlo es independiente al lenguaje de programación."
    ),
    FAQ(
        "¿Existe algún orden para resolver los ejercicios?",
        "Los retos están organizados siguiendo una ruta de estudio que hará un repaso por todos los fundamentos comunes de la gran mayoría de lenguajes de programación usados en la actualidad. Te recomiendo seguir su numeración."
    ),
    FAQ(
        "¿Y si ya tengo conocimientos?",
        "La ruta de estudio no sólo trata de dar a conocer los fundamentos del lenguaje, si no generar una forma organizada de estudiar, practicar y mejorar tus conocimientos. Estoy seguro de que, de esta manera, aprenderás algo nuevo."
    ),
    FAQ(
        "¿Y si mi corrección no se parece a la solución?",
        "Ante todo, estos ejercicios sirven para poner a prueba tus habilidades, y la solución sólo es una posible opción. La tuya puede ser diferente, o incluso poseer errores, pero lo importante es que a programar se aprende programando."
    )
]


@rx.page(
    route=ROUTE.value,
    title=utils.title_roadmap,
    description=utils.description_roadmap,
    image=utils.preview_roadmap,
    meta=utils.meta_roadmap
)
def roadmap() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(ROUTE),
        rx.center(
            rx.vstack(
                header(
                    "roadmap",
                    "Ruta de estudio con ejercicios para aprender cualquier lenguaje",
                    constants.GITHUB_ROADMAP_REPO_URL
                ),
                # featured_challenge(
                #     f"{ROUTE.value}#last",
                #     last_roadmap_challenge
                # ),
                rx.vstack(
                    paragraph(
                        "Una guía que te ayuda a mejorar.",
                        "Sigue la ruta de estudio para aprender los fundamentos del lenguaje de programación que quieras desde su base, de manera práctica, paso a paso y en comunidad.",
                        "Cada ejercicio se explica en detenimiento para ayudarte a mejorar tu lógica de programación mientras estudias las características más importantes del lenguaje."
                    ),
                    button(
                        "Preguntas frecuentes",
                        f"{ROUTE.value}#faq",
                        "/icons/light/arrow.svg",
                        True,
                        False
                    ),
                    spacing=Spacing.BIG.value,
                    style=styles.max_width_style
                ),
                rx.box(
                    heading("Roadmap"),
                    style=styles.max_width_style
                ),
                stats(roadmap_stats),
                challenge_list(roadmap_challenges),
                faq(FAQ_LIST),
                more(ROUTE),
                languages(ROUTE),
                footer(),
                spacing=Spacing.VERY_BIG.value,
                align="center",
                width="100%"
            )
        )
    )

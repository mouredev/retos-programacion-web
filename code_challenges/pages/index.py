import reflex as rx
import code_challenges.utils as utils
from code_challenges.routes import Route
from code_challenges.styles.styles import Size
from code_challenges.views.navbar import navbar
from code_challenges.views.header import header
from code_challenges.views.challenges import challenges
from code_challenges.views.featured_challenge import featured_challenge
from code_challenges.views.faq import faq, FAQ
from code_challenges.views.languages import languages
from code_challenges.views.footer import footer
from code_challenges.data.Challenge import last_roadmap_challenge

ROUTE = Route.INDEX

FAQ_LIST = [
    FAQ(
        "¿Qué conocimientos necesito para participar?",
        "Los ejercicios semanales se resuelven en pocas líneas de código por lo que el conocimiento mínimo para abordarlos será menor que en las aplicaciones mensuales, ya que estas últimas cubren funcionalidades reales completas. "
        "¿Crees que no estás preparado? No te preocupes. Intenta llevar a cabo los ejercicios. Se trata de aprender y mejorar poco a poco, no de hacerlos perfectos o completos a la primera."
    ),
    FAQ(
        "Acabo de llegar. ¿Debo realizar los retos anteriores?",
        "Cada ejercicio semanal y mensual es independiente del anterior. Cuanto más ejercicios resuelvas, mejor. "
        "Dispondrás de correcciones y propuestas de resolución de todos los retos pasados, pudiendo realizar el seguimiento en comunidad de los últimos publicados mediante la transmisión en directo en Twitch."
    ),
    FAQ(
        "¿Cómo funcionan las transmisiones en directo?",
        "Cada ejercicio posee una fecha de publicación y corrección. El día indicado (habitualmente a las 20:00 hora España) realizaré una transmisión en directo desde Twitch para corregir y comentar el reto. "
        "Puedes consultar transmisiones pasadas de hasta 60 días en la sección vídeos de Twitch. No olvides que todas las correcciones están disponibles en el repositorio de GitHub correspondiente."
    ),
    FAQ(
        "¿Puedo usar cualquier lenguaje de programación?",
        "Por supuesto. Los ejercicios están pensados para que puedan ser resueltos con la mayoría de lenguajes de programación actuales. "
        "Para participar, en la sección de cada tipo de reto encontrarás todas las instrucciones y preguntas frecuentes, así como el enlace al repositorio de GitHub con enunciados y resoluciones de cada reto."
    )
]

# class State(rx.State):
#     pass


@rx.page(
    title=utils.title_index,
    description=utils.description_index,
    image=utils.preview_index,
    meta=utils.meta_index
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        # navbar(ROUTE),
        rx.center(
            rx.vstack(
                header(),
                # challenges(),
                # featured_challenge(
                #     f"{Route.ROADMAP.value}#last",
                #     last_roadmap_challenge
                # ),
                # faq(FAQ_LIST),
                languages(ROUTE),
                footer(),
                spacing=Size.VERY_BIG.value,
                width="100%"
            )
        )
    )

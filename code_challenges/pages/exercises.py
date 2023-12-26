import reflex as rx
import code_challenges.utils as utils
import code_challenges.styles.styles as styles
import code_challenges.constants as constants
from code_challenges.routes import Route
from code_challenges.styles.styles import Size
from code_challenges.views.navbar import navbar
from code_challenges.views.header import header
from code_challenges.components.paragraph import paragraph
from code_challenges.components.button import button
from code_challenges.views.challenge_list import challenge_list
from code_challenges.views.faq import faq, FAQ
from code_challenges.views.more import more
from code_challenges.views.languages import languages
from code_challenges.views.footer import footer
from code_challenges.data.Challenge import exercises_challenges

ROUTE = Route.EXERCISES

FAQ_LIST = [
    FAQ(
        "¿Cómo puedo participar en los retos?",
        "A parte de poder consultar la corrección de los retos, también puedes enviar tus propias soluciones al repositorio. Consulta las instrucciones de participación en cada uno de los repositorios de GitHub correspondientes."
    ),
    FAQ(
        "¿Puedo utilizar cualquier lenguaje de programación?",
        "Por supuesto. Lo bueno de los retos de lógica es que su principal valor es enseñarnos a pensar y seguir un razonamiento a la hora de resolver un problema. La manera de enfocarlo es independiente al lenguaje de programación."
    ),
    FAQ(
        "¿Se van a añadir más ejercicios al listado?",
        "Por el momento, este listado se corresponde con los ejercicios lógicos resueltos en 2022 y 2023. Para consultar los retos lógicos de 2024 debes de visitar la sección llamada \"roadmap de retos\", ya que son ligeramente diferentes."
    ),
    FAQ(
        "¿Qué diferencia hay entre los retos de 2022 y 2023?",
        "La principal diferencia es la manera de aportar tu propia corrección (consulta las instrucciones del repositorio). También ha variado el lenguaje con el que se aporta la corrección principal, pero no es algo relevante en lógica."
    ),
    FAQ(
        "¿Existe algún orden para resolver los ejercicios?",
        "Cada reto es independiente del resto y posee una etiqueta con su dificultad estimada (Fácil, Medio o Difícil). De esta manera podrás identificar los retos que mejor se adapten a tus habilidades y subir de nivel gradualmente."
    ),
    FAQ(
        "¿Y si mi corrección no se parece a la solución?",
        "Ante todo, estos ejercicios sirven para poner a prueba tus habilidades, y la solución sólo es una posible opción. La tuya puede ser diferente, o incluso poseer errores, pero lo importante es que a programar se aprende programando."
    )
]


@rx.page(
    route=ROUTE.value,
    title=utils.title_exercises,
    description=utils.description_exercises,
    image=utils.preview_exercises,
    meta=utils.meta_exercises
)
def exercises() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(ROUTE),
        rx.center(
            rx.vstack(
                header(
                    "ejercicios",
                    "101 ejercicios para practicar lógica de programacion",
                    constants.GITHUB_EXERCISES_REPO_URL
                ),
                rx.vstack(
                    paragraph(
                        "Mejora tus habilidades.",
                        "Utiliza el lenguaje de programación que tú quieras para resolver ejercicios que te ayudarán a mejorar tu forma de pensar y enfrentarte a retos de código.",
                        "Consulta correcciones de la comunidad en los repositorios de código de los diferentes retos. Se han dividido entre los resueltos en 2022 y 2023 (consulta su etiqueta)."
                    ),
                    button(
                        "Preguntas frecuentes",
                        f"{ROUTE.value}#faq",
                        "/icons/light/arrow.svg",
                        True,
                        False
                    ),
                    spacing=Size.BIG.value,
                    style=styles.max_width_style
                ),
                challenge_list(exercises_challenges),
                faq(FAQ_LIST),
                more(ROUTE),
                languages(ROUTE),
                footer(),
                spacing=Size.VERY_BIG.value,
                width="100%"
            )
        )
    )

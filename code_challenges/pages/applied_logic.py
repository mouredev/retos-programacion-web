import reflex as rx
from code_challenges.components.button import button
import code_challenges.styles.styles as styles
import code_challenges.utils as utils
import code_challenges.constants as constants
from code_challenges.routes import Route
from code_challenges.styles.styles import Spacing
from code_challenges.views.faq import FAQ, faq
from code_challenges.views.featured_challenge import featured_challenge
from code_challenges.views.navbar import navbar
from code_challenges.views.header import header
from code_challenges.components.paragraph import paragraph
from code_challenges.views.challenge_list import challenge_list
from code_challenges.views.more import more
from code_challenges.views.languages import languages
from code_challenges.views.footer import footer
from code_challenges.data.Challenge import applied_logic_challenges, last_applied_logic_challenge

ROUTE = Route.APPLIED_LOGIC

FAQ_LIST = [
    FAQ(
        "¿Cómo puedo participar en los proyectos?",
        "A parte de poder consultar la corrección de los ejercicios en código y vídeo, también puedes enviar tus propias soluciones. Consulta las instrucciones de participación en su repositorio de GitHub y pregunta a la comunidad en Discord."
    ),
    FAQ(
        "¿Puedo utilizar cualquier lenguaje de programación?",
        "Sí, en la gran mayoría de los casos. Lo bueno de los proyectos de lógica aplicada es que su principal valor es enseñarnos a pensar y seguir un razonamiento a la hora de implementar una funcionalidad concreta. La manera de enfocarlo es independiente del lenguaje de programación."
    ),
    FAQ(
        "¿Existe algún orden para resolver los retos?",
        "Los proyectos son independientes. Cada uno de ellos hará referencia a diferentes funcionalidades que nos encontramos de manera habitual en aplicaciones reales."
    ),
    FAQ(
        "¿Cuándo se publican los proyectos?",
        "No existe una frecuencia fija, aunque idealmente intentaré que sea me manera semanal o quincenal (consulta el día y la hora en esta web). Se realizará una transmisión en directo resolviendo y explicando el ejercicio. Hecho esto, se publicará la corrección. Todo quedará grabado."
    ),
    FAQ(
        "¿Y si ya tengo conocimientos?",
        "Cada persona puede abordar los proyectos según su nivel de conocimientos, ya que, dependiendo de estos podrás practicar tu lógica de manera diferente. Estoy seguro de que siempre se puede aprender algo nuevo."
    ),
    FAQ(
        "¿Y si mi corrección no se parece a la solución?",
        "Ante todo, estos proyectos sirven para poner a prueba tus habilidades, y la solución sólo es una posible opción. La tuya puede ser diferente, o incluso poseer errores, pero lo importante es que a programar se aprende programando."
    )
]


@rx.page(
    route=ROUTE.value,
    title=utils.title_applied_logic,
    description=utils.description_applied_logic,
    image=utils.preview_applied_logic,
    meta=utils.meta_applied_logic
)
def applied_logic() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(ROUTE),
        rx.center(
            rx.vstack(
                header(
                    "lógica aplicada",
                    "Practica lógica con proyectos y funcionalidades reales",
                    constants.GITHUB_APPLIED_LOGIC_REPO_URL
                ),
                featured_challenge(
                    f"{ROUTE.value}#last",
                    last_applied_logic_challenge
                ),
                rx.vstack(
                    paragraph(
                        "Mejora tu lógica con proyectos reales.",
                        "Este es un listado de proyectos reales que pueden ayudarte a mejorar tu lógica y descubrir cómo implementar diferentes funcionalidades comunes en aplicaciones de nuestro día a día.",
                        "Con el apoyo de la comunidad. Aporta tus propias soluciones a los proyectos sin importar el lenguaje o la tecnología aplicada. Un recurso libre donde todo el mundo pueda aprender."
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
                challenge_list(applied_logic_challenges, True),
                faq(FAQ_LIST),
                more(ROUTE),
                languages(ROUTE),
                footer(),
                spacing=Spacing.VERY_BIG.value,
                align="center",
                width="100%"
            )
        ),
    )

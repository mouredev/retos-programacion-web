import reflex as rx
import code_challenges.utils as utils
from code_challenges.routes import Route
from .button import button


def share(route: Route) -> rx.Component:
    return button(
        "Compartir en",
        _share_text(route),
        "/icons/light/x.svg",
        True
    )


def _share_text(route: Route) -> str:
    text = "https://x.com/intent/tweet?text="
    if route == Route.ROADMAP:
        text += utils.description_roadmap
    elif route == Route.EXERCISES:
        text += utils.description_exercises
    elif route == Route.PROJECTS:
        text += utils.description_projects
    else:
        text += utils.description_index

    return f"{text.replace(' ', '%20')}%0A%0ADescubre&url=retosdeprogramacion.com{route.value}&via=mouredev"

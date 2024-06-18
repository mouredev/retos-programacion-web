import reflex as rx
import code_challenges.constants as constants
import code_challenges.styles.styles as styles
from code_challenges.pages.index import index
from code_challenges.pages.roadmap import roadmap
from code_challenges.pages.roadmap_ranking import roadmap_ranking
from code_challenges.pages.mini import mini
from code_challenges.pages.exercises import exercises
from code_challenges.pages.projects import projects

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(
            src=f"https://www.googletagmanager.com/gtag/js?id={constants.GOOGLE_ANALYTICS_TAG}"
        ),
        rx.script(
            f"""
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', '{constants.GOOGLE_ANALYTICS_TAG}');
"""
        ),
    ],
)

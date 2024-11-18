import reflex as rx
import reflex_chakra as rc
from enum import Enum
from .colors import Color, TextColor
from .fonts import Font, FontWeight


class CustomAttrs(Enum):
    DATA_TEXT = "datatext"


MAX_WIDTH = "1200px"
FLEX_DIRECTION = ["column", "column", "row", "row"]


class Size(Enum):
    ZERO = "0px !important"
    VERY_SMALL = "0.3em"
    SMALL = "0.5em"
    MEDIUM = "0.75em"
    DEFAULT = "1em"
    DEFAULT_MEDIUM = "1.125em"
    DEFAULT_BIG = "1.5em"
    BIG = "2em"
    MEDIUM_BIG = "3em"
    VERY_BIG = "4em"


class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "2"
    DEFAULT = "4"  # 1em
    DEFAULT_BIG = "5"
    BIG = "6"
    MEDIUM_BIG = "8"
    VERY_BIG = "9"


STYLESHEETS = [
    "/css/main.css",
    "/fonts/fonts.css",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.NORMAL.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value,
    rx.link: {
        "color": TextColor.PRIMARY.value,
        "text_decoration": "none",
        "_hover": {}
    },
    rx.button: {
        "font_weight": FontWeight.BOLD.value,
        "font_size": "1.25rem",
        "padding": "1.8rem 2rem",
        "border_radius": "0.5rem",
        "_hover": {
            "background": f"{TextColor.BLUE.value}",
            "box-shadow": f"0 0 {Size.DEFAULT.value} {Color.SECONDARY.value}"
        }
    },
    rx.badge: {
        "font_weight": FontWeight.BOLD.value,
        "border_radius": Size.BIG.value,
        "background": "transparent"
    },
    rc.heading: {
        "font_family": Font.NEON.value,
        "font_weight": FontWeight.BOLD.value,
        "width": "100%"
    },
}

max_width_style = dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH
)

background_pattern_style = {
    "background": "url('/mosaic.png') repeat",
    "background-size": "120px 120px",
}

background_gradient_style = {
    "background": f"linear-gradient(to bottom, rgb(0, 0, 0, 0) 20%, {Color.PRIMARY.value} 100%)"
}

glow_text_style = {
    "position": "relative",
    "cursor": "pointer",
    "_after": {
        "content": f"attr({CustomAttrs.DATA_TEXT.value})",
        "position": "absolute",
        "left": "0",
        "width": "100%",
        "height": "100%",
        "opacity": "60%",
        "filter": "blur(6px)",
        "backface-visibility": "hidden",
        "-webkit-backface-visibility": "hidden",
        "-moz-backface-visibility": "hidden",
        "transform": "translateZ(0)",
        "-webkit-transform": "translateZ(0)",
        "-moz-transform": "translateZ(0)"
    },
    "_hover": {
        "_after": {
            "opacity": "100%"
        }
    }
}

container_style = {
    "padding": Size.MEDIUM_BIG.value,
    "border_radius": "1.5rem",
    "background": Color.SECONDARY.value,
    "_hover": {
        "box-shadow": f"0 0 {Size.DEFAULT.value} {Color.SECONDARY.value}"
    }
}

featured_container_style = {
    "padding": Size.MEDIUM_BIG.value,
    "border_radius": "1.5rem",
    "background": Color.SECONDARY.value,
    "box-shadow": f"0 0 {Size.DEFAULT.value} {TextColor.PURPLE.value}"
}

button_style = {
    "color": TextColor.TERTIARY.value,
    "background": f"{Color.TERTIARY.value}"
}

button_secondary_style = {
    "color": TextColor.PRIMARY.value,
    "background": f"{Color.PRIMARY.value}",
    "border": f"2px solid {TextColor.SECONDARY.value}"
}

roadmap_path_style = {
    "position": "absolute",
    "height": "8em",
    "bottom": "-7em",
    "left": Size.BIG.value,
    "user-select": "none !important",
    "-webkit-user-select": "none",
    "-moz-user-select": "none",
    "-ms-user-select": "none",
    "z_index": "1"
}

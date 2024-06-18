import reflex as rx
from code_challenges.routes import Route
from code_challenges.styles.styles import Size, Spacing, Color
from code_challenges.styles.fonts import Font
from code_challenges.styles.colors import TextColor
from code_challenges.components.title import title
from code_challenges.components.badge import badge

FONT_SIZE = [Size.DEFAULT_MEDIUM.value, Size.DEFAULT_BIG.value]


def navbar(route: Route) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.link(
                rx.hstack(
                    title(
                        "{",
                        Font.ARGON,
                        color=TextColor.BLUE,
                        size=FONT_SIZE
                    ),
                    title(
                        "Retos",
                        Font.NEON,
                        size=FONT_SIZE
                    ),
                    title(
                        "de",
                        Font.RADON,
                        size=FONT_SIZE
                    ),
                    title(
                        "Programación",
                        Font.NEON,
                        size=FONT_SIZE
                    ),
                    title(
                        "}",
                        Font.ARGON,
                        color=TextColor.BLUE,
                        size=FONT_SIZE
                    )
                ),
                href=Route.INDEX.value
            ),
            rx.spacer(),
            rx.tablet_and_desktop(
                rx.hstack(
                    rx.spacer(),
                    _menu_roadmap(route),
                    _menu_mini(route),
                    _menu_exercises(route),
                    _menu_projects(route),
                    spacing=Spacing.BIG.value
                ),
                width="100%"
            ),
            rx.mobile_only(
                rx.menu.root(
                    rx.menu.trigger(
                        rx.image(
                            src="/icons/menu.svg",
                            height="auto",
                            width=Size.DEFAULT_BIG.value,
                            alt="Icono del menú de navegación"
                        ),
                        display="flex"
                    ),
                    rx.menu.content(
                        rx.menu.item(
                            _menu_roadmap(route),
                            background="transparent"
                        ),
                        rx.menu.item(
                            _menu_mini(route),
                            background="transparent"
                        ),
                        rx.menu.item(
                            _menu_exercises(route),
                            background="transparent"
                        ),
                        rx.menu.item(
                            _menu_projects(route),
                            background="transparent"
                        ),
                        background=Color.SECONDARY.value,
                        border_color=Color.PRIMARY.value,
                        minWidth="100px"
                    ),
                )
            ),
            width="100%",
            align="center"
        ),
        bg=Color.SECONDARY.value,
        position="sticky",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%"
    )


def _menu_roadmap(route: Route) -> rx.Component:
    return rx.link(
        rx.hstack(
            title(
                "Roadmap",
                size=[Size.DEFAULT_MEDIUM.value],
                color=TextColor.PURPLE if route == Route.ROADMAP else TextColor.PRIMARY
            ),
            badge(
                "2024",
                TextColor.PURPLE if route == Route.ROADMAP else TextColor.PINK,
                True
            ),
            spacing=Spacing.SMALL.value
        ),
        href=Route.ROADMAP.value
    )


def _menu_mini(route: Route) -> rx.Component:
    return rx.link(
        title(
            "Mini",
            size=[Size.DEFAULT_MEDIUM.value],
            color=TextColor.BLUE if route == Route.MINI else TextColor.PRIMARY
        ),
        href=Route.MINI.value
    )


def _menu_exercises(route: Route) -> rx.Component:
    return rx.link(
        title(
            "Ejercicios",
            size=[Size.DEFAULT_MEDIUM.value],
            color=TextColor.GREEN if route == Route.EXERCISES else TextColor.PRIMARY
        ),
        href=Route.EXERCISES.value
    )


def _menu_projects(route: Route) -> rx.Component:
    return rx.link(
        title(
            "Proyectos",
            size=[Size.DEFAULT_MEDIUM.value],
            color=TextColor.YELLOW if route == Route.PROJECTS else TextColor.PRIMARY
        ),
        href=Route.PROJECTS.value
    )

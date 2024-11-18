import reflex as rx
import reflex_chakra as rc
import code_challenges.styles.styles as styles
from code_challenges.styles.styles import Size, Spacing, Color, TextColor, Font, FontWeight
from code_challenges.data.Challenge import Challenge
from .heading import heading
from .badge import badge
from .button import button


def challenge(data: Challenge, id: str, roadmap: bool, last: bool) -> rx.Component:
    return rx.box(
        rc.accordion_item(
            rc.accordion_button(
                rx.vstack(
                    rx.cond(
                        data.level != 0 or data.date != "",
                        rx.hstack(
                            rx.cond(
                                data.level != 0,
                                badge(
                                    _level(data.level)[0],
                                    _level(data.level)[1]
                                )
                            ),
                            rx.cond(
                                data.date != "",
                                badge(
                                    data.date,
                                    TextColor.SECONDARY
                                )
                            ),
                            rx.spacer(),
                            rc.accordion_icon(),
                            spacing=Spacing.DEFAULT.value,
                            width="100%"
                        ),
                        rx.hstack(
                            rx.spacer(),
                            rc.accordion_icon(),
                            spacing=Spacing.DEFAULT.value,
                            width="100%"
                        )
                    ),
                    rx.hstack(
                        heading(
                            data.title.split(" ", 1)[0],
                            TextColor.BLUE,
                            "lg",
                            True
                        ),
                        heading(
                            data.title.split(" ", 1)[1],
                            size="lg",
                            auto=True
                        ),
                        spacing=Spacing.SMALL.value,
                        align_items="start",
                        text_align="start",
                        width="100%"
                    ),
                    width="100%"
                )
            ),
            rc.accordion_panel(
                rx.box(
                    rx.code_block(
                        data.code,
                        theme=rx.code_block.themes.a11y_dark,
                        border_radius="1.5rem",
                        custom_style={
                            "background-color": Color.PRIMARY.value,
                            "padding": Size.DEFAULT_BIG.value
                        },
                        code_tag_props={
                            "style": {
                                "fontFamily": Font.ARGON.value,
                                "fontWeight": FontWeight.NORMAL.value,
                                "color": TextColor.PRIMARY.value
                            }
                        }
                    ),
                    width="100%"
                ),
                rx.cond(
                    data.solution != "",
                    rx.flex(
                        button(
                            "Ejercicio",
                            data.url,
                            "/icons/dark/github.svg"
                        ),
                        button(
                            "Solución",
                            data.solution,
                            "/icons/dark/github.svg"
                        ),
                        rx.hstack(
                            rx.cond(
                                data.video != "",
                                rx.box(
                                    rx.tablet_and_desktop(
                                        button(
                                            data.video_title if data.video_title != "" else "Vídeo",
                                            data.video,
                                            "/icons/light/youtube.svg",
                                            True
                                        )
                                    ),
                                    rx.mobile_only(
                                        button(
                                            "",
                                            data.video,
                                            "/icons/light/youtube.svg",
                                            True
                                        )
                                    )
                                )
                            ),
                            rx.cond(
                                data.community != "",
                                rx.box(
                                    rx.tablet_and_desktop(
                                        button(
                                            "Comunidad",
                                            data.community,
                                            "/icons/light/github.svg",
                                            True
                                        )
                                    ),
                                    rx.mobile_only(
                                        button(
                                            "",
                                            data.community,
                                            "/icons/light/github.svg",
                                            True
                                        )
                                    )
                                )
                            ),
                            spacing=Spacing.DEFAULT_BIG.value
                        ),
                        spacing=Spacing.DEFAULT_BIG.value,
                        flex_direction=styles.FLEX_DIRECTION,
                        margin_top=Size.DEFAULT_BIG.value
                    ),
                    rx.flex(
                        rx.cond(
                            data.url != "",
                            button(
                                "Ejercicio" if roadmap else "Ejercicio y soluciones",
                                data.url,
                                "/icons/dark/github.svg"
                            )
                        ),
                        rx.cond(
                            roadmap and data.event != "",
                            button(
                                "Horario",
                                data.event,
                                "/icons/light/discord.svg",
                                True
                            )
                        ),
                        rx.cond(
                            data.video != "",
                            button(
                                data.video_title if data.video_title != "" else "Vídeo",
                                data.video,
                                "/icons/light/youtube.svg",
                                True
                            )
                        ),
                        spacing=Spacing.DEFAULT_BIG.value,
                        flex_direction=styles.FLEX_DIRECTION,
                        margin_top=Size.DEFAULT_BIG.value
                    )
                ),
            ),
            border_top_width=Size.ZERO.value,
            border_bottom_width=Size.ZERO.value
        ),
        rx.cond(
            roadmap and not last,
            rx.image(
                src="/path.png",
                style=styles.roadmap_path_style,
                alt="Imagen entre bloques de ejercicios que representa dos cículos unidos por una línea"
            )
        ),
        id=id,
        style=styles.featured_container_style if id == "1" and roadmap else styles.container_style,
        margin_bottom=Size.ZERO.value if last else "6em" if roadmap else Size.BIG.value,
        position="relative",
        width="100%"
    )


def _level(level: int) -> (str, TextColor):
    if level == 1:
        return ("Fácil", TextColor.GREEN)
    elif level == 2:
        return ("Medio", TextColor.BLUE)
    elif level == 3:
        return ("Difícil", TextColor.PINK)
    else:
        return ("", TextColor.SECONDARY)

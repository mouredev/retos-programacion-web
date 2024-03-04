import reflex as rx

# Común


def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


meta = [
    {"name": "og:type", "content": "website"},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@mouredev"}
]

# Index


title_index = "Retos de Programación | by MoureDev"
description_index = "Ejercicios, retos y aplicaciones para mejorar tu lógica de programación con cualquier lenguaje. Gratis, a tu ritmo y en comunidad."
preview_index = "https://retosdeprogramacion.com/preview.jpg"

meta_index = [
    {"name": "og:title", "content": title_index},
    {"name": "og:description", "content": description_index},
    {"name": "og:image", "content": preview_index}
]
meta_index.extend(meta)

# Roadmap

title_roadmap = "Roadmap de Retos de Programación | by MoureDev"
description_roadmap = "Ruta de estudio con ejercicios para mejorar tu lógica de programación y aprender cualquier lenguaje. Gratis, a tu ritmo y en comunidad."
preview_roadmap = "https://retosdeprogramacion.com/preview_roadmap.jpg"

meta_roadmap = [
    {"name": "og:title", "content": title_roadmap},
    {"name": "og:description", "content": description_roadmap},
    {"name": "og:image", "content": preview_roadmap}
]
meta_roadmap.extend(meta)

# Roadmap Ranking

title_roadmap_ranking = "Ranking Roadmap de Retos de Programación | by MoureDev"
description_roadmap_ranking = "Ranking de la ruta de estudio con ejercicios para mejorar tu lógica de programación y aprender cualquier lenguaje. Gratis, a tu ritmo y en comunidad."

meta_roadmap_ranking = [
    {"name": "og:title", "content": title_roadmap_ranking},
    {"name": "og:description", "content": description_roadmap_ranking},
    {"name": "og:image", "content": preview_roadmap}
]
meta_roadmap_ranking.extend(meta)

# Ejercicios

title_exercises = "Ejercicios de Programación | by MoureDev"
description_exercises = "101 ejercicios para practicar tu lógica de programación con cualquier lenguaje. Gratis, a tu ritmo y en comunidad."
preview_exercises = "https://retosdeprogramacion.com/preview_exercises.jpg"

meta_exercises = [
    {"name": "og:title", "content": title_exercises},
    {"name": "og:description", "content": description_exercises},
    {"name": "og:image", "content": preview_exercises}
]
meta_exercises.extend(meta)

# Proyectos

title_projects = "Proyectos de Programación | by MoureDev"
description_projects = "12 aplicaciones pensadas para añadir a tu portafolio personal . Gratis, a tu ritmo y en comunidad."
preview_projects = "https://retosdeprogramacion.com/preview_projects.jpg"

meta_projects = [
    {"name": "og:title", "content": title_projects},
    {"name": "og:description", "content": description_projects},
    {"name": "og:image", "content": preview_projects}
]
meta_projects.extend(meta)

# Devicon

DEVICON = {
    "c#": "csharp", "c++": "cplusplus", "sql": "azuresqldatabase", "cobol": "devicon",
    "mojo": "devicon", "pascal": "devicon", "vb.net": "visualbasic", "ada": "devicon",
    "racket": "devicon", "tcl": "devicon"
}


def devicon(name: str) -> str:
    return f"devicon-{DEVICON.get(name.lower(), name.lower())}-plain"

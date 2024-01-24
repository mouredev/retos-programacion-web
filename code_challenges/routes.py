from enum import Enum


class Route(Enum):
    INDEX = "/"
    ROADMAP = "/roadmap"
    ROADMAP_RANKING = "/roadmap/ranking"
    EXERCISES = "/ejercicios"
    PROJECTS = "/proyectos"

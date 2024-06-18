from enum import Enum


class Route(Enum):
    INDEX = "/"
    ROADMAP = "/roadmap"
    ROADMAP_RANKING = "/roadmap/ranking"
    MINI = "/mini"
    EXERCISES = "/ejercicios"
    PROJECTS = "/proyectos"

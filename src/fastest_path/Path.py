from typing import List

from fastest_path.Graph import Graph
from fastest_path.Vertex import Vertex


class Path(object):
    __graph: Graph
    __stack: List[Vertex]

    def __init__(self, graph: Graph) -> None:
        self.__graph = graph
        self.__stack = []

    def add_to_beginning_of_path(self, vertex: Vertex):
        self.__stack.append(vertex)

    def fastest_path_for_printing(self) -> str:
        first_arrow: str = '--('
        second_arrow: str = ')-->'
        fastest_path: str = ''
        current: Vertex

        while len(self.__stack) > 1:
            current = self.__stack.pop()
            fastest_path += current.name
            fastest_path += first_arrow
            fastest_path += self.get_cost_from_current_vertex_to_next(current)
            fastest_path += second_arrow
        fastest_path += self.__stack.pop().name
        return fastest_path

    def get_cost_from_current_vertex_to_next(self, current: Vertex) -> str:
        return str(self.__graph.graph.get(current).get(self.__stack[-1]))

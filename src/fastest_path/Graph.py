from typing import Dict, List

from fastest_path.Vertex import Vertex


class Graph(object):
    __graph: Dict[Vertex, Dict[Vertex, int]]

    def __init__(self, graph: Dict[Vertex, Dict[Vertex, int]]) -> None:
        self.__graph = graph

    @property
    def graph(self) -> Dict[Vertex, Dict[Vertex, int]]:
        return self.__graph

    @graph.setter
    def graph(self, val: Dict[Vertex, Dict[Vertex, int]]) -> None:
        self.__graph = val

    def get_all_vertices(self) -> List[Vertex]:
        list_vertices: List[Vertex] = list(self.__graph.keys())
        return list_vertices

    def get_connections_and_costs_of_vertex(self, vertex: Vertex) -> Dict[Vertex, int]:
        return self.graph.get(vertex)

    @classmethod
    def init_graph(cls, connections: List[str], vertex_position: int, connected_vertex_position: int,
                   cost_position: slice) -> Dict[Vertex, Dict[Vertex, int]]:
        graph: Dict[Vertex, Dict[Vertex, int]] = {}
        for connection in connections:
            try:
                graph[Vertex(str(connection[vertex_position]))][
                    Vertex(str(connection[connected_vertex_position]))] = int(connection[cost_position])
            except KeyError:
                graph[Vertex(str(connection[vertex_position]))] = {
                    Vertex(str(connection[connected_vertex_position])): int(connection[cost_position])}

        return graph

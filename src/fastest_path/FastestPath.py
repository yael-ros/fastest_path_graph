import sys
from typing import Dict, List
from fastest_path.CostAndPrev import CostAndPrev
from fastest_path.FileReader import FileReader
from fastest_path.Graph import Graph
from fastest_path.Path import Path
from fastest_path.Vertex import Vertex

# fastest path between two vertices in a graph is determined by dijkstra algorithm.
# all vertices in the graph are connected to each other. the connections are not
# the same in their costs.


class FastestPath(object):
    """
    A class which represent the fastest path between two vertices in a graph.

    Methods
    -------
    get_fastest_path():
        Returns the fastest path between two vertices in a graph.
    """

    __file_name: str
    __graph: Graph
    __source: Vertex
    __destination: Vertex

    def __init__(self, file_name: str) -> None:
        self.__file_name = file_name

    def get_fastest_path(self) -> str:
        """
        Returns the fastest path between two vertices in a graph.

        Returns
        -------
        A string which represent the fastest path from the source vertex to the
        destination vertex, including the costs between each two vertices
        """

        file_reader: FileReader = FileReader(self.__file_name)
        self.__graph = file_reader.init_graph_from_file()
        self.__source = file_reader.get_vertex("source")
        self.__destination = file_reader.get_vertex("destination")
        costs: Dict[Vertex, CostAndPrev] = self.__create_table_of_costs()
        fastest_path: Path = self.__build_path(costs)

        return fastest_path.fastest_path_for_printing()

    def __build_path(self, costs: Dict[Vertex, CostAndPrev]) -> Path:
        new_path: Path = Path(self.__graph)
        current: Vertex = self.__destination

        while current is not self.__source:
            new_path.add_to_beginning_of_path(current)
            current = costs.get(current).prev_vertex
        new_path.add_to_beginning_of_path(current)
        return new_path

    def __create_table_of_costs(self) -> Dict[Vertex, CostAndPrev]:
        costs: Dict[Vertex, CostAndPrev] = self.__init_table_of_costs()
        unvisited_list: List[Vertex] = self.graph.get_all_vertices()
        current_visited_vertex: Vertex = self.__source
        all_connections_and_costs_of_vertex: Dict[Vertex, int]

        while unvisited_list:
            all_connections_and_costs_of_vertex = \
                self.graph.get_connections_and_costs_of_vertex(current_visited_vertex)

            for current_vertex, cost_of_connection in all_connections_and_costs_of_vertex.items():
                # from source to current vertex
                old_cost: int = costs.get(current_vertex).cost
                # from source to current visited + from current visited to current vertex
                new_cost: int = cost_of_connection + costs.get(current_visited_vertex).cost
                if old_cost > new_cost:
                    costs[current_vertex] = CostAndPrev(new_cost, current_visited_vertex)

            unvisited_list.remove(current_visited_vertex)
            current_visited_vertex = self.__get_next_vertex_by_minimum_cost(costs, unvisited_list)

        return costs

    @classmethod
    def __get_next_vertex_by_minimum_cost(cls, costs: Dict[Vertex, CostAndPrev], unvisited_list: List[Vertex]):
        min_cost: int = sys.maxsize
        result: Vertex = Vertex(None)
        for vertex in unvisited_list:
            current_cost: int = costs.get(vertex).cost
            if current_cost < min_cost:
                result = vertex
                min_cost = current_cost
        return result

    def __init_table_of_costs(self) -> Dict[Vertex, CostAndPrev]:
        all_vertices: List[Vertex] = self.__graph.get_all_vertices()
        costs: Dict[Vertex, CostAndPrev] = {vertex: CostAndPrev(sys.maxsize, None) for vertex in all_vertices}
        costs.update({self.__source: CostAndPrev(0, None)})

        return costs

    @property
    def graph(self) -> Graph:
        return self.__graph

    @graph.setter
    def graph(self, val: Graph) -> None:
        self.__graph = val

    @property
    def source(self) -> Vertex:
        return self.__source

    @source.setter
    def source(self, val: Vertex) -> None:
        self.__source = val

    @property
    def destination(self) -> Vertex:
        return self.__destination

    @destination.setter
    def destination(self, val: Vertex) -> None:
        self.__destination = val


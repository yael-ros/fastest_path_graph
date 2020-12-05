from fastest_path.Vertex import Vertex


class CostAndPrev(object):

    def __init__(self, new_cost: int, prev: Vertex = None) -> None:
        self.__cost: int = new_cost
        self.__prev_vertex: Vertex = prev

    @property
    def prev_vertex(self) -> Vertex:
        return self.__prev_vertex

    @prev_vertex.setter
    def prev_vertex(self, vertex: Vertex) -> None:
        self.__prev_vertex = vertex

    @property
    def cost(self) -> int:
        return self.__cost

    @cost.setter
    def cost(self, new_cost: int) -> None:
        self.__cost = new_cost

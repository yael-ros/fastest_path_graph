class Vertex(object):
    vertex_name: str

    def __init__(self, name: str) -> None:
        if name is not None:
            self.vertex_name = name

    @property
    def name(self) -> str:
        return self.vertex_name

    @name.setter
    def name(self, value):
        self.vertex_name = value

    def __hash__(self) -> int:
        return hash(self.vertex_name)

    def __eq__(self, o) -> bool:
        return self.__class__ == o.__class__ and self.vertex_name == o.vertex_name


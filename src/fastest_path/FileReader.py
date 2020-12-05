from pathlib import Path
from typing import List
from fastest_path.Graph import Graph
from fastest_path.Vertex import Vertex


class FileReader(object):
    __file_content: List[str]
    __file_path: str

    def __init__(self, file_name: str) -> None:
        project_path: Path = Path(__file__).parent.parent.parent
        self.__file_path = str(project_path) + '/resources/' + file_name
        self.__file_path = self.__file_path.replace("\\", "/")
        self.__file_content = self.__load_file_content()

    def init_graph_from_file(self) -> Graph:
        connections: List[str] = self.__file_content[3:]
        # remove spaces
        connections = [''.join(connection.split()) for connection in connections]

        return Graph(Graph.init_graph(connections, 0, 3, slice(5, None)))

    def __load_file_content(self) -> List[str]:
        with open(self.__file_path) as file:
            content: List[str] = file.readlines()
        # remove empty lines from the list
        content = [x.strip() for x in content]
        return content

    def get_vertex(self, name: str) -> Vertex:
        source_and_destination: List[str] = self.__file_content[:3]
        source_and_destination = [''.join(x.split()) for x in source_and_destination]
        if name == "source":
            return Vertex(source_and_destination[0][-1])
        return Vertex(source_and_destination[1][-1])

from typing import Union


class Edge:
    def __init__(self, from_node: int, to_node:int, weight:float):
        self.from_node: int = from_node
        self.to_node: int = to_node
        self.weight: float = weight
class Node:
    def __init__(self, index: int, label=None):
        self.index: int = index
        self.edges: dict = {}
        self.label: str = label
    def num_edges(self) -> int:
        return len(self.edges)
    def get_edge(self, neighbor: int) -> Union[Edge, None]:
        if neighbor in self.edges:
            return self.edges[neighbor]
        return None
    def add_edge(self, neighbor: int, weight: float):
        self.edges[neighbor] = Edge(self.index, neighbor,weight)
    def remove_edge(self, neighbor: int):
        if neighbor in self.edges:
        del self.edges(neighbor)
    def get_edge_list(self) -> list:
        return list(self.edges.values())
    def get_sorted_edge_list(self) -> list:
        result = []
        neighbors = (list)(self.edges.keys())
        neighbors.sort()
        for n in neighbors:
            result.append(self.edges[n])
        return result

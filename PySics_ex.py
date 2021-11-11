
from PySics import Graph, SicsAlgorithams

if __name__ == "__main__":

    m = Graph("adjacency_list", "undirected_tag", 3)
    m.set_vertex_label(0, "red")
    m.set_vertex_label(1, "blue")
    m.set_vertex_label(2, "green")
    m.add_edge(0, 1)
    m.add_edge(1, 2)
    m.add_edge(2, 0)

    n = Graph("adjacency_list", "undirected_tag", 4)
    n.set_vertex_label(0, "red")
    n.set_vertex_label(1, "blue")
    n.set_vertex_label(2, "green")
    n.set_vertex_label(3, "green")
    n.add_edge(0, 1)
    n.add_edge(1, 2)
    n.add_edge(2, 0)
    n.add_edge(1, 3)
    n.add_edge(3, 0)

    c = SicsAlgorithams("adjacency_list", "undirected_tag")
    c.backtracking_parent_ind(m, n, "GCF")
#import PySicsModule as psics
from PySicsModule import adjacency_listmat_undirected_tag_alg as alg, adjacency_degreesortedlistmat_undirected_tag_alg as alg_ds, adjacency_listmat_undirected_tag as graph, adjacency_degreesortedlistmat_undirected_tag as graph_ds

if __name__ == "__main__":
    
    m = graph(3)
    m.set_vertex_label(0, "red")
    m.set_vertex_label(1, "blue")
    m.set_vertex_label(2, "green")
    m.add_edge(0, 1)
    m.add_edge(1, 2)
    m.add_edge(2, 0)

    n = graph(4)
    n.set_vertex_label(0, "red")
    n.set_vertex_label(1, "blue")
    n.set_vertex_label(2, "green")
    n.set_vertex_label(3, "green")
    n.add_edge(0, 1)
    n.add_edge(1, 2)
    n.add_edge(2, 0)
    n.add_edge(1, 3)
    n.add_edge(3, 0)

    m_ds = graph_ds(m)

    n_ds = graph_ds(n)

    c = alg()
    c.backtracking_parent_ind(m, n, "GCF")

    ds = alg_ds()
    #ds.lazyforwardchecking_parent_ind(m_ds, n_ds, "GCF")
    #ds.backtracking_parent_adjacentconsistency_ind(m_ds, n_ds, "GCF")
    
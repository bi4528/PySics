
from PySics import Graph, SicsAlgorithams, read_amalfi, read_py_ldgraphs_lab, read_ldgraphs_lab

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

    #m = read_py_ldgraphs_lab("adjacency_list", "undirected_tag", "F:\\MyFolder\\MIVIA\\eta2.tar\\eta2 2\\lab8_nonuni_eta2\\target\\si2_rnd_eta02_m300.B30.grf")
    #n = read_ldgraphs_lab("adjacency_list", "undirected_tag", "F:\\MyFolder\\MIVIA\\eta2.tar\\eta2 2\\lab8_nonuni_eta2\\target\\si2_rnd_eta02_m300.B30.grf")
    #n = m

    #m = read_py_ldgraphs_lab("adjacency_list", "undirected_tag", "C:\\Users\\Bojan Ilic\\Documents\\DIPLOMSKA\\test\\m_graph.txt")
    #n = read_ldgraphs_lab("adjacency_list", "undirected_tag", "C:\\Users\\Bojan Ilic\\Documents\\DIPLOMSKA\\test\\n_graph.txt")

    c = SicsAlgorithams("adjacency_list", "undirected_tag")
    
    c.backjumping_bitset_degreeprune_ind(m, n, "GCF", mapping=True)
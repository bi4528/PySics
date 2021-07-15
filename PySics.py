import PySicsModule as psics
#from PySicsModule import adjacency_list_bidirectional_tag_alg as alg, adjacency_list_bidirectional_tag as graph

if __name__ == "__main__":
    
    g = psics.adjacency_list_undirected_tag(3)
    g.set_vertex_label(0, "red")
    g.set_vertex_label(1, "blue")
    g.set_vertex_label(2, "green")
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    

    h = psics.adjacency_list_undirected_tag(4)
    h.set_vertex_label(0, "red")
    h.set_vertex_label(1, "blue")
    h.set_vertex_label(2, "green")
    h.set_vertex_label(3, "green")
    h.add_edge(0, 1)
    h.add_edge(1, 2)
    h.add_edge(2, 0)
    h.add_edge(1, 3)
    h.add_edge(3, 0)

    
    c = psics.adjacency_list_undirected_tag_alg()

    print("Algorithm lazyforwardcheckingbackjumping_low_bitset_degreeprune_ind for adjacency_list_undirected_tag:", end='\n') 
    c.lazyforwardcheckingbackjumping_low_bitset_degreeprune_ind(g, h, "GCF")

    print("Algorithm backtracking_ind for adjacency_list_undirected_tag:", end='\n') 
    c.backtracking_ind(g, h, "DEG")

    m = psics.adjacency_list_bidirectional_tag(3)
    m.set_vertex_label(0, "red")
    m.set_vertex_label(1, "blue")
    m.set_vertex_label(2, "green")
    m.add_edge(0, 1)
    m.add_edge(1, 2)
    m.add_edge(2, 0)
    

    n = psics.adjacency_list_bidirectional_tag(4)
    n.set_vertex_label(0, "red")
    n.set_vertex_label(1, "blue")
    n.set_vertex_label(2, "green")
    n.set_vertex_label(3, "green")
    n.add_edge(0, 1)
    n.add_edge(1, 2)
    n.add_edge(2, 0)
    n.add_edge(1, 3)
    n.add_edge(3, 0)

    c1 = psics.adjacency_list_bidirectional_tag_alg()

    print("Algorithm lazyforwardcheckingbackjumping_low_bitset_degreeprune_ind for adjacency_list_bidirectional_tag:", end='\n') 
    c1.lazyforwardcheckingbackjumping_low_bitset_degreeprune_ind(m, n, "RDEG")

    print("Algorithm backtracking_ind for adjacency_list_bidirectional_tag:", end='\n') 
    c1.backtracking_ind(m, n, "DEG")
    
    

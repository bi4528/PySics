import PySicsModule as psics

if __name__ == "__main__":
    
    g = psics.graph_type(3)
    g.set_vertex_label(0, "red")
    g.set_vertex_label(1, "blue")
    g.set_vertex_label(2, "green")
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    

    h = psics.graph_type(4)
    h.set_vertex_label(0, "red")
    h.set_vertex_label(1, "blue")
    h.set_vertex_label(2, "green")
    h.set_vertex_label(3, "green")
    h.add_edge(0, 1)
    h.add_edge(1, 2)
    h.add_edge(2, 0)
    h.add_edge(1, 3)
    h.add_edge(3, 0)

    print("Algoritem lazyforwardcheckingbackjumping_low_bitset_degreeprune_ind:", end='\n') 
    psics.lazyforwardcheckingbackjumping_low_bitset_degreeprune_ind(g, h)
    
    print("", end='\n') 

    print("Algoritem backtracking_ind:", end='\n') 
    psics.backtracking_ind(g, h)
    

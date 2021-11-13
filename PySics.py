
from PySicsModule import (
    adjacency_list_undirected_tag,
    adjacency_list_undirected_tag_alg, 
    adjacency_list_bidirectional_tag,
    adjacency_list_bidirectional_tag_alg, 
    adjacency_listmat_undirected_tag,
    adjacency_listmat_undirected_tag_alg, 
    adjacency_listmat_bidirectional_tag,
    adjacency_listmat_bidirectional_tag_alg,
    adjacency_degreesortedlistmat_undirected_tag,
    adjacency_degreesortedlistmat_undirected_tag_alg,
    adjacency_degreesortedlistmat_bidirectional_tag,
    adjacency_degreesortedlistmat_bidirectional_tag_alg,
)

__all__ = ['Graph', 'SicsAlgorithams']

class Graph:

    def __init__(self, data_structure, graph_type, num_vertices):
        
        valid_data_structures = {"adjacency_list", "adjacency_listmat", "adjacency_degreesortedlistmat"}
        valid_graph_types = {"undirected_tag", "bidirectional_tag"}

        if data_structure not in valid_data_structures:
             raise ValueError('_init_() argument \'data_structure\' must be one of %r.' % valid_data_structures)

        if graph_type not in valid_graph_types:
             raise ValueError("_init_() argument \'graph_type must\' be one of %r." % valid_graph_types)

        if not isinstance(num_vertices, int):
             raise ValueError("_init_() argument \'num_verticies\' must be type int.")

        if (data_structure == "adjacency_list" and  graph_type == "undirected_tag"):
            self.graph_type = adjacency_list_undirected_tag
        elif (data_structure == "adjacency_list" and  graph_type == "bidirectional_tag"):
           self.graph_type = adjacency_list_bidirectional_tag
        elif (data_structure == "adjacency_listmat" and  graph_type == "undirected_tag"):
           self.graph_type = adjacency_listmat_undirected_tag
        elif (data_structure == "adjacency_listmat" and  graph_type == "bidirectional_tag"):
           self.graph_type = adjacency_listmat_bidirectional_tag
        elif (data_structure == "adjacency_degreesortedlistmat" and  graph_type == "undirected_tag"):
           self.graph_type = adjacency_degreesortedlistmat_undirected_tag
        elif (data_structure == "adjacency_degreesortedlistmat" and  graph_type == "bidirectional_tag"):
           self.graph_type = adjacency_degreesortedlistmat_bidirectional_tag

        self.graph = self.graph_type(num_vertices)

    def set_vertex_label(self, vertex, label):

        self.graph.set_vertex_label(vertex, label)

    def add_edge(self, vertex1, vertex2):

        self.graph.add_edge(vertex1, vertex2)

class SicsAlgorithams:

    def __init__(self, data_structure, graph_type):
        
        self.data_structure_str = data_structure
        self.graph_type_str = graph_type

        valid_data_structures = {"adjacency_list", "adjacency_listmat", "adjacency_degreesortedlistmat"}
        valid_graph_types = {"undirected_tag", "bidirectional_tag"}

        if data_structure not in valid_data_structures:
             raise ValueError('_init_: data structure must be one of %r.' % valid_data_structures)

        if graph_type not in valid_graph_types:
             raise ValueError("_init_: graph type must be one of %r." % valid_graph_types)

        if (data_structure == "adjacency_list" and  graph_type == "undirected_tag"):
            self.graph_type_alg = adjacency_list_undirected_tag_alg
        elif (data_structure == "adjacency_list" and  graph_type == "bidirectional_tag"):
           self.graph_type_alg = adjacency_list_bidirectional_tag_alg
        elif (data_structure == "adjacency_listmat" and  graph_type == "undirected_tag"):
           self.graph_type_alg = adjacency_listmat_undirected_tag_alg
        elif (data_structure == "adjacency_listmat" and  graph_type == "bidirectional_tag"):
           self.graph_type_alg = adjacency_listmat_bidirectional_tag_alg
        elif (data_structure == "adjacency_degreesortedlistmat" and  graph_type == "undirected_tag"):
           self.graph_type_alg = adjacency_degreesortedlistmat_undirected_tag_alg
        elif (data_structure == "adjacency_degreesortedlistmat" and  graph_type == "bidirectional_tag"):
           self.graph_type_alg = adjacency_degreesortedlistmat_bidirectional_tag_alg

        self.alg = self.graph_type_alg()

    def backjumping_bitset_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backjumping_bitset_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backjumping_bitset_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backjumping_bitset_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backjumping_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backjumping_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backjumping_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backjumping_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backjumping_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backjumping_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_adjacentconsistency_forwardcount_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_adjacentconsistency_forwardcount_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_adjacentconsistency_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_adjacentconsistency_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_adjacentconsistency_precount_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_adjacentconsistency_precount_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_bitset_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_bitset_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_bitset_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_bitset_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_degreeprune_adjacentconsistency_forwardcount_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_degreeprune_adjacentconsistency_forwardcount_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_degreeprune_adjacentconsistency_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_degreeprune_adjacentconsistency_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_degreeprune_adjacentconsistency_precount_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_degreeprune_adjacentconsistency_precount_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_forwardcount_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_forwardcount_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_parent_adjacentconsistency_forwardcount_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_parent_adjacentconsistency_forwardcount_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_parent_adjacentconsistency_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_parent_adjacentconsistency_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_parent_adjacentconsistency_precount_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_parent_adjacentconsistency_precount_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_parent_degreeprune_adjacentconsistency_forwardcount_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_parent_degreeprune_adjacentconsistency_forwardcount_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_parent_degreeprune_adjacentconsistency_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_parent_degreeprune_adjacentconsistency_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_parent_degreeprune_adjacentconsistency_precount_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_parent_degreeprune_adjacentconsistency_precount_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_parent_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_parent_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_parent_forwardcount_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_parent_forwardcount_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_parent_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.backtracking_parent_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def conflictbackjumping_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.conflictbackjumping_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def conflictbackjumping_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.conflictbackjumping_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def conflictbackjumping_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.conflictbackjumping_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def forwardchecking_bitset_degreeprune_ac1_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.forwardchecking_bitset_degreeprune_ac1_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def forwardchecking_bitset_degreeprune_countingalldifferent_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.forwardchecking_bitset_degreeprune_countingalldifferent_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def forwardchecking_bitset_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.forwardchecking_bitset_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def forwardchecking_bitset_degreesequenceprune_ac1_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.forwardchecking_bitset_degreesequenceprune_ac1_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def forwardchecking_bitset_degreesequenceprune_countingalldifferent_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.forwardchecking_bitset_degreesequenceprune_countingalldifferent_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def forwardchecking_bitset_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.forwardchecking_bitset_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def forwardchecking_bitset_mrv_degreeprune_ac1_ind(self, graph1, graph2, vertex_order=None, mapping=False):

        if vertex_order is not None:
            raise AttributeError("forwardchecking_bitset_mrv_degreeprune_ac1_ind() vertex_order is not supported for this algoritham. MRV algorithams already use dynamic search strategy Minimum Remaining Values.")

        self.alg.forwardchecking_bitset_mrv_degreeprune_ac1_ind(graph1.graph, graph2.graph, mapping)

    def forwardchecking_bitset_mrv_degreeprune_countingalldifferent_ind(self, graph1, graph2, vertex_order=None, mapping=False):

        if vertex_order is not None:
            raise AttributeError("forwardchecking_bitset_mrv_degreeprune_countingalldifferent_ind() vertex_order is not supported for this algoritham. MRV algorithams already use dynamic search strategy Minimum Remaining Values.")

        self.alg.forwardchecking_bitset_mrv_degreeprune_countingalldifferent_ind(graph1.graph, graph2.graph, mapping)

    def forwardchecking_bitset_mrv_degreeprune_ind(self, graph1, graph2, vertex_order=None, mapping=False):

        if vertex_order is not None:
            raise AttributeError("forwardchecking_bitset_mrv_degreeprune_countingalldifferent_ind() vertex_order is not supported for this algoritham. MRV algorithams already use dynamic search strategy Minimum Remaining Values.")

        self.alg.forwardchecking_bitset_mrv_degreeprune_ind(graph1.graph, graph2.graph, mapping)

    def forwardchecking_bitset_mrv_degreesequenceprune_ac1_ind(self, graph1, graph2, vertex_order=None, mapping=False):

        if vertex_order is not None:
            raise AttributeError("forwardchecking_bitset_mrv_degreesequenceprune_ac1_ind() vertex_order is not supported for this algoritham. MRV algorithams already use dynamic search strategy Minimum Remaining Values.")

        self.alg.forwardchecking_bitset_mrv_degreesequenceprune_ac1_ind(graph1.graph, graph2.graph, mapping)

    def forwardchecking_bitset_mrv_degreesequenceprune_countingalldifferent_ind(self, graph1, graph2, vertex_order=None, mapping=False):
        
        if vertex_order is not None:
            raise AttributeError("forwardchecking_bitset_mrv_degreesequenceprune_countingalldifferent_ind() vertex_order is not supported for this algoritham. MRV algorithams already use dynamic search strategy Minimum Remaining Values.")

        self.alg.forwardchecking_bitset_mrv_degreesequenceprune_countingalldifferent_ind(graph1.graph, graph2.graph, mapping)

    def forwardchecking_bitset_mrv_degreesequenceprune_ind(self, graph1, graph2, vertex_order=None, mapping=False):

        if vertex_order is not None:
            raise AttributeError("forwardchecking_bitset_mrv_degreesequenceprune_ind() vertex_order is not supported for this algoritham. MRV algorithams already use dynamic search strategy Minimum Remaining Values.")

        self.alg.forwardchecking_bitset_mrv_degreesequenceprune_ind(graph1.graph, graph2.graph, mapping)

    def forwardchecking_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.forwardchecking_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def forwardchecking_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.forwardchecking_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def forwardchecking_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.forwardchecking_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def forwardchecking_mrv_degreeprune_ind(self, graph1, graph2, vertex_order=None, mapping=False):
        
        if vertex_order is not None:
            raise AttributeError("forwardchecking_mrv_degreeprune_ind() vertex_order is not supported for this algoritham. MRV algorithams already use dynamic search strategy Minimum Remaining Values.")

        self.alg.forwardchecking_mrv_degreeprune_ind(graph1.graph, graph2.graph, mapping)

    def lazyforwardchecking_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.lazyforwardchecking_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.lazyforwardchecking_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.lazyforwardchecking_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_low_bitset_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.lazyforwardchecking_low_bitset_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_low_bitset_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.lazyforwardchecking_low_bitset_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_low_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.lazyforwardchecking_low_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_low_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.lazyforwardchecking_low_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_low_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.lazyforwardchecking_low_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_low_parent_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.lazyforwardchecking_low_parent_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_low_parent_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.lazyforwardchecking_low_parent_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_parent_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.lazyforwardchecking_parent_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_parent_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.lazyforwardchecking_parent_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_parent_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.lazyforwardchecking_parent_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardcheckingbackjumping_low_bitset_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.lazyforwardcheckingbackjumping_low_bitset_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardcheckingbackjumping_low_bitset_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):

        self.alg.lazyforwardcheckingbackjumping_low_bitset_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)




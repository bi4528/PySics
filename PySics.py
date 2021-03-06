"""Python module which provides two classes for user-friendly use of pysicsmodule 
developed for use of algorithams for solving the Subgraph Isomorphism Constraint Satisfaction problem.

The pysics module relies on objects and functions developed in  pysicsmodule.

The Graph class stores different graph types in different data structures
and allows only strings as vertex labels.

The SicsAlgorithams class contains algorithams for solving the Subgraph Isomorphism Constraint Satisfaction problem
which can be executed on two objects of class Graph

Read_* functions read data from files provided in databases such as AMALFI, MIVIA LDGraphs...
They allow reading only from file path.
"""
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
    read_amalfi_adjacency_list_bidirectional_tag,
    read_amalfi_adjacency_list_undirected_tag,
    read_amalfi_adjacencymat_list_bidirectional_tag,
    read_amalfi_adjacencymat_list_undirected_tag,
    read_amalfi_adjacency_degreesortedlistmat_bidirectional_tag,
    read_amalfi_adjacency_degreesortedlistmat_undirected_tag,
    read_gal_adjacency_list_bidirectional_tag,
    read_gal_adjacency_list_undirected_tag,
    read_gal_adjacencymat_list_bidirectional_tag,
    read_gal_adjacencymat_list_undirected_tag,
    read_gal_adjacency_degreesortedlistmat_bidirectional_tag,
    read_gal_adjacency_degreesortedlistmat_undirected_tag,
    read_galv_adjacency_list_bidirectional_tag,
    read_galv_adjacency_list_undirected_tag,
    read_galv_adjacencymat_list_bidirectional_tag,
    read_galv_adjacencymat_list_undirected_tag,
    read_galv_adjacency_degreesortedlistmat_bidirectional_tag,
    read_galv_adjacency_degreesortedlistmat_undirected_tag,
    read_gf_adjacency_list_bidirectional_tag,
    read_gf_adjacency_list_undirected_tag,
    read_gf_adjacencymat_list_bidirectional_tag,
    read_gf_adjacencymat_list_undirected_tag,
    read_gf_adjacency_degreesortedlistmat_bidirectional_tag,
    read_gf_adjacency_degreesortedlistmat_undirected_tag,
    read_ldgraphs_unl_adjacency_list_bidirectional_tag,
    read_ldgraphs_unl_adjacency_list_undirected_tag,
    read_ldgraphs_unl_adjacencymat_list_bidirectional_tag,
    read_ldgraphs_unl_adjacencymat_list_undirected_tag,
    read_ldgraphs_unl_adjacency_degreesortedlistmat_bidirectional_tag,
    read_ldgraphs_unl_adjacency_degreesortedlistmat_undirected_tag,
    read_ldgraphs_lab_adjacency_list_bidirectional_tag,
    read_ldgraphs_lab_adjacency_list_undirected_tag,
    read_ldgraphs_lab_adjacencymat_list_bidirectional_tag,
    read_ldgraphs_lab_adjacencymat_list_undirected_tag,
    read_ldgraphs_lab_adjacency_degreesortedlistmat_bidirectional_tag,
    read_ldgraphs_lab_adjacency_degreesortedlistmat_undirected_tag
)

__all__ = ['Graph', 'SicsAlgorithams']

class Graph:
    """
    Base class for undirected and biderctional graphs.
    
    Directed graphs are not available in this release.

    A Graph stores vertecies and edges of different graph types 
    in different data structures and allows only strings as vertex labels.

    A vertex is an object which has its serial number (which is determined when
    graph is inizialized) and optional vertex label which has to be string.
    
    An edge is an object which is a link between two verticies.  
    Edge labels are not available in this release.

    A graph_type represents a property of the graph. Currently available:
        - undirected_tag
        - bidirectional_tag

    A data_structure represents a data structure we store data about verticies and edges in. Currently available:
        - adjacency_list
        - adjacency_listmat (includes adjacency matrix)
        - adjacency_degreesortedlistmat (includes adjacency matrix and vertices are sorted according to degree)

    Parameters
    ----------
    data_structure : string. Currently available:
        - adjacency_list
        - adjacency_listmat (includes adjacency matrix)
        - adjacency_degreesortedlistmat (includes adjacency matrix and vertices are sorted according to degree)

    graph_type : string. Currently available:
        - undirected_tag
        - bidirectional_tag

    num_vertices : integer, optional (default: None)
        When number of verticies is not defined or set to 0, it creates empty graph 
        on which you are not able to set lables, add edges or execute algorithams.
        An example of such use are degreesorted graphs or the use of read_* functions.

    Examples
    ----------

    """
    def __init__(self, data_structure, graph_type, num_vertices=None, graph=None):

        self.data_structure = data_structure
        self.graph = None

        valid_data_structures = {"adjacency_list", "adjacency_listmat", "adjacency_degreesortedlistmat"}
        valid_graph_types = {"undirected_tag", "bidirectional_tag"}

        if data_structure not in valid_data_structures:
             raise ValueError('_init_() argument \'data_structure\' must be one of %r.' % valid_data_structures)

        if graph_type not in valid_graph_types:
             raise ValueError("_init_() argument \'graph_type must\' be one of %r." % valid_graph_types)

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
        
        if (data_structure == "adjacency_degreesortedlistmat"):
            if not num_vertices is None:
                    raise TypeError("data structure %s doesn't support inizialization by number of verticies." % data_structure)
            elif isinstance(graph, Graph):
                self.graph = self.graph_type(graph.graph)
            else:
                raise TypeError("graph must be of type Graph.");
        else:
            if not graph is None:
                    raise TypeError("data structure %s doesn't support inizialization by another graph." % data_structure)
            elif isinstance(num_vertices, int):
                self.graph = self.graph_type(num_vertices)
            elif not num_vertices is None:
                raise TypeError("num_vertices must be of type int.")

    def set_vertex_label(self, vertex, label):

        if not self.graph is None:
            self.graph.set_vertex_label(vertex, label)
        else:
            raise TypeError("cannot set a vertex label of an empty graph.")

    def add_edge(self, vertex1, vertex2):

        if not self.graph is None:
            self.graph.add_edge(vertex1, vertex2)
        else:
            raise TypeError("cannot add an edge to an empty graph.")

    def read_amalfi(self, myfile_name):

        if (self.graph_type == adjacency_list_undirected_tag):
            self.graph = read_amalfi_adjacency_list_undirected_tag(myfile_name)
        elif (self.graph_type == adjacency_list_bidirectional_tag):
            self.graph = read_amalfi_adjacency_list_bidirectional_tag(myfile_name)
        elif (self.graph_type == adjacency_listmat_undirected_tag):
            self.graph = read_amalfi_adjacency_listmat_undirected_tag(myfile_name)
        elif (self.graph_type == adjacency_listmat_bidirectional_tag):
            self.graph = read_amalfi_adjacency_listmat_bidirectional_tag(myfile_name)
        elif (self.graph_type == adjacency_degreesortedlistmat_undirected_tag):
            self.graph = read_amalfi_adjacency_degreesortedlistmat_undirected_tag(myfile_name)
        elif (self.graph_type == adjacency_degreesortedlistmat_bidirectional_tag):
            self.graph = read_amalfi_adjacency_degreesortedlistmat_bidirectional_tag(myfile_name)

    def read_gal(self, myfile_name):

        if (self.graph_type == adjacency_list_undirected_tag):
            self.graph = read_gal_adjacency_list_undirected_tag(myfile_name)
        elif (self.graph_type == adjacency_list_bidirectional_tag):
            self.graph = read_gal_adjacency_list_bidirectional_tag(myfile_name)
        elif (self.graph_type == adjacency_listmat_undirected_tag):
            self.graph = read_gal_adjacency_listmat_undirected_tag(myfile_name)
        elif (self.graph_type == adjacency_listmat_bidirectional_tag):
            self.graph = read_gal_adjacency_listmat_bidirectional_tag(myfile_name)
        elif (self.graph_type == adjacency_degreesortedlistmat_undirected_tag):
            self.graph = read_gal_adjacency_degreesortedlistmat_undirected_tag(myfile_name)
        elif (self.graph_type == adjacency_degreesortedlistmat_bidirectional_tag):
            self.graph = read_gal_adjacency_degreesortedlistmat_bidirectional_tag(myfile_name)

    def read_galv(self, myfile_name):

        if (self.graph_type == adjacency_list_undirected_tag):
            self.graph = read_galv_adjacency_list_undirected_tag(myfile_name)
        elif (self.graph_type == adjacency_list_bidirectional_tag):
            self.graph = read_galv_adjacency_list_bidirectional_tag(myfile_name)
        elif (self.graph_type == adjacency_listmat_undirected_tag):
            self.graph = read_galv_adjacency_listmat_undirected_tag(myfile_name)
        elif (self.graph_type == adjacency_listmat_bidirectional_tag):
            self.graph = read_galv_adjacency_listmat_bidirectional_tag(myfile_name)
        elif (self.graph_type == adjacency_degreesortedlistmat_undirected_tag):
            self.graph = read_galv_adjacency_degreesortedlistmat_undirected_tag(myfile_name)
        elif (self.graph_type == adjacency_degreesortedlistmat_bidirectional_tag):
            self.graph = read_galv_adjacency_degreesortedlistmat_bidirectional_tag(myfile_name)

    def read_gf(self, myfile_name):

        if (self.graph_type == adjacency_list_undirected_tag):
            self.graph = read_gf_adjacency_list_undirected_tag(myfile_name)
        elif (self.graph_type == adjacency_list_bidirectional_tag):
            self.graph = read_gf_adjacency_list_bidirectional_tag(myfile_name)
        elif (self.graph_type == adjacency_listmat_undirected_tag):
            self.graph = read_gf_adjacency_listmat_undirected_tag(myfile_name)
        elif (self.graph_type == adjacency_listmat_bidirectional_tag):
            self.graph = read_gf_adjacency_listmat_bidirectional_tag(myfile_name)
        elif (self.graph_type == adjacency_degreesortedlistmat_undirected_tag):
            self.graph = read_gf_adjacency_degreesortedlistmat_undirected_tag(myfile_name)
        elif (self.graph_type == adjacency_degreesortedlistmat_bidirectional_tag):
            self.graph = read_gf_adjacency_degreesortedlistmat_bidirectional_tag(myfile_name)

    def read_ldgraphs_unl(self, myfile_name):

        if (self.graph_type == adjacency_list_undirected_tag):
            self.graph = read_ldgraphs_unl_adjacency_list_undirected_tag(myfile_name)
        elif (self.graph_type == adjacency_list_bidirectional_tag):
            self.graph = read_ldgraphs_unl_adjacency_list_bidirectional_tag(myfile_name)
        elif (self.graph_type == adjacency_listmat_undirected_tag):
            self.graph = read_ldgraphs_unl_adjacency_listmat_undirected_tag(myfile_name)
        elif (self.graph_type == adjacency_listmat_bidirectional_tag):
            self.graph = read_ldgraphs_unl_adjacency_listmat_bidirectional_tag(myfile_name)
        elif (self.graph_type == adjacency_degreesortedlistmat_undirected_tag):
            self.graph = read_ldgraphs_unl_adjacency_degreesortedlistmat_undirected_tag(myfile_name)
        elif (self.graph_type == adjacency_degreesortedlistmat_bidirectional_tag):
            self.graph = read_ldgraphs_unl_adjacency_degreesortedlistmat_bidirectional_tag(myfile_name)

    def read_ldgraphs_lab(self, myfile_name):

        if (self.graph_type == adjacency_list_undirected_tag):
            self.graph = read_ldgraphs_lab_adjacency_list_undirected_tag(myfile_name)
        elif (self.graph_type == adjacency_list_bidirectional_tag):
            self.graph = read_ldgraphs_lab_adjacency_list_bidirectional_tag(myfile_name)
        elif (self.graph_type == adjacency_listmat_undirected_tag):
            self.graph = read_ldgraphs_lab_adjacency_listmat_undirected_tag(myfile_name)
        elif (self.graph_type == adjacency_listmat_bidirectional_tag):
            self.graph = read_ldgraphs_lab_adjacency_listmat_bidirectional_tag(myfile_name)
        elif (self.graph_type == adjacency_degreesortedlistmat_undirected_tag):
            self.graph = read_ldgraphs_lab_adjacency_degreesortedlistmat_undirected_tag(myfile_name)
        elif (self.graph_type == adjacency_degreesortedlistmat_bidirectional_tag):
            self.graph = read_ldgraphs_lab_adjacency_degreesortedlistmat_bidirectional_tag(myfile_name)

def read_amalfi(data_structure, graph_type, myfile_name):

    g = Graph(data_structure, graph_type)
    g.read_amalfi(myfile_name)

    return g

def read_gal(data_structure, graph_type, myfile_name):

    g = Graph(data_structure, graph_type)
    g.read_gal(myfile_name)

    return g

def read_galv(data_structure, graph_type, myfile_name):

    g = Graph(data_structure, graph_type)
    g.read_galv(myfile_name)

    return g

def read_gf(data_structure, graph_type, myfile_name):

    g = Graph(data_structure, graph_type)
    g.read_gf(myfile_name)

    return g

def read_ldgraphs_unl(data_structure, graph_type, myfile_name):

    g = Graph(data_structure, graph_type)
    g.read_ldgraphs_unl(myfile_name)

    return g

def read_ldgraphs_lab(data_structure, graph_type, myfile_name):

    g = Graph(data_structure, graph_type)
    g.read_ldgraphs_lab(myfile_name)

    return g

def read_py_ldgraphs_unl(data_structure, graph_type, myfile_name):

    g = Graph(data_structure, graph_type)
    g.read_ldgraphs_unl(myfile_name)

    return g

def read_py_ldgraphs_lab(data_structure, graph_type, myfile_name):

    file = open(myfile_name)

    n = int(file.readline())

    g = Graph(data_structure, graph_type, n)

    for i in range(n):
        
        line = file.readline()
        if (line[-1] == '\n'):
            line = line[:-1]

        vertex = int(line.split(' ')[0])
        label = line.split(' ')[1]

        g.set_vertex_label(vertex, label)

    for i in range(n):

        a = int(file.readline())
        
        for i in range(a):

            line = file.readline()
            if (line[-1] == '\n'):
                line = line[:-1]

            vertex1 = int(line.split(' ')[0])
            vertex2 = int(line.split(' ')[1])

            g.add_edge(vertex1, vertex2)
 
    file.close()

    return g

class SicsAlgorithams:
    """
    Base class for algorithams for solving the Subgraph Isomorphism Constraint Satisfaction problem

    Parameters
    ----------
    data_structure : string. Currently available:
        - adjacency_list
        - adjacency_listmat (includes adjacency matrix)
        - adjacency_degreesortedlistmat (includes adjacency matrix and vertices are sorted according to degree)

    graph_type : string. Currently available:
        - undirected_tag
        - bidirectional_tag

    Examples
    ----------

    """
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
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")
        
        self.alg.backjumping_bitset_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backjumping_bitset_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backjumping_bitset_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backjumping_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backjumping_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backjumping_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backjumping_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backjumping_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backjumping_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_adjacentconsistency_forwardcount_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_adjacentconsistency_forwardcount_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_adjacentconsistency_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_adjacentconsistency_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_adjacentconsistency_precount_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_adjacentconsistency_precount_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_bitset_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_bitset_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_bitset_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_bitset_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_degreeprune_adjacentconsistency_forwardcount_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_degreeprune_adjacentconsistency_forwardcount_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_degreeprune_adjacentconsistency_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_degreeprune_adjacentconsistency_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_degreeprune_adjacentconsistency_precount_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_degreeprune_adjacentconsistency_precount_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_forwardcount_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_forwardcount_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_parent_adjacentconsistency_forwardcount_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_parent_adjacentconsistency_forwardcount_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_parent_adjacentconsistency_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_parent_adjacentconsistency_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_parent_adjacentconsistency_precount_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_parent_adjacentconsistency_precount_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_parent_degreeprune_adjacentconsistency_forwardcount_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_parent_degreeprune_adjacentconsistency_forwardcount_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_parent_degreeprune_adjacentconsistency_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_parent_degreeprune_adjacentconsistency_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_parent_degreeprune_adjacentconsistency_precount_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_parent_degreeprune_adjacentconsistency_precount_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_parent_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_parent_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_parent_forwardcount_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_parent_forwardcount_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def backtracking_parent_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.backtracking_parent_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def conflictbackjumping_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.conflictbackjumping_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def conflictbackjumping_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.conflictbackjumping_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def conflictbackjumping_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.conflictbackjumping_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def forwardchecking_bitset_degreeprune_ac1_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.forwardchecking_bitset_degreeprune_ac1_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def forwardchecking_bitset_degreeprune_countingalldifferent_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.forwardchecking_bitset_degreeprune_countingalldifferent_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def forwardchecking_bitset_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.forwardchecking_bitset_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def forwardchecking_bitset_degreesequenceprune_ac1_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.forwardchecking_bitset_degreesequenceprune_ac1_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def forwardchecking_bitset_degreesequenceprune_countingalldifferent_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.forwardchecking_bitset_degreesequenceprune_countingalldifferent_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def forwardchecking_bitset_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.forwardchecking_bitset_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def forwardchecking_bitset_mrv_degreeprune_ac1_ind(self, graph1, graph2, vertex_order=None, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        if vertex_order is not None:
            raise AttributeError("forwardchecking_bitset_mrv_degreeprune_ac1_ind() vertex_order is not supported for this algoritham. MRV algorithams already use dynamic search strategy Minimum Remaining Values.")

        self.alg.forwardchecking_bitset_mrv_degreeprune_ac1_ind(graph1.graph, graph2.graph, mapping)

    def forwardchecking_bitset_mrv_degreeprune_countingalldifferent_ind(self, graph1, graph2, vertex_order=None, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        if vertex_order is not None:
            raise AttributeError("forwardchecking_bitset_mrv_degreeprune_countingalldifferent_ind() vertex_order is not supported for this algoritham. MRV algorithams already use dynamic search strategy Minimum Remaining Values.")

        self.alg.forwardchecking_bitset_mrv_degreeprune_countingalldifferent_ind(graph1.graph, graph2.graph, mapping)

    def forwardchecking_bitset_mrv_degreeprune_ind(self, graph1, graph2, vertex_order=None, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        if vertex_order is not None:
            raise AttributeError("forwardchecking_bitset_mrv_degreeprune_countingalldifferent_ind() vertex_order is not supported for this algoritham. MRV algorithams already use dynamic search strategy Minimum Remaining Values.")

        self.alg.forwardchecking_bitset_mrv_degreeprune_ind(graph1.graph, graph2.graph, mapping)

    def forwardchecking_bitset_mrv_degreesequenceprune_ac1_ind(self, graph1, graph2, vertex_order=None, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        if vertex_order is not None:
            raise AttributeError("forwardchecking_bitset_mrv_degreesequenceprune_ac1_ind() vertex_order is not supported for this algoritham. MRV algorithams already use dynamic search strategy Minimum Remaining Values.")

        self.alg.forwardchecking_bitset_mrv_degreesequenceprune_ac1_ind(graph1.graph, graph2.graph, mapping)

    def forwardchecking_bitset_mrv_degreesequenceprune_countingalldifferent_ind(self, graph1, graph2, vertex_order=None, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        if vertex_order is not None:
            raise AttributeError("forwardchecking_bitset_mrv_degreesequenceprune_countingalldifferent_ind() vertex_order is not supported for this algoritham. MRV algorithams already use dynamic search strategy Minimum Remaining Values.")

        self.alg.forwardchecking_bitset_mrv_degreesequenceprune_countingalldifferent_ind(graph1.graph, graph2.graph, mapping)

    def forwardchecking_bitset_mrv_degreesequenceprune_ind(self, graph1, graph2, vertex_order=None, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        if vertex_order is not None:
            raise AttributeError("forwardchecking_bitset_mrv_degreesequenceprune_ind() vertex_order is not supported for this algoritham. MRV algorithams already use dynamic search strategy Minimum Remaining Values.")

        self.alg.forwardchecking_bitset_mrv_degreesequenceprune_ind(graph1.graph, graph2.graph, mapping)

    def forwardchecking_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.forwardchecking_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def forwardchecking_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.forwardchecking_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def forwardchecking_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.forwardchecking_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def forwardchecking_mrv_degreeprune_ind(self, graph1, graph2, vertex_order=None, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        if vertex_order is not None:
            raise AttributeError("forwardchecking_mrv_degreeprune_ind() vertex_order is not supported for this algoritham. MRV algorithams already use dynamic search strategy Minimum Remaining Values.")

        self.alg.forwardchecking_mrv_degreeprune_ind(graph1.graph, graph2.graph, mapping)

    def lazyforwardchecking_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.lazyforwardchecking_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.lazyforwardchecking_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.lazyforwardchecking_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_low_bitset_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.lazyforwardchecking_low_bitset_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_low_bitset_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.lazyforwardchecking_low_bitset_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_low_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.lazyforwardchecking_low_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_low_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.lazyforwardchecking_low_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_low_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.lazyforwardchecking_low_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_low_parent_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.lazyforwardchecking_low_parent_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_low_parent_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.lazyforwardchecking_low_parent_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_parent_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.lazyforwardchecking_parent_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_parent_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.lazyforwardchecking_parent_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardchecking_parent_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.lazyforwardchecking_parent_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardcheckingbackjumping_low_bitset_degreeprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.lazyforwardcheckingbackjumping_low_bitset_degreeprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)

    def lazyforwardcheckingbackjumping_low_bitset_degreesequenceprune_ind(self, graph1, graph2, vertex_order, mapping=False):
        
        if graph1.graph is None:
            raise TypeError("the first graph parameter is an empty graph.")
        if graph2.graph is None:
            raise TypeError("the second graph parameter is an empty graph.")

        self.alg.lazyforwardcheckingbackjumping_low_bitset_degreesequenceprune_ind(graph1.graph, graph2.graph, vertex_order, mapping)




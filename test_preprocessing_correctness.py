from graph import Graph, Vertex, Edge
from preprocessing import count_automorphisms, calc_true_twins, calc_false_twins, check_neighbourhood_TT, check_neighbourhood_FT


def test_calc_TT_and_FT():
    G = Graph(False, 0)
    v1 = Vertex(G)
    v2 = Vertex(G)
    v3 = Vertex(G)
    v4 = Vertex(G)
    e1 = Edge(v1, v2)
    e2 = Edge(v1, v3)
    e3 = Edge(v1, v4)
    e4 = Edge(v2, v3)
    e5 = Edge(v3, v4)
    G.add_edge(e1)
    G.add_edge(e2)
    G.add_edge(e3)
    G.add_edge(e4)
    G.add_edge(e5)
    TT = calc_true_twins(G)
    FT = calc_false_twins(G)
    expected_TT = [[0, 2]]
    expected_FT = [[1, 3]]
    assert expected_TT == TT
    assert expected_FT == FT


def test_twin_false_twin():
    G = Graph(False, 0)
    v1 = Vertex(G)
    v2 = Vertex(G)
    v3 = Vertex(G)
    v4 = Vertex(G)
    e1 = Edge(v1, v2)
    e2 = Edge(v1, v3)
    e3 = Edge(v1, v4)
    e4 = Edge(v2, v3)
    e5 = Edge(v3, v4)
    G.add_edge(e1)
    G.add_edge(e2)
    G.add_edge(e3)
    G.add_edge(e4)
    G.add_edge(e5)
    expected = 4
    num = count_automorphisms(G)
    assert expected == num


def test_single_vertex():
    G = Graph(False, 1)
    expected = 1
    num = count_automorphisms(G)
    assert expected == num


def test_two_no_edges_vertex():
    G = Graph(False, 2)
    expected = 2
    num = count_automorphisms(G)
    assert expected == num


def test_two_with_edge_vertex():
    G = Graph(False, 0)
    v1 = Vertex(G)
    v2 = Vertex(G)
    e1 = Edge(v1, v2)
    G.add_edge(e1)
    expected = 2
    num = count_automorphisms(G)
    assert expected == num


def test_true_triplets_calc_TT():
    G = Graph(False, 0)
    v1 = Vertex(G)
    v2 = Vertex(G)
    v3 = Vertex(G)
    e1 = Edge(v1, v2)
    e2 = Edge(v1, v3)
    e3 = Edge(v2, v3)
    G.add_edge(e1)
    G.add_edge(e2)
    G.add_edge(e3)

    result = calc_true_twins(G)
    expected = [[0, 1, 2]]
    assert expected == result


def test_true_triplets():
    G = Graph(False, 0)
    v1 = Vertex(G)
    v2 = Vertex(G)
    v3 = Vertex(G)
    e1 = Edge(v1, v2)
    e2 = Edge(v1, v3)
    e3 = Edge(v2, v3)
    G.add_edge(e1)
    G.add_edge(e2)
    G.add_edge(e3)

    expected = 6
    num = count_automorphisms(G)
    assert expected == num
from graph import Graph, Vertex, Edge
from colour_ref import colour_refinement


def same_group(colouring: dict[Vertex, int], vertices: list[Vertex]):
    v = vertices[0]
    for u in vertices[1:]:
        if colouring[v] != colouring[u]:
            return False
        v = u
    return True


def test_single_node():
    G = Graph(False, 1)
    result_coloring = colour_refinement(G.vertices, {G.vertices[0]: 0})
    assert result_coloring[G.vertices[0]] == 0


def test_two_nodes_with_edge():
    G = Graph(False, 2)
    e1 = Edge(G.vertices[0], G.vertices[1])
    G.add_edge(e1)
    result_coloring = colour_refinement(G.vertices, {v: 0 for v in G.vertices})
    assert result_coloring[G.vertices[0]] == 0
    assert result_coloring[G.vertices[1]] == 0


def test_two_nodes_no_edge():
    G = Graph(False, 2)
    result_coloring = colour_refinement(G.vertices, {v: 0 for v in G.vertices})
    assert result_coloring[G.vertices[0]] == 0
    assert result_coloring[G.vertices[1]] == 0


def test_three_nodes_no_edges():
    G = Graph(False, 3)
    result_coloring = colour_refinement(G.vertices, {v: 0 for v in G.vertices})
    assert result_coloring[G.vertices[0]] == 0
    assert result_coloring[G.vertices[1]] == 0
    assert result_coloring[G.vertices[2]] == 0


def test_three_nodes_one_edge_01():
    G = Graph(False, 3)
    v0 = G.vertices[0]
    v1 = G.vertices[1]
    v2 = G.vertices[2]
    G.add_vertex(v0)
    G.add_vertex(v1)
    G.add_vertex(v2)
    e0 = Edge(v0, v1)
    G.add_edge(e0)

    result_coloring = colour_refinement(G.vertices, {v: 0 for v in G.vertices})
    assert result_coloring[v0] == result_coloring[v1]
    assert result_coloring[v2] != result_coloring[v1]
    assert result_coloring[v2] != result_coloring[v0]


def test_three_nodes_one_edge_02():
    G = Graph(False, 3)
    v0 = G.vertices[0]
    v1 = G.vertices[1]
    v2 = G.vertices[2]
    G.add_vertex(v0)
    G.add_vertex(v1)
    G.add_vertex(v2)
    e0 = Edge(v0, v2)
    G.add_edge(e0)

    result_coloring = colour_refinement(G.vertices, {v: 0 for v in G.vertices})
    assert result_coloring[v0] == result_coloring[v2]
    assert result_coloring[v1] != result_coloring[v2]
    assert result_coloring[v1] != result_coloring[v0]


def test_three_nodes_one_edge_12():
    G = Graph(False, 3)
    v0 = G.vertices[0]
    v1 = G.vertices[1]
    v2 = G.vertices[2]
    G.add_vertex(v0)
    G.add_vertex(v1)
    G.add_vertex(v2)
    e0 = Edge(v1, v2)
    G.add_edge(e0)

    result_coloring = colour_refinement(G.vertices, {v: 0 for v in G.vertices})
    assert result_coloring[v1] == result_coloring[v2]
    assert result_coloring[v0] != result_coloring[v1]
    assert result_coloring[v0] != result_coloring[v2]


def test_three_nodes_two_edges():
    G = Graph(False, 3)
    v0 = G.vertices[0]
    v1 = G.vertices[1]
    v2 = G.vertices[2]
    G.add_vertex(v0)
    G.add_vertex(v1)
    G.add_vertex(v2)
    e0 = Edge(v0, v1)
    e1 = Edge(v1, v2)
    G.add_edge(e0)
    G.add_edge(e1)

    result_coloring = colour_refinement(G.vertices, {v: 0 for v in G.vertices})
    assert result_coloring[v0] == result_coloring[v2]
    assert result_coloring[v1] != result_coloring[v2]
    assert result_coloring[v1] != result_coloring[v0]


def test_three_nodes_three_edges():
    G = Graph(False, 3)
    v0 = G.vertices[0]
    v1 = G.vertices[1]
    v2 = G.vertices[2]
    G.add_vertex(v0)
    G.add_vertex(v1)
    G.add_vertex(v2)
    e0 = Edge(v0, v1)
    e1 = Edge(v1, v2)
    e2 = Edge(v0, v2)
    G.add_edge(e0)
    G.add_edge(e1)
    G.add_edge(e2)

    result_coloring = colour_refinement(G.vertices, {v: 0 for v in G.vertices})
    assert result_coloring[v0] == result_coloring[v2]
    assert result_coloring[v1] == result_coloring[v2]
    assert same_group(result_coloring, [v0, v1, v2])


def test_four_nodes_snake():
    G = Graph(False, 4)
    v0 = G.vertices[0]
    v1 = G.vertices[1]
    v2 = G.vertices[2]
    v3 = G.vertices[3]
    G.add_vertex(v0)
    G.add_vertex(v1)
    G.add_vertex(v2)
    G.add_vertex(v3)
    e0 = Edge(v0, v1)
    e1 = Edge(v1, v2)
    e2 = Edge(v2, v3)
    G.add_edge(e0)
    G.add_edge(e1)
    G.add_edge(e2)
    result_coloring = colour_refinement(G.vertices, {v: 0 for v in G.vertices})
    assert same_group(result_coloring, [v0, v3])
    assert same_group(result_coloring, [v1, v2])


def test_four_nodes_square():
    G = Graph(False, 4)
    v0 = G.vertices[0]
    v1 = G.vertices[1]
    v2 = G.vertices[2]
    v3 = G.vertices[3]
    G.add_vertex(v0)
    G.add_vertex(v1)
    G.add_vertex(v2)
    G.add_vertex(v3)
    e0 = Edge(v0, v1)
    e1 = Edge(v1, v2)
    e2 = Edge(v2, v3)
    e3 = Edge(v3, v0)
    G.add_edge(e0)
    G.add_edge(e1)
    G.add_edge(e2)
    G.add_edge(e3)
    result_coloring = colour_refinement(G.vertices, {v: 0 for v in G.vertices})
    assert same_group(result_coloring, [v0, v1, v2, v3])


def test_five_nodes_triangle_with_legs():
    G = Graph(False, 5)
    v0 = G.vertices[0]
    v1 = G.vertices[1]
    v2 = G.vertices[2]
    v3 = G.vertices[3]
    v4 = G.vertices[4]
    G.add_vertex(v0)
    G.add_vertex(v1)
    G.add_vertex(v2)
    G.add_vertex(v3)
    G.add_vertex(v4)
    e0 = Edge(v0, v1)
    e1 = Edge(v1, v2)
    e2 = Edge(v1, v3)
    e3 = Edge(v0, v3)
    e4 = Edge(v3, v4)

    G.add_edge(e0)
    G.add_edge(e1)
    G.add_edge(e2)
    G.add_edge(e3)
    G.add_edge(e4)
    result_coloring = colour_refinement(G.vertices, {v: 0 for v in G.vertices})
    assert same_group(result_coloring, [v1, v3])
    assert same_group(result_coloring, [v2, v4])
    assert not same_group(result_coloring, [v0, v3])
    assert not same_group(result_coloring, [v0, v4])


def test_five_nodes_triangle_with_legs_negative_initial_colouring():
    G = Graph(False, 5)
    v0 = G.vertices[0]
    v1 = G.vertices[1]
    v2 = G.vertices[2]
    v3 = G.vertices[3]
    v4 = G.vertices[4]
    G.add_vertex(v0)
    G.add_vertex(v1)
    G.add_vertex(v2)
    G.add_vertex(v3)
    G.add_vertex(v4)
    e0 = Edge(v0, v1)
    e1 = Edge(v1, v2)
    e2 = Edge(v1, v3)
    e3 = Edge(v0, v3)
    e4 = Edge(v3, v4)

    G.add_edge(e0)
    G.add_edge(e1)
    G.add_edge(e2)
    G.add_edge(e3)
    G.add_edge(e4)
    initial_colouring = {v0: -100, v1: -99, v2: -98, v3: -99, v4: -98}
    result_coloring = colour_refinement(G.vertices, initial_colouring)
    assert same_group(result_coloring, [v1, v3])
    assert same_group(result_coloring, [v2, v4])
    assert not same_group(result_coloring, [v0, v3])
    assert not same_group(result_coloring, [v0, v4])

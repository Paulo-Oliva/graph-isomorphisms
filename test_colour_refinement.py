from colour_ref import colour_refinement
from count_isomorphisms import check_isomorphism
from graph import Edge, Graph, Vertex
from graph_io import load_graph


def test_colorref_largeexample_4_1026():
    path = "./cr_tests/" + "colorref_largeexample_4_1026.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
    assert check_isomorphism([], [], graphs[0], graphs[1])
    assert check_isomorphism([], [], graphs[2], graphs[3])
    assert not check_isomorphism([], [], graphs[0], graphs[2])
    assert not check_isomorphism([], [], graphs[0], graphs[3])


def test_colorref_largeexample_6_960():
    path = "./cr_tests/" + "colorref_largeexample_6_960.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
    assert check_isomorphism([], [], graphs[0], graphs[4])
    assert check_isomorphism([], [], graphs[1], graphs[3])
    assert check_isomorphism([], [], graphs[2], graphs[5])
    assert not check_isomorphism([], [], graphs[0], graphs[1])
    assert not check_isomorphism([], [], graphs[0], graphs[2])
    assert not check_isomorphism([], [], graphs[1], graphs[2])


def test_colorref_smallexample_2_49():
    path = "./cr_tests/" + "colorref_smallexample_2_49.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
    assert check_isomorphism([], [], graphs[0], graphs[1])


def test_colorref_smallexample_4_7():
    path = "./cr_tests/" + "colorref_smallexample_4_7.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
    assert check_isomorphism([], [], graphs[0], graphs[2])
    assert check_isomorphism([], [], graphs[1], graphs[3])
    assert not check_isomorphism([], [], graphs[0], graphs[1])


def test_colorref_smallexample_4_16():
    path = "./cr_tests/" + "colorref_smallexample_4_16.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
    assert check_isomorphism([], [], graphs[0], graphs[1])
    assert check_isomorphism([], [], graphs[2], graphs[3])
    assert not check_isomorphism([], [], graphs[0], graphs[2])


def test_colorref_smallexample_6_15():
    path = "./cr_tests/" + "colorref_smallexample_6_15.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
    assert check_isomorphism([], [], graphs[0], graphs[1])
    assert check_isomorphism([], [], graphs[2], graphs[3])
    assert check_isomorphism([], [], graphs[4], graphs[5])
    assert not check_isomorphism([], [], graphs[0], graphs[2])
    assert not check_isomorphism([], [], graphs[0], graphs[4])
    assert not check_isomorphism([], [], graphs[2], graphs[4])


def test_cref9vert_4_9():
    path = "./cr_tests/" + "cref9vert_4_9.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
    assert check_isomorphism([], [], graphs[0], graphs[3])
    assert check_isomorphism([], [], graphs[1], graphs[2])
    assert not check_isomorphism([], [], graphs[0], graphs[1])


def test_cref9vert3comp_10_27():
    path = "./cr_tests/" + "cref9vert3comp_10_27.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
    assert check_isomorphism([], [], graphs[0], graphs[3])
    assert check_isomorphism([], [], graphs[1], graphs[8])
    assert check_isomorphism([], [], graphs[1], graphs[9])
    assert check_isomorphism([], [], graphs[2], graphs[4])
    assert check_isomorphism([], [], graphs[2], graphs[7])
    assert check_isomorphism([], [], graphs[5], graphs[6])
    assert not check_isomorphism([], [], graphs[0], graphs[1])
    assert not check_isomorphism([], [], graphs[0], graphs[2])
    assert not check_isomorphism([], [], graphs[0], graphs[5])
    assert not check_isomorphism([], [], graphs[1], graphs[2])
    assert not check_isomorphism([], [], graphs[1], graphs[5])
    assert not check_isomorphism([], [], graphs[2], graphs[5])
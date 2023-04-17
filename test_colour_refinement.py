from src.count_isomorphisms import check_isomorphism
from src.graph_io import load_graph

GRAPHS_PATH = "./tests/cref/"


def test_colorref_largeexample_4_1026():
    path = GRAPHS_PATH + "colorref_largeexample_4_1026.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
    assert check_isomorphism(
        [], [], graphs[0], graphs[1],
        {v: v.degree
         for v in graphs[0].vertices + graphs[1].vertices})
    assert check_isomorphism(
        [], [], graphs[2], graphs[3],
        {v: v.degree
         for v in graphs[2].vertices + graphs[3].vertices})
    assert not check_isomorphism(
        [], [], graphs[0], graphs[2],
        {v: v.degree
         for v in graphs[0].vertices + graphs[2].vertices})
    assert not check_isomorphism(
        [], [], graphs[0], graphs[3],
        {v: v.degree
         for v in graphs[0].vertices + graphs[3].vertices})


def test_colorref_largeexample_6_960():
    path = GRAPHS_PATH + "colorref_largeexample_6_960.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
    assert check_isomorphism(
        [], [], graphs[0], graphs[4],
        {v: v.degree
         for v in graphs[0].vertices + graphs[4].vertices})
    assert check_isomorphism(
        [], [], graphs[1], graphs[3],
        {v: v.degree
         for v in graphs[1].vertices + graphs[3].vertices})
    assert check_isomorphism(
        [], [], graphs[2], graphs[5],
        {v: v.degree
         for v in graphs[2].vertices + graphs[5].vertices})
    assert not check_isomorphism(
        [], [], graphs[0], graphs[1],
        {v: v.degree
         for v in graphs[0].vertices + graphs[1].vertices})
    assert not check_isomorphism(
        [], [], graphs[0], graphs[2],
        {v: v.degree
         for v in graphs[0].vertices + graphs[2].vertices})
    assert not check_isomorphism(
        [], [], graphs[1], graphs[2],
        {v: v.degree
         for v in graphs[1].vertices + graphs[2].vertices})


def test_colorref_smallexample_2_49():
    path = GRAPHS_PATH + "colorref_smallexample_2_49.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
    assert check_isomorphism(
        [], [], graphs[0], graphs[1],
        {v: v.degree
         for v in graphs[0].vertices + graphs[1].vertices})


def test_colorref_smallexample_4_7():
    path = GRAPHS_PATH + "colorref_smallexample_4_7.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
    assert check_isomorphism(
        [], [], graphs[0], graphs[2],
        {v: v.degree
         for v in graphs[0].vertices + graphs[2].vertices})
    assert check_isomorphism(
        [], [], graphs[1], graphs[3],
        {v: v.degree
         for v in graphs[1].vertices + graphs[3].vertices})
    assert not check_isomorphism(
        [], [], graphs[0], graphs[1],
        {v: v.degree
         for v in graphs[0].vertices + graphs[1].vertices})


def test_colorref_smallexample_4_16():
    path = GRAPHS_PATH + "colorref_smallexample_4_16.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
    assert check_isomorphism(
        [], [], graphs[0], graphs[1],
        {v: v.degree
         for v in graphs[0].vertices + graphs[1].vertices})
    assert check_isomorphism(
        [], [], graphs[2], graphs[3],
        {v: v.degree
         for v in graphs[2].vertices + graphs[3].vertices})
    assert not check_isomorphism(
        [], [], graphs[0], graphs[2],
        {v: v.degree
         for v in graphs[0].vertices + graphs[2].vertices})


def test_colorref_smallexample_6_15():
    path = GRAPHS_PATH + "colorref_smallexample_6_15.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
    assert check_isomorphism(
        [], [], graphs[0], graphs[1],
        {v: v.degree
         for v in graphs[0].vertices + graphs[1].vertices})
    assert check_isomorphism(
        [], [], graphs[2], graphs[3],
        {v: v.degree
         for v in graphs[2].vertices + graphs[3].vertices})
    assert check_isomorphism(
        [], [], graphs[4], graphs[5],
        {v: v.degree
         for v in graphs[4].vertices + graphs[5].vertices})
    assert not check_isomorphism(
        [], [], graphs[0], graphs[2],
        {v: v.degree
         for v in graphs[0].vertices + graphs[2].vertices})
    assert not check_isomorphism(
        [], [], graphs[0], graphs[4],
        {v: v.degree
         for v in graphs[0].vertices + graphs[4].vertices})
    assert not check_isomorphism(
        [], [], graphs[2], graphs[4],
        {v: v.degree
         for v in graphs[2].vertices + graphs[4].vertices})


def test_cref9vert_4_9():
    path = GRAPHS_PATH + "cref9vert_4_9.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
    assert check_isomorphism(
        [], [], graphs[0], graphs[3],
        {v: v.degree
         for v in graphs[0].vertices + graphs[3].vertices})
    assert check_isomorphism(
        [], [], graphs[1], graphs[2],
        {v: v.degree
         for v in graphs[1].vertices + graphs[2].vertices})
    assert not check_isomorphism(
        [], [], graphs[0], graphs[1],
        {v: v.degree
         for v in graphs[0].vertices + graphs[1].vertices})


def test_cref9vert3comp_10_27():
    path = GRAPHS_PATH + "cref9vert3comp_10_27.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
    assert check_isomorphism(
        [], [], graphs[0], graphs[3],
        {v: v.degree
         for v in graphs[0].vertices + graphs[3].vertices})
    assert check_isomorphism(
        [], [], graphs[1], graphs[8],
        {v: v.degree
         for v in graphs[1].vertices + graphs[8].vertices})
    assert check_isomorphism(
        [], [], graphs[1], graphs[9],
        {v: v.degree
         for v in graphs[1].vertices + graphs[9].vertices})
    assert check_isomorphism(
        [], [], graphs[2], graphs[4],
        {v: v.degree
         for v in graphs[2].vertices + graphs[4].vertices})
    assert check_isomorphism(
        [], [], graphs[2], graphs[7],
        {v: v.degree
         for v in graphs[2].vertices + graphs[7].vertices})
    assert check_isomorphism(
        [], [], graphs[5], graphs[6],
        {v: v.degree
         for v in graphs[5].vertices + graphs[6].vertices})
    assert not check_isomorphism(
        [], [], graphs[0], graphs[1],
        {v: v.degree
         for v in graphs[0].vertices + graphs[1].vertices})
    assert not check_isomorphism(
        [], [], graphs[0], graphs[2],
        {v: v.degree
         for v in graphs[0].vertices + graphs[2].vertices})
    assert not check_isomorphism(
        [], [], graphs[0], graphs[5],
        {v: v.degree
         for v in graphs[0].vertices + graphs[5].vertices})
    assert not check_isomorphism(
        [], [], graphs[1], graphs[2],
        {v: v.degree
         for v in graphs[1].vertices + graphs[2].vertices})
    assert not check_isomorphism(
        [], [], graphs[1], graphs[5],
        {v: v.degree
         for v in graphs[1].vertices + graphs[5].vertices})
    assert not check_isomorphism(
        [], [], graphs[2], graphs[5],
        {v: v.degree
         for v in graphs[2].vertices + graphs[5].vertices})

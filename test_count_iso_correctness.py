import pytest

from count_isomorphisms_test import count_iso
from src.graph_io import load_graph


def _count_iso(name, expected_groups):
    path = "./tests/branching/" + name
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
    result = count_iso(graphs)

    assert result == expected_groups


# @pytest.mark.timeout(10)
def test_count_iso_torus24():
    _count_iso("torus24.grl", [([0, 3], 96), ([1, 2], 96)])


@pytest.mark.timeout(10)
def test_count_iso_torus72():
    _count_iso("torus72.grl", [([0, 2], 288), ([1, 5], 288), ([3, 6], 288),
                               ([4, 7], 288)])


@pytest.mark.timeout(10)
def test_count_iso_products72():
    _count_iso("products72.grl", [([0, 6], 288), ([1, 5], 576), ([2, 3], 576),
                                  ([4, 7], 864)])


# @pytest.mark.timeout(20)
def test_count_iso_trees11():
    _count_iso("trees11.grl", [([0, 3], 6), ([1, 4], 1), ([2, 5], 2)])


@pytest.mark.timeout(5)
def test_count_iso_trees36():
    _count_iso("trees36.grl", [([0, 7], 2), ([1, 4], 6), ([2, 6], 2),
                               ([3, 5], 6)])


@pytest.mark.timeout(40)
def test_count_iso_modulesD():
    _count_iso("modulesD.grl", [([0, 2], 24), ([1, 3], 1), ([4, 5], 24)])


@pytest.mark.timeout(10)
def test_count_iso_cubes3():
    _count_iso("cubes3.grl", [([0, 2], 48), ([1, 3], 16)])


@pytest.mark.timeout(20)
def test_count_iso_cubes5():
    _count_iso("cubes5.grl", [([0, 1], 3840), ([2, 3], 24)])


@pytest.mark.timeout(80)
def test_count_iso_cubes6():
    _count_iso("cubes6.grl", [([0, 1], 96), ([2, 3], 46080)])


# @pytest.mark.timeout(10)
def test_count_iso_wheeljoin14():
    _count_iso("wheeljoin14.grl", [([0, 1], 1600), ([2, 3], 672),
                                   ([4, 7], 1536), ([5, 6], 720)])

from graph_io import load_graph
from count_isomorphisms_test import count_iso2
import pytest

base_path = "./graphs/"

# @pytest.mark.timeout(10)
def test_count_iso_torus24():
    path = base_path + "torus24.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0,3], 96),([1,2],96)]
    result = count_iso2(graphs)

    assert result == expected_groups

@pytest.mark.timeout(10)
def test_count_iso_torus72():
    path = base_path + "torus72.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0,2], 288),([1,5],288), ([3,6],288), ([4,7],288)]
    result = count_iso2(graphs)

    assert result == expected_groups


@pytest.mark.timeout(10)
def test_count_iso_products72():
    path = base_path + "products72.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0,6], 288),([1,5],576), ([2,3],576), ([4,7],864)]
    result = count_iso2(graphs)

    assert result == expected_groups


    
# @pytest.mark.timeout(20)
def test_count_iso_trees11():
    path = base_path + "trees11.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0,3],  6),([1,4], 1), ([2,5], 2)]
    result = count_iso2(graphs)

    assert result == expected_groups
    

@pytest.mark.timeout(5)
def test_count_iso_trees36():
    path = base_path + "trees36.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0,7],  2),([1,4], 6), ([2,6], 2), ([3,5],6)]
    result = count_iso2(graphs)

    assert result == expected_groups



@pytest.mark.timeout(40)
def test_count_iso_modulesD():
    path = base_path + "modulesD.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0,2],  24),([1,3], 1), ([4,5], 24)]
    result = count_iso2(graphs)

    assert result == expected_groups

@pytest.mark.timeout(10)
def test_count_iso_cubes3():
    path = base_path + "cubes3.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0,2],  48),([1,3], 16)]
    result = count_iso2(graphs)

    assert result == expected_groups


@pytest.mark.timeout(20)
def test_count_iso_cubes5():
    path = base_path + "cubes5.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0,1],  3840),([2,3], 24)]
    result = count_iso2(graphs)

    assert result == expected_groups


@pytest.mark.timeout(80)
def test_count_iso_cubes6():
    path = base_path + "cubes6.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0,1],  96),([2,3], 46080)]
    result = count_iso2(graphs)

    assert result == expected_groups



# @pytest.mark.timeout(10)
def test_count_iso_wheeljoin14():
    path = base_path + "wheeljoin14.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0, 1], 1600),([2, 3], 672),([4, 7], 1536),([5, 6], 720)]
    result = count_iso2(graphs)

    assert result == expected_groups


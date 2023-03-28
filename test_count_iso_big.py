from graph_io import load_graph
from count_isomorphisms_test import count_iso2
import pytest

base_path = "./graphs/"


@pytest.mark.timeout(80)
def test_count_iso_products216():
    path = base_path + "products216.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0,6],  1728),([1,7], 1728), ([2,9], 1728), ([3,8],10368),([4,5],1728)]
    result = count_iso2(graphs)

    assert result == expected_groups


    
@pytest.mark.timeout(240)
def test_count_iso_torus144():
    path = base_path + "torus144.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0,6],  576),([1,7], 576), ([2,4], 576), ([3,10],576),([5,9],1152), ([8,11],576)]
    result = count_iso2(graphs)

    assert result == expected_groups

@pytest.mark.timeout(240)
def test_count_iso_cographs1():
    path = base_path + "cographs1.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0,3],  5971968),([1,2], 995328)]
    result = count_iso2(graphs)

    assert result == expected_groups

@pytest.mark.timeout(240)
def test_count_iso_trees90():
    path = base_path + "trees90.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0,3],  6912),([1,2], 20736)]
    result = count_iso2(graphs)

    assert result == expected_groups

@pytest.mark.timeout(240)
def test_count_iso_modulesC():
    path = base_path + "modulesC.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0,7],  17915904),([1,5], 17915904), ([2,4], 2488320), ([3, 6], 2985984)]
    result = count_iso2(graphs)

    assert result == expected_groups


@pytest.mark.timeout(80)
def test_count_iso_cubes7():
    path = base_path + "cubes7.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0,3],  645120),([1,2], 480)]
    result = count_iso2(graphs)

    assert result == expected_groups

@pytest.mark.timeout(80)
def test_count_iso_cubes9():
    path = base_path + "cubes9.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0, 1], 185794560),([2, 3], 20160)]
    result = count_iso2(graphs)

    assert result == expected_groups

@pytest.mark.timeout(80)
def test_count_iso_bigtrees1():
    path = base_path + "bigtrees1.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0, 2], 442368),([1, 3],  5308416)]
    result = count_iso2(graphs)

    assert result == expected_groups

@pytest.mark.timeout(80)
def test_count_iso_bigtrees2():
    path = base_path + "bigtrees2.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0, 3], 80244904034304),([1, 2],  160489808068608)]
    result = count_iso2(graphs)

    assert result == expected_groups

@pytest.mark.timeout(80)
def test_count_iso_bigtrees3():
    path = base_path + "bigtrees3.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0, 2], 2772351862699137701073289910157312),([1, 3],  462058643783189616845548318359552)]
    result = count_iso2(graphs)

    assert result == expected_groups

@pytest.mark.timeout(80)
def test_count_iso_wheeljoin33():
    path = base_path + "wheeljoin33.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0, 4], 8257536),([1, 2], 7962624),([3, 5], 50577408),([6, 7], 1290240)]
    result = count_iso2(graphs)

    assert result == expected_groups

@pytest.mark.timeout(80)
def test_count_iso_wheelstar12():
    path = base_path + "wheelstar12.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0, 3], 1935360),([1, 2], 6718464)]
    result = count_iso2(graphs)

    assert result == expected_groups

@pytest.mark.timeout(80)
def test_count_iso_wheelstar15():
    path = base_path + "wheelstar15.grl"
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _nothing = load_graph(grl, read_list=True)
    expected_groups = [([0, 7], 1703116800),([1, 4] ,3009871872),([2, 3] ,10642046976),([5, 6], 2890137600)]
    result = count_iso2(graphs)

    assert result == expected_groups
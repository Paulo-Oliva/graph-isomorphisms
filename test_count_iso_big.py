import pytest

from count_isomorphisms_test import count_iso
from graph_io import load_graph


def _count_iso(name, expected_groups):
    path = "./graphs/" + name
    with open(path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
    result = count_iso(graphs)

    assert result == expected_groups


@pytest.mark.timeout(80)
def test_count_iso_products216():
    _count_iso("products216.grl", [([0, 6], 1728), ([1, 7], 1728),
                                   ([2, 9], 1728), ([3, 8], 10368),
                                   ([4, 5], 1728)])


@pytest.mark.timeout(240)
def test_count_iso_torus144():
    expected_groups = [([0, 6], 576), ([1, 7], 576), ([2, 4], 576),
                       ([3, 10], 576), ([5, 9], 1152), ([8, 11], 576)]
    _count_iso("torus144.grl", expected_groups)


@pytest.mark.timeout(240)
def test_count_iso_cographs1():
    _count_iso("cographs1.grl", [([0, 3], 5971968), ([1, 2], 995328)])


@pytest.mark.timeout(240)
def test_count_iso_trees90():
    _count_iso("trees90.grl", [([0, 3], 6912), ([1, 2], 20736)])


@pytest.mark.timeout(240)
def test_count_iso_modulesC():
    _count_iso("modulesC.grl", [([0, 7], 17915904), ([1, 5], 17915904),
                                ([2, 4], 2488320), ([3, 6], 2985984)])


@pytest.mark.timeout(80)
def test_count_iso_cubes7():
    _count_iso("cubes7.grl", [([0, 3], 645120), ([1, 2], 480)])


@pytest.mark.timeout(80)
def test_count_iso_cubes9():
    _count_iso("cubes9.grl", [([0, 1], 185794560), ([2, 3], 20160)])


@pytest.mark.timeout(80)
def test_count_iso_bigtrees1():
    _count_iso("bigtrees1.grl", [([0, 2], 442368), ([1, 3], 5308416)])


@pytest.mark.timeout(80)
def test_count_iso_bigtrees2():
    _count_iso("bigtrees2.grl", [([0, 3], 80244904034304),
                                 ([1, 2], 160489808068608)])


@pytest.mark.timeout(80)
def test_count_iso_bigtrees3():
    _count_iso("bigtrees3.grl", [([0, 2], 2772351862699137701073289910157312),
                                 ([1, 3], 462058643783189616845548318359552)])


@pytest.mark.timeout(80)
def test_count_iso_wheeljoin33():
    _count_iso("wheeljoin33.grl", [([0, 4], 8257536), ([1, 2], 7962624),
                                   ([3, 5], 50577408), ([6, 7], 1290240)])


@pytest.mark.timeout(80)
def test_count_iso_wheelstar12():
    _count_iso("wheelstar12.grl", [([0, 3], 1935360), ([1, 2], 6718464)])


@pytest.mark.timeout(80)
def test_count_iso_wheelstar15():
    _count_iso("wheelstar15.grl", [([0, 7], 1703116800), ([1, 4], 3009871872),
                                   ([2, 3], 10642046976),
                                   ([5, 6], 2890137600)])

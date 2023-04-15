from timeit import timeit

from count_isomorphisms import check_isomorphism, count_isomorphism
from count_isomorphisms_test import print_isomorphisms
from graph import Graph
from graph_io import load_graph
from preprocessing import count_automorphisms


def count_iso(graphs: list[Graph]) -> list[tuple[list[int], int]]:
    already_checked = {g_inx: False for g_inx in range(len(graphs))}
    iso_groups = []
    for i in range(len(graphs)):
        if already_checked[i]:
            continue
        already_checked[i] = True
        iso_group = [i]
        for j in range(i + 1, len(graphs)):
            if already_checked[j]:
                continue
                # print("Checking", i, j)
            are_iso = check_isomorphism([], [], graphs[i], graphs[j])
            if are_iso:
                iso_group.append(j)
                already_checked[j] = True
        iso_groups.append(iso_group)
    return iso_groups


def print_aut(filename):
    with open("benchmarks/final_test/automorphism_tests/" + filename,
              "r",
              encoding="utf-8") as grl:
        graph = load_graph(grl)

        print("Number of automorphisms: ", count_automorphisms(graph))
        # g2 = graph.copy()
        # print("Number of automorphisms: ", count_isomorphism([], [], graph, g2, {v: 0 for v in graph.vertices + g2.vertices}))


def print_iso(filename):
    with open("benchmarks/final_test/isomorphism_tests/" + filename,
              "r",
              encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
        result = count_iso(graphs)
        print(filename + ":")
        for group in result:
            print(group)


if __name__ == '__main__':
    # print_isomorphisms("benchmarks/final_test/iso_auto_tests")

    print(timeit(lambda: print_aut("basicAut1.gr"), number=1), "\n", sep="s")

    # print(timeit(lambda: print_aut("basicAut2.gr"), number=1), "\n", sep="s")

    # print(timeit(lambda: print_iso("basicGI1.grl"), number=1), "\n", sep="s")
    # print(timeit(lambda: print_iso("basicGI2.grl"), number=1), "\n", sep="s")
    # print(timeit(lambda: print_iso("basicGI3.grl"), number=1), "\n", sep="s")

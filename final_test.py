import os
import sys
from timeit import timeit

from count_isomorphisms_test import count_iso
from src.count_isomorphisms import check_isomorphism
from src.graph import Graph
from src.graph_io import load_graph
from src.preprocessing import count_automorphisms


def find_isomorphic_graphs(graphs: list[Graph]) -> list[list[int]]:
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
            are_iso = check_isomorphism(
                [], [], graphs[i], graphs[j],
                {v: v.degree
                 for v in graphs[i].vertices + graphs[j].vertices})
            if are_iso:
                iso_group.append(j)
                already_checked[j] = True
        iso_groups.append(iso_group)
    return iso_groups


def print_iso(file):
    print(file.name + ":")
    with open(file.path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
        result = find_isomorphic_graphs(graphs)
        print("Equivalence classes:")
        for group in result:
            print(group)


def print_aut(file):
    print(file.name)
    with open(file.path, "r", encoding="utf-8") as grl:
        graph = load_graph(grl)
        print("{:<11}".format("Graph:"), "#Aut:")
        print("{:<11}".format("0"), count_automorphisms(graph))


def print_aut2(file):
    print(file.name)
    with open(file.path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
        i = 0
        for graph in graphs:
            print("{:<11}".format("Graph:"), "#Aut:")
            print("{:<11}".format(i), count_automorphisms(graph))
            i += 1


def print_iso_aut(file):
    print(file.name)
    with open(file.path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
        print("{:<27}".format("Equivalence classes:"), "#Aut:")
        for iso_groups, iso_count in count_iso(graphs):
            print("{:<27}".format(str(iso_groups)), iso_count)


def solve(path: str):
    for file in os.scandir(path):
        if "Aut" in file.name and "GI" in file.name:
            print(timeit(lambda: print_iso_aut(file), number=1), "\n", sep="s")

        elif "Aut" in file.name and file.name.endswith(".gr"):
            print(timeit(lambda: print_aut(file), number=1), "\n", sep="s")
        elif "GI" in file.name:
            print(timeit(lambda: print_iso(file), number=1), "\n", sep="s")
        else:
            print(timeit(lambda: print_aut2(file), number=1), "\n", sep="s")


if __name__ == '__main__':
    PATH = sys.argv[1] if len(sys.argv) > 1 else "input"
    print("Total time: ", timeit(lambda: solve(PATH), number=1), "s", sep="")

"""
This module is the main module of the project.

It contains the main function of the project, which is used to solve the
GI and Aut problems for all the files in the given directory.

Functions:
- print_iso: Print the isomorphic graphs in a .grl file.
- print_aut_gr: Print the automorphism count of a .gr file.
- print_aut_grl: Print the automorphism count of a .grl file.
- print_iso_aut: Print the isomorphic graphs and the automorphism count of a
    .grl file.
- solve: Solve the GI and Aut problems for all the files in the given
    directory.
"""

import os
import sys
from timeit import timeit

from count_isomorphisms_test import count_iso
from src.count_isomorphisms import check_isomorphism
from src.graph import Graph
from src.graph_io import load_graph
from src.preprocessing import count_automorphisms


def _find_isomorphic_graphs(graphs: list[Graph]) -> list[list[int]]:
    """
    Find the isomorphic graphs in a list of graphs.

    Args:
        graphs (list[Graph]): The list of graphs.

    Returns:
        list[list[int]]: A list of lists of indices of the isomorphic graphs.
    """
    already_checked = {g_index: False for g_index in range(len(graphs))}
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
    """
    Print the isomorphic graphs in a .grl file.

    Args:
        file (os.DirEntry): The .grl file to be read.
    """
    print(file.name + ":")
    with open(file.path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
        result = _find_isomorphic_graphs(graphs)
        print("Equivalence classes:")
        for group in result:
            print(group)


def print_aut_gr(file):
    """
    Print the automorphism count of a .gr file.

    Args:
        file (os.DirEntry): The .gr file to be read.
    """
    print(file.name)
    with open(file.path, "r", encoding="utf-8") as grl:
        graph = load_graph(grl)
        print(f"{'Graph:' : <11} #Aut:")
        print(f"{'0' : <11} {count_automorphisms(graph)}")


def print_aut_grl(file):
    """
    Print the automorphism count of a .grl file.

    Args:
        file (os.DirEntry): The .grl file to be read.
    """
    print(file.name)
    with open(file.path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
        i = 0
        for graph in graphs:
            print(f"{'Graph:' : <11} #Aut:")
            print(f"{i :<11} {count_automorphisms(graph)}")
            i += 1


def print_iso_aut(file):
    """
    Print the isomorphic graphs and the automorphism count of a .grl file.

    Args:
        file (os.DirEntry): The .grl file to be read.
    """
    print(file.name)
    with open(file.path, "r", encoding="utf-8") as grl:
        graphs, _ = load_graph(grl, read_list=True)
        print(f"{'Equivalence classes:' : <27} #Aut")
        for iso_groups, iso_count in count_iso(graphs):
            print(f"{str(iso_groups) : <27} {iso_count}")


def solve(path: str):
    """
    Solve the GI and Aut problems for all the files in the given directory.

    Args:
        path (str): The path to the directory containing the files.
    """
    for file in os.scandir(path):
        if "Aut" in file.name and "GI" in file.name:
            print(timeit(lambda: print_iso_aut(file), number=1), "\n", sep="s")
        elif "Aut" in file.name and file.name.endswith(".gr"):
            print(timeit(lambda: print_aut_gr(file), number=1), "\n", sep="s")
        elif "GI" in file.name:
            print(timeit(lambda: print_iso(file), number=1), "\n", sep="s")
        elif "Aut" in file.name and file.name.endswith(".grl"):
            print(timeit(lambda: print_aut_grl(file), number=1), "\n", sep="s")


if __name__ == '__main__':
    PATH = sys.argv[1] if len(sys.argv) > 1 else "input"
    print("Total time: ", timeit(lambda: solve(PATH), number=1), "s", sep="")

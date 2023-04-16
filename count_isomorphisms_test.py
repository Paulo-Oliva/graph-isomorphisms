"""
This module can be used to run the colour refinement algorithm on .grl files.
"""

import os
import sys
import timeit

from count_isomorphisms import check_isomorphism, count_isomorphism
from graph import Graph
from graph_io import load_graph
from preprocessing import count_automorphisms


def skip_large(file):
    to_skip = [
        "cubes7.grl", "cubes8.grl", "cubes9.grl", "modulesC.grl",
        "wheeljoin25.grl", "wheeljoin33.grl", "trees90.grl", "torus144.grl",
        "products216.grl"
    ]
    if file.name.startswith("big") or file.name.startswith(
            "wheeljoin") or file.name.startswith(
                "wheelstar") or file.name in to_skip:
        return True


def print_isomorphisms(path: str):
    """
    This function prints the possible isomorphisms in all the graphs in a
    directory of .grl files. The directory is specified by the path
    argument.

    Args:
        path (str): The path to the directory containing the .grl files.
    """
    files = os.scandir(path)
    for file in files:
        if not file.name.startswith("tree"):
            continue

        print(file.name)
        # Load the graphs
        with open(file.path, "r", encoding="utf-8") as grl:
            graphs, _ = load_graph(grl, read_list=True)

        # if skip_large(file):
        #     continue

        t = timeit.timeit(lambda: print_result(count_iso(graphs)), number=1)
        print(t, "s", sep="")
        print()


def print_result(result):
    for group, number_of_iso in result:
        print(group, number_of_iso)


def count_iso(graphs: list[Graph]) -> list[tuple[list[int], int]]:
    # Preprocess z

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
        iso_groups.append((iso_group, count_automorphisms(graphs[i])))
    return iso_groups


if __name__ == "__main__":
    # Get an argument for the path
    # Default to "graphs"
    PATH = sys.argv[1] if len(sys.argv) > 1 else "graphs"
    # Iterate over all files
    print_isomorphisms(PATH)

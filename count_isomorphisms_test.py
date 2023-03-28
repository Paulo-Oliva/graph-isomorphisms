"""
_summary_

Returns:
    _type_: _description_
"""
# Paulo Oliva

import os
import sys
from graph import Graph
from graph_io import load_graph
from count_isomorphisms import count_isomorphism, check_isomorphism
import timeit
import time
from preprocessing import count_automorphisms


def skip_large(file):
    if file.name.startswith("big"):
        return True

    if file.name.startswith("cograph"):
        return True

    if file.name.startswith("cubes7"):
        return True

    if file.name.startswith("cubes8"):
        return True

    if file.name.startswith("cubes9"):
        return True

    if file.name.startswith("modulesC"):
        return True

    if file.name.startswith("wheeljoin25"):
        return True
    
    if file.name.startswith("wheeljoin33"):
        return True

    if file.name.startswith("wheelstar"):
        return True
    
    if file.name.startswith("trees90"):
        return True
    
    if file.name.startswith("torus144"):
        return True
    
    if file.name.startswith("products216"):
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
        print(file.name)
        # Load the graphs

        with open(file.path, "r", encoding="utf-8") as grl:
            graphs, _nothing = load_graph(grl, read_list=True)

        if skip_large(file):
            continue

        # already_checked = set()
        # t = timeit.timeit(lambda: count_iso(graphs, already_checked), number=1)
        start = time.time_ns()
        result = count_iso2(graphs)
        stop = time.time_ns()
        for group, number_of_iso in result:
            print(group, number_of_iso)
        print((stop - start)/(10**9), 's')
        print()


def count_iso(graphs, already_checked):
    for i in range(len(graphs)):
        to_print = [i]
        ans = 0
        for j in range(i + 1, len(graphs)):
            if j in already_checked:
                continue
                # print("Checking", i, j)
            answer = count_isomorphism([], [], graphs[i], graphs[j])
            if answer:
                to_print.append(j)
                already_checked.add(j)
                ans = answer
        if len(to_print) > 1:
            print(to_print, ans)

def count_iso2(graphs : list["Graph"]):
    already_checked = {g_inx:False for g_inx in range(len(graphs))}
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
        iso_groups.append((iso_group, count_isomorphism([],[],graphs[i],graphs[i].copy())))
    return iso_groups
        


if __name__ == "__main__":
    # Get an argument for the path
    # Default to "graphs"
    PATH = sys.argv[1] if len(sys.argv) > 1 else "graphs"
    # Iterate over all files
    print_isomorphisms(PATH)

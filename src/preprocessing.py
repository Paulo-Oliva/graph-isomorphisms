"""
This module contains functions for preprocessing the graph.

Moreover, it also contains a function for counting the automorphisms of a
graph using a preprocessing based on the true and false twins of the graph.

Functions:
- count_automorphisms: Count the automorphisms of a graph.
- calc_true_twins: Calculate the true twins of a graph.
- calc_false_twins: Calculate the false twins of a graph.
- check_neighbourhood_FT: Check if two vertices are false twins.
- check_neighbourhood_TT: Check if two vertices are true twins.
"""

from math import factorial

from .count_isomorphisms import count_isomorphism
from .graph import Graph, Vertex


def count_automorphisms(G: Graph) -> int:
    """
    Count the automorphisms of a graph.

    This function uses the preprocessing based on the true and false twins of
    the graph to count the automorphisms of the graph.

    Args:
        G (Graph): The graph.

    Returns:
        int: The number of automorphisms of the graph.
    """
    true_twins = calc_true_twins(G)
    false_twins = calc_false_twins(G)
    colour_counter = 0
    len_of_true_family_to_colour_dict = {}

    for true_twin in true_twins:
        len_f = len(true_twin)
        if len_f not in len_of_true_family_to_colour_dict.keys():
            colour_counter += 1
            len_of_true_family_to_colour_dict[len_f] = colour_counter
    len_of_false_family_to_colour_dict = {}
    for false_twin in false_twins:
        len_f = len(false_twin)
        if len_f not in len_of_false_family_to_colour_dict.keys():
            colour_counter += 1
            len_of_false_family_to_colour_dict[len_f] = colour_counter

    edges_to_destroy = set()
    vertices_to_destroy = set()
    coloring = {v: 0 for v in G.vertices}
    vertices = G.vertices

    for true_twin in true_twins:
        chosen_idx = true_twin[0]
        coloring[vertices[chosen_idx]] = len_of_true_family_to_colour_dict[len(
            true_twin)]
        for v_idx in true_twin[1:]:
            v = vertices[v_idx]
            for e in v.incidence:
                u = e.other_end(v)
                u.remove_incidence(v)
                edges_to_destroy.add(e)
            vertices_to_destroy.add(v)
            coloring.pop(v)

    for false_twin in false_twins:
        chosen_idx = false_twin[0]
        coloring[vertices[chosen_idx]] = len_of_false_family_to_colour_dict[
            len(false_twin)]
        for v_idx in false_twin[1:]:
            v = vertices[v_idx]
            for e in v.incidence:
                u = e.other_end(v)
                u.remove_incidence(v)
                edges_to_destroy.add(e)
            vertices_to_destroy.add(v)
            coloring.pop(v)

    _reduce_graph(G, edges_to_destroy, vertices_to_destroy)

    G_copy = G.copy()
    for i, v in enumerate(G_copy.vertices):
        coloring[v] = coloring[G.vertices[i]]

    return count_isomorphism([], [], G, G_copy, coloring) * _calc_multiplier(
        true_twins, false_twins)


def _reduce_graph(G, edges_to_destroy, vertices_to_destroy):
    G._e = list(set(G._e).difference(edges_to_destroy))
    G._v = list(set(G._v).difference(vertices_to_destroy))


def _calc_multiplier(true_twins, false_twins) -> int:
    multiplier = 1
    for true_twin in true_twins:
        multiplier *= factorial(len(true_twin))
    for false_twin in false_twins:
        multiplier *= factorial(len(false_twin))
    return multiplier


def calc_true_twins(G: Graph) -> list:
    """
    Return the true twins of a graph.

    Args:
        G (Graph): The graph.

    Returns:
        list: The true twins of the graph.
    """
    vertices = G.vertices
    true_twins = []
    already_checked = {v_inx: False for v_inx in range(len(vertices))}
    for i in range(len(vertices)):
        if already_checked[i]:
            continue
        already_checked[i] = True
        twin = [i]
        for j in range(i + 1, len(vertices)):
            if already_checked[j]:
                continue
            are_twins = check_neighbourhood_TT(G, vertices[i], vertices[j])
            if are_twins:
                twin.append(j)
                already_checked[j] = True
        if len(twin) > 1:
            true_twins.append(twin)
    return true_twins


def calc_false_twins(G: Graph) -> list:
    """
    Return the false twins of a graph.

    Args:
        G (Graph): The graph.

    Returns:
        list: The false twins of the graph.
    """
    vertices = G.vertices
    false_twins = []
    already_checked = {v_inx: False for v_inx in range(len(vertices))}
    for i in range(len(vertices)):
        if already_checked[i]:
            continue
        already_checked[i] = True
        twin = [i]
        for j in range(i + 1, len(vertices)):
            if already_checked[j]:
                continue
            are_twins = check_neighbourhood_FT(G, vertices[i], vertices[j])
            if are_twins:
                twin.append(j)
                already_checked[j] = True
        if len(twin) > 1:
            false_twins.append(twin)
    return false_twins


def check_neighbourhood_TT(G: Graph, v: Vertex, u: Vertex) -> bool:
    """
    Check if two vertices are true twins.

    Args:
        G (Graph): The graph containing the vertices.
        v (Vertex): The first vertex.
        u (Vertex): The second vertex.

    Returns:
        bool: True if the vertices are true twins, False otherwise.
    """
    if v.degree != u.degree:
        return False
    if not G.is_adjacent(v, u):
        return False
    v_other_neighbours = v.neighbours.copy()
    v_other_neighbours.remove(u)
    u_other_neighbours = u.neighbours.copy()
    u_other_neighbours.remove(v)
    if set(v_other_neighbours) == set(u_other_neighbours):
        return True
    return False


def check_neighbourhood_FT(G: Graph, v: Vertex, u: Vertex) -> bool:
    """
    Check if two vertices are false twins.

    Args:
        G (Graph): The graph containing the vertices.
        v (Vertex): The first vertex.
        u (Vertex): The second vertex.

    Returns:
        bool: True if the vertices are false twins, False otherwise.
    """
    if v.degree != u.degree:
        return False
    if G.is_adjacent(v, u):
        return False
    if set(v.neighbours) == set(u.neighbours):
        return True
    return False

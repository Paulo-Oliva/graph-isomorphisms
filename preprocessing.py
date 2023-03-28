from graph import *
from count_isomorphisms import count_isomorphism
from math import factorial


def count_automorphisms(G: "Graph"):
    true_twins = calc_true_twins(G)
    false_twins = calc_false_twins(G)
    offset = max([len(true_twin) for true_twin in true_twins]) if len(true_twins) > 0 else 0
    edges_to_destroy = set()
    vertices_to_destroy = set()
    coloring = {v: v.degree for v in G.vertices}
    vertices = G.vertices

    for true_twin in true_twins:
        chosen_idx = true_twin[0]
        coloring[vertices[chosen_idx]] = len(true_twin) + 5000
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
        coloring[vertices[chosen_idx]] = len(false_twin)+ offset + 5000
        for v_idx in false_twin[1:]:
            v = vertices[v_idx]
            for e in v.incidence:
                u = e.other_end(v)
                u.remove_incidence(v)
                edges_to_destroy.add(e)
            vertices_to_destroy.add(v)
            coloring.pop(v)

    reduce_graph(G, edges_to_destroy, vertices_to_destroy)

    G_copy = G.copy()
    for i,v in enumerate(G_copy.vertices):
        coloring[v] = coloring[G.vertices[i]]

    return count_isomorphism([],[],G, G_copy, coloring)*calc_multiplier(true_twins, false_twins)


def reduce_graph(G, edges_to_destroy, vertices_to_destroy):
    G._e = list(set(G._e).difference(edges_to_destroy))
    G._v = list(set(G._v).difference(vertices_to_destroy))


def calc_multiplier(TT, FT):
    m = 1
    for true_twin in TT:
        m*=factorial(len(true_twin))
    for false_twin in FT:
        m*=factorial(len(false_twin))
    return m

def calc_true_twins(G: "Graph"):
    vertices = G.vertices
    true_twins = []
    already_checked = { v_inx: False for v_inx in range(len(vertices)) }
    for i in range(len(vertices)):
        if already_checked[i]:
            continue
        already_checked[i] = True
        twin = [i]
        for j in range(i + 1,len(vertices)):
            if already_checked[j]:
                continue
            are_twins = check_neighbourhood_TT(G,vertices[i], vertices[j])
            if are_twins:
                twin.append(j)
                already_checked[j] = True
        if len(twin) > 1:
            true_twins.append(twin)
    return true_twins


def calc_false_twins(G: "Graph"):
    vertices = G.vertices
    false_twins = []
    already_checked = { v_inx: False for v_inx in range(len(vertices)) }
    for i in range(len(vertices)):
        if already_checked[i]:
            continue
        already_checked[i] = True
        twin = [i]
        for j in range(i + 1,len(vertices)):
            if already_checked[j]:
                continue
            are_twins = check_neighbourhood_FT(G,vertices[i], vertices[j])
            if are_twins:
                twin.append(j)
                already_checked[j] = True
        if len(twin) > 1:
            false_twins.append(twin)
    return false_twins

def check_neighbourhood_TT(G:"Graph", v: "Vertex", u: "Vertex"):
    if v.degree != u.degree:
        return False
    if not G.is_adjacent(v,u):
        return False
    v_other_neighbours = v.neighbours.copy()
    v_other_neighbours.remove(u)
    u_other_neighbours = u.neighbours.copy()
    u_other_neighbours.remove(v)
    if set(v_other_neighbours) == set(u_other_neighbours):
        return True
    return False


def check_neighbourhood_FT(G:"Graph", v: "Vertex", u: "Vertex"):
    if v.degree != u.degree:
        return False
    if G.is_adjacent(v,u):
        return False
    if set(v.neighbours) == set(u.neighbours):
        return True
    return False
from graph import *
from count_isomorphisms import count_isomorphism
from math import factorial


def count_automorphisms(G: "Graph"):
    multiplier = 1
    true_twins = calc_true_twins(G)
    false_twins = calc_false_twins(G)

    edges_to_destroy = set()
    vertices_to_destroy = set()

    coloring = {v: v.degree for v in G.vertices}

    offset = len(true_twins)

    for true_twin in true_twins:
        coloring[true_twin[0]] = len(true_twin)
        for v in true_twin[1:]:
            G.vertices[true_twin[0]].pop(G.vertices[v])
            for e in G.vertices[v].incidence:
                edges_to_destroy.add(e)
            vertices_to_destroy.add(G.vertices[v])
            coloring.pop(G.vertices[v])
    
    for false_twin in false_twins:
        coloring[false_twin[0]] = len(false_twin)+ offset
        for v in false_twin[1:]:
            for e in G.vertices[v].incidence:
                edges_to_destroy.add(e)
            vertices_to_destroy.add(G.vertices[v])
            coloring.pop(G.vertices[v])
    if len(edges_to_destroy) > 0:
        G._e = list(set(G._e).difference(edges_to_destroy))
    if len(vertices_to_destroy) > 0:
        G._v = list(set(G._v).difference(vertices_to_destroy))

    for true_twin in true_twins:
        multiplier*=factorial(len(true_twin))
    for false_twin in false_twins:
        multiplier*=factorial(len(false_twin))
    G_copy = G.copy()

    for i,v in enumerate(G_copy.vertices):
        coloring[v] = coloring[G.vertices[i]]

    result = count_isomorphism([],[],G, G_copy, coloring)
    
    return result*multiplier
        



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
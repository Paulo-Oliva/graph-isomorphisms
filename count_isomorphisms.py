from colour_ref import colour_refinement
from graph import Graph, Vertex



def count_isomorphism(D, I, G, H, alpha):
    # print("count_isomorphism(D={}, I={})".format(D, I))
    vertices = G.vertices + H.vertices

    alpha.update({v: -i - 1 for i, v in enumerate(D)})
    alpha.update({v: -i - 1 for i, v in enumerate(I)})

    vertices = [v for v in vertices if v not in D and v not in I]
    
    beta = colour_refinement(vertices, alpha)
    if not is_balanced(beta, G, H):
        return 0
    if is_bijection(beta, G, H):
        # print("+1: D={}, I={}".format(D, I))
        return 1
    # Choose a colour class C of beta with |C| ≥ 4
    C = pick_colour_class(beta)
    # Choose a vertex x ∈ C that belongs to G
    x = next(v for v in C if v in G and v not in D)
    num = 0
    # For each vertex y ∈ C that belongs to H
    for y in (v for v in C if v in H and v not in I):
        num = num + count_isomorphism(D + [x], I + [y], G, H, beta)
    return num

def check_isomorphism(D, I, G, H):
    # print("check_isomorphism(D={}, I={})".format(D, I))
    vertices = G.vertices + H.vertices

    alpha = {v: 0 for v in vertices}
    alpha.update({v: -i - 1 for i, v in enumerate(D)})
    alpha.update({v: -i - 1 for i, v in enumerate(I)})

    vertices = [v for v in vertices if v not in D and v not in I]
    
    beta = colour_refinement(vertices, alpha)
    if not is_balanced(beta, G, H):
        return 0
    if is_bijection(beta, G, H):
        # print("+1: D={}, I={}".format(D, I))
        return 1
    # Choose a colour class C of beta with |C| ≥ 4
    C = pick_colour_class(beta)
    # Choose a vertex x ∈ C that belongs to G
    x = next(v for v in C if v in G and v not in D)
    num = 0
    # For each vertex y ∈ C that belongs to H
    for y in (v for v in C if v in H and v not in I):
        if check_isomorphism(D + [x], I + [y], G, H) != 0:
            return 1
    return num


def pick_x(C, G, D):
    """
    Choose a vertex x ∈ C that belongs to G.

    Parameters:
    C (list): A list of vertices with the same colour.
    G (Graph): A graph.
    D (list): A list of vertices.

    Returns:
    Vertex: A vertex x ∈ C that belongs to G.
    """
    # Return the vertex with the highest degree in C that belongs to G and is not in D
    return max((v for v in C if v in G and v not in D), key=lambda v: v.degree)


def pick_y(C, H, I):
    """
    Choose a vertex y ∈ C that belongs to H.

    Parameters:
    C (list): A list of vertices with the same colour.
    H (Graph): A graph.
    I (list): A list of vertices.

    Returns:
    Vertex: A vertex y ∈ C that belongs to H.
    """
    # Return an iterator over all vertices in C that belong to H and are not in I ordered by degree in descending order
    return sorted((v for v in C if v in H and v not in I),
                  key=lambda v: v.degree,
                  reverse=True)


def colouring_to_colour_classes(colouring: dict):
    """
    Convert a colouring to a dictionary mapping each colour to a list of vertices
    with that colour.

    Parameters:
    colors (dict): A dictionary mapping each vertex to its color.

    Returns:
    dict: A dictionary mapping each colour to a list of vertices with that colour.
    """
    colour_classes = {}
    for v, c in colouring.items():
        if c not in colour_classes:
            colour_classes[c] = []
        colour_classes[c].append(v)
    return colour_classes


def pick_colour_class(colouring):
    """
    Pick a colour class of a colouring with at least 4 vertices.

    Parameters:
    colors (dict): A dictionary mapping each vertex to its color.

    Returns:
    list: A list of vertices with the same colour.
    """
    colour_classes = colouring_to_colour_classes(colouring)

    gen = (colour_classes[c] for c in colour_classes
           if len(colour_classes[c]) >= 4)

    colour_class = max(
        gen, key=lambda c: sorted([v.degree for v in c], reverse=True))

    return colour_class


def is_balanced(colouring, G, H):
    """
    Check if a coloring is balanced.

    Parameters:
    colors (dict): A dictionary mapping each vertex to its color.

    Returns:
    bool: True if the coloring is balanced, False otherwise.
    """
    # split the colouring into two colourings, one for each graph
    colouring_g1 = {v: colouring[v] for v in G}
    colouring_g2 = {v: colouring[v] for v in H}
    return sorted(colouring_g1.values()) == sorted(colouring_g2.values())


def is_bijection(colouring, G, H):
    """
    Check if a coloring is a bijection.

    Parameters:
    colors (dict): A dictionary mapping each vertex to its color.

    Returns:
    bool: True if the coloring is a bijection, False otherwise.
    """
    colouring_g1 = {v: colouring[v] for v in G}
    colouring_g2 = {v: colouring[v] for v in H}

    # Check if each colour is unique
    if len(set(colouring_g1.values())) != len(colouring_g1):
        return False
    if len(set(colouring_g2.values())) != len(colouring_g2):
        return False
    return True


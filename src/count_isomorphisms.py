"""
Contains the function to count the number of isomorphisms between two graphs.

Functions:
- count_isomorphism: Count the number of isomorphisms between two graphs.
- check_isomorphism: Check if two graphs are isomorphic.

"""
from .colour_ref import colour_refinement
from .graph import Graph, Vertex


def count_isomorphism(D: list[Vertex], I: list[Vertex], G: Graph, H: Graph,
                      alpha: dict[Vertex, int]) -> int:
    """
    Count the number of isomorphisms between G and H.

    This function is a recursive function that counts the number of
    isomorphisms between G and H using the branching algorithm
    described in the slides of the lecture.

    Args:
        D (list[Vertex]): The list of fixed vertices of G.
        I (list[Vertex]): The list of fixed vertices of H.
        G (Graph): The graph G.
        H (Graph): The graph H.
        alpha (dict[Vertex, int]): The current colouring of the vertices.

    Returns:
        int: The number of isomorphisms between G and H.
    """
    vertices = G.vertices + H.vertices

    alpha.update({v: -i - 1 for i, v in enumerate(D)})
    alpha.update({v: -i - 1 for i, v in enumerate(I)})

    vertices = [v for v in vertices if v not in D and v not in I]

    beta = colour_refinement(vertices, alpha)
    if not _is_balanced(beta, G, H):
        return 0
    if _is_bijection(beta, G, H):
        return 1
    # Choose a colour class C of beta with |C| >= 4
    C = _pick_colour_class(beta)
    # Choose a vertex x in C that belongs to G
    x = _pick_x(C, G, D)
    num = 0
    # For each vertex y in C that belongs to H
    for y in _pick_y(C, H, I):
        num = num + count_isomorphism(D + [x], I + [y], G, H, beta.copy())
    return num


def check_isomorphism(D: list[Vertex], I: list[Vertex], G: Graph, H: Graph,
                      alpha: dict[Vertex, int]) -> int:
    """
    Check if G and H are isomorphic.

    This function is a recursive function that checks if G and H are
    isomorphic based on the branching algorithm described in the slides
    of the lecture.

    Args:
        D (list[Vertex]): The list of fixed vertices of G.
        I (list[Vertex]): The list of fixed vertices of H.
        G (Graph): The graph G.
        H (Graph): The graph H.
        alpha (dict[Vertex, int]): The current colouring of the vertices.

    Returns:
        int: 1 if G and H are isomorphic, 0 otherwise.
    """
    vertices = G.vertices + H.vertices

    alpha.update({v: -i - 1 for i, v in enumerate(D)})
    alpha.update({v: -i - 1 for i, v in enumerate(I)})

    vertices = [v for v in vertices if v not in D and v not in I]

    beta = colour_refinement(vertices, alpha)
    if not _is_balanced(beta, G, H):
        return 0
    if _is_bijection(beta, G, H):
        return 1
    # Choose a colour class C of beta with |C| >= 4
    C = _pick_colour_class(beta)
    # Choose a vertex x in C that belongs to G
    x = _pick_x(C, G, D)
    num = 0
    # For each vertex y in C that belongs to H
    for y in _pick_y(C, H, I):
        if check_isomorphism(D + [x], I + [y], G, H, beta.copy()) != 0:
            return 1
    return num


def _pick_x(C, G, D):
    return next(v for v in C if v in G and v not in D)


def _pick_y(C, H, I):
    return (v for v in C if v in H and v not in I)


def _pick_colour_class(colouring: dict[Vertex, int]) -> list[Vertex]:
    colour_classes = _colouring_to_colour_classes(colouring)

    # Pick a colour class with at least 4 vertices
    gen = (colour_classes[c] for c in colour_classes
           if len(colour_classes[c]) >= 4)

    colour_class = max(
        gen, key=lambda c: sorted([v.degree for v in c], reverse=True))

    return colour_class


# TODO: can be optimized since we implemented fcr
def _colouring_to_colour_classes(
        colouring: dict[Vertex, int]) -> dict[int, list[Vertex]]:
    colour_classes = {}
    for vertex, colour in colouring.items():
        if colour not in colour_classes:
            colour_classes[colour] = []
        colour_classes[colour].append(vertex)
    return colour_classes


def _is_balanced(colouring: dict[Vertex, int], G: Graph, H: Graph) -> bool:
    # split the colouring into two colourings, one for each graph
    colouring_g1 = {v: colouring[v] for v in G}
    colouring_g2 = {v: colouring[v] for v in H}
    return sorted(colouring_g1.values()) == sorted(colouring_g2.values())


def _is_bijection(colouring: dict[Vertex, int], G: Graph, H: Graph) -> bool:
    colouring_g1 = {v: colouring[v] for v in G}
    colouring_g2 = {v: colouring[v] for v in H}
    # Check if each colour is unique
    if len(set(colouring_g1.values())) != len(colouring_g1):
        return False
    if len(set(colouring_g2.values())) != len(colouring_g2):
        return False
    return True

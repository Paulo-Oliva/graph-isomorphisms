"""
This module contains implementations of the colour refinement algorithm.

Functions:
- colour_refinement_normal: Refines the colouring of a graph using the
    standard colour refinement algorithm.
- colour_refinement: Refines the colouring of a graph using the
    fast colour refinement algorithm.
"""

from collections import deque

from .doubly_linked_list import DoublyLinkedList, Node
from .graph import Graph, Vertex


def colour_refinement_normal(
        vertices: list[Vertex], colouring: dict[Vertex,
                                                int]) -> dict[Vertex, int]:
    """
    Refine the colouring of a graph using the standard colour refinement.

    This function implements the colour refinement algorithm described in
    the slides of the lecture. The main difference is that this function
    takes a list of vertices instead of the graph itself.

    Args:
        vertices (list[Vertex]): A list of the vertices of the graph(s).
        colouring (dict[Vertex, int]): A dictionary mapping each vertex to a
            colour represented by a number.

    Returns:
        dict[Vertex, int]: A dictionary mapping each vertex to a colour
            represented by a number.
    """
    while True:
        colour = 0
        # Create a copy of the colouring
        new_colouring = colouring.copy()
        # Dictionary that maps a tuple of colours to a colour
        neighbours_to_colour = {}

        for vertex in vertices:
            # Get the neighbours of the current vertex
            neighbours = vertex.neighbours
            # Get the colours of the neighbours as a sorted tuple
            neighbour_colours = tuple(
                sorted([colouring[n] for n in neighbours]))
            # If the colours of the neighbours are not in the dictionary yet
            if neighbour_colours not in neighbours_to_colour:
                # Add them and increment the colour
                neighbours_to_colour[neighbour_colours] = colour
                colour += 1
            # Assign the correct colour to the current vertex
            new_colouring[vertex] = neighbours_to_colour[neighbour_colours]

        # Check if the colouring has changed
        if new_colouring == colouring:
            break

        # Update the colouring
        colouring = new_colouring
    # When the algorithm is finished, return the colouring
    return colouring


def are_isomorphic(g1: Graph, g2: Graph) -> tuple[bool, bool]:
    """
    Check if two graphs are isomorphic.

    This function is no longer used in the project. It is kept here for
    proof of work from the first assignment.

    Args:
        g1 (Graph): The first graph.
        g2 (Graph): The second graph.

    Returns:
        tuple[bool, bool]: A tuple containing two booleans. The first boolean
            indicates if the graphs are isomorphic. The second boolean
            indicates if the colouring is discrete colouring.
    """
    # If the graphs have a different number of vertices or edges
    if len(g1.vertices) != len(g2.vertices) or len(g1.edges) != len(g2.edges):
        return False, False

    # Run the colour refinement algorithm on both graphs vertices
    # at the same time
    vertices = g1.vertices + g2.vertices

    alpha = {v: v.degree for v in vertices}
    colouring = colour_refinement_normal(vertices, alpha)

    # Separate the colouring into two colourings, one for each graph
    colouring_g1 = {v: colouring[v] for v in g1.vertices}
    colouring_g2 = {v: colouring[v] for v in g2.vertices}

    # Check if both graphs have the same colouring (i.e. bijection)
    if not sorted(colouring_g1.values()) == sorted(colouring_g2.values()):
        return False, False

    # Check if the degrees are the same
    degrees_g1 = sorted([len(v.neighbours) for v in g1.vertices])
    degrees_g2 = sorted([len(v.neighbours) for v in g2.vertices])
    if degrees_g1 != degrees_g2:
        return False, False

    return True, is_discrete_colouring(colouring_g1)


def is_discrete_colouring(colouring: dict[Vertex, int]) -> bool:
    """
    Check if a colouring is a discrete.

    Args:
        colouring (dict[Vertex, int]): A dictionary mapping each vertex to a
            colour represented by a number.

    Returns:
        bool: A boolean indicating if the colouring is discrete.
    """
    colour_amount = len(set(colouring.values()))
    vertex_amount = len(colouring.keys())
    # The colouring is discrete if the number of colours is equal to the
    # number of vertices
    return colour_amount == vertex_amount


# TODO: Remove the unused argument in the future
def colour_refinement(_, colouring: dict[Vertex, int]) -> dict[Vertex, int]:
    """
    Refine the colouring of a graph using fast colour refinement.

    Args:
        _ : Unused argument, only here to preserve the same function signature
            as the old colour refinement function.
        colouring (dict[Vertex, int]): A dictionary mapping each vertex of the
            graph to a colour represented by a number. In a initial case, this
            colouring should be based on the degree of the vertices.

    Returns:
        dict[Vertex, int]: The refined colouring of the graph, based on the
            colouring given as input.
    """
    colour_classes, vertex_to_node = _create_colour_and_vertex_dicts(colouring)

    # We cannot refine the colouring if there is only one colour class
    if len(colour_classes) == 1:
        return colouring

    queue = deque()
    # Append all colour classes to the queue in decreasing order of size
    for colour in sorted(colour_classes,
                         key=lambda c: len(colour_classes[c]),
                         reverse=True):
        queue.append(colour)

    in_queue = {c: True for c in colour_classes}

    new_colour = max(colour_classes.keys())

    while queue:
        # Pop the first colour class from the queue
        c = queue.popleft()
        in_queue[c] = False

        # Compute the adjacent colour classes
        L = set()
        A = {}
        for vertex in colour_classes[c]:
            neighbours = vertex.neighbours
            for n in neighbours:
                colour_of_n = colouring[n]
                L.add(colour_of_n)
                if A.get(colour_of_n) is None:
                    A[colour_of_n] = {n}
                else:
                    A[colour_of_n].add(n)
        # For each adjacent colour class, check if it should be split
        for i in L:
            if i < 0:
                continue
            if len(A[i]) < len(colour_classes[i]):
                # Create a new colour class
                new_colour += 1
                colour_classes[new_colour] = DoublyLinkedList()
                # Move the vertices from the old colour class to the new one
                for vertex in A[i]:
                    node = vertex_to_node[vertex]
                    colour_classes[i].remove(node)
                    colour_classes[new_colour].append_node(node)
                    colouring[vertex] = new_colour
                # Update the queue
                if in_queue[i]:
                    queue.append(new_colour)
                    in_queue[new_colour] = True
                else:
                    if len(colour_classes[i]) < len(
                            colour_classes[new_colour]):
                        queue.append(i)
                        in_queue[i] = True
                        in_queue[new_colour] = False
                    else:
                        queue.append(new_colour)
                        in_queue[new_colour] = True
    return colouring


def _create_colour_and_vertex_dicts(
    colouring: dict[Vertex, int]
) -> tuple[dict[int, DoublyLinkedList], dict[Vertex, Node]]:
    """
    Create 2 dictionaries for further use in the fast colour ref. algorithm.

    The 1st dictionary maps each colour to a doubly linked list of vertices
    with that colour. The 2nd dictionary maps each vertex to the node in the
    doubly linked list that contains that vertex.

    Args:
        colouring (dict[Vertex, int]): The colouring of the graph.

    Returns:
        tuple[dict[int, DoublyLinkedList], dict[Vertex, Node]]: A tuple
            containing the 2 dictionaries.
    """
    colour_classes: dict[int, DoublyLinkedList] = {}
    vertex_to_node: dict[Vertex, Node] = {}

    for vertex, colour in colouring.items():
        if colour not in colour_classes:
            colour_classes[colour] = DoublyLinkedList()
        node = colour_classes[colour].append_vertex(vertex)
        vertex_to_node[vertex] = node
    return colour_classes, vertex_to_node

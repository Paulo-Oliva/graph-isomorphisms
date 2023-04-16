"""
This module contains an implementation of the colour refinement algorithm
and a function to check if two graphs are isomorphic.
"""

from collections import deque

from doubly_linked_list import DoublyLinkedList, Node
from graph import Graph, Vertex


def create_colours_to_vertices_dict(
        colouring: dict[Vertex, int]) -> dict[int, set[Vertex]]:
    colours_to_vertices_dict = {}
    for v, col in colouring.items():
        if col not in colours_to_vertices_dict.keys():
            colours_to_vertices_dict[col] = {v}
        else:
            colours_to_vertices_dict[col].add(v)
    return colours_to_vertices_dict


def colour_refinement_old(vertices: list[Vertex],
                          colouring: dict[Vertex, int]) -> dict[Vertex, int]:
    """
    This function implements the colour refinement algorithm described in`
    the slides of the lecture. The main difference is that this function
    takes a list of vertices instead of a graph, instead of the graph itself.
    This allows us to run the algorithm on two graphs at the same time more
    easily, and thus, check if they are isomorphic.

    Args:
        vertices (list[Vertex]): A list of the vertices of the graph(s).

    Returns:
        dict[Vertex, int]: A dictionary mapping each vertex to a colour
            represented by a number.
    """
    while True:
        colour = 0
        # Create a new dictionary to store the colours and add all the vertices to it
        new_colouring = colouring.copy()
        # This dictionary maps the colours of the neighbours of a vertex
        # to a new colour
        neighbours_to_colour = {}

        for v in vertices:
            # Get the neighbours of the current vertex
            neighbours = v.neighbours
            # Get the colours of the neighbours as a sorted tuple
            neighbour_colours = tuple(
                sorted([colouring[n] for n in neighbours]))
            # If the colours of the neighbours are not in the dictionary yet
            if neighbour_colours not in neighbours_to_colour:
                # Add them and increment the colour
                neighbours_to_colour[neighbour_colours] = colour
                colour += 1
            # Assign the correct colour to the current vertex
            new_colouring[v] = neighbours_to_colour[neighbour_colours]

        # Check if the colouring has changed
        if new_colouring == colouring:
            break

        # Update the colouring
        colouring = new_colouring
    # When the algorithm is finished, return the colouring
    return colouring


def are_isomorphic(g1: Graph, g2: Graph) -> tuple[bool, bool]:
    """
    This function checks if two graphs are isomorphic.
    To do so, it checks if the vertices, edges and degrees are preserved
    between the two graphs checks if there's a bijection between the
    colourings of the two graphs using the colour refinement algorithm.

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
    colouring = colour_refinement(vertices, alpha)

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
    This function checks if a colouring is a discrete.

    Args:
        colouring (dict[Vertex, int]): A dictionary mapping each vertex to a
            colour represented by a number.

    Returns:
        bool: A boolean indicating if the colouring is discrete.
    """
    # Get the number of colours and vertices in the colouring
    colour_amount = len(set(colouring.values()))
    vertex_amount = len(colouring.keys())
    # Return whether the number of colours is equal to the number of vertices
    return colour_amount == vertex_amount


def colour_refinement(_, colouring: dict[Vertex, int]) -> dict[Vertex, int]:

    colour_classes, vertex_to_node = create_colour_and_vertex_dicts(colouring)

    if len(colour_classes) == 1:
        return colouring

    queue = deque()
    # Append all colour classes to the queue in decreasing order of size
    for c in sorted(colour_classes,
                    key=lambda c: len(colour_classes[c]),
                    reverse=True):
        queue.append(c)

    in_queue = {c: True for c in colour_classes}

    l = max(colour_classes.keys())

    while queue:
        # Pop the first colour class from the queue
        C = queue.popleft()
        in_queue[C] = False
        # print("Popped colour class", C, "from queue")

        # Compute the adjacent colour classes
        L = set()
        A = {}
        for v in colour_classes[C]:
            neighbours = v.neighbours
            for n in neighbours:
                colour_of_n = colouring[n]
                L.add(colour_of_n)
                if A.get(colour_of_n) == None:
                    A[colour_of_n] = {n}
                else:
                    A[colour_of_n].add(n)

        for i in L:
            if i < 0:
                continue
            if len(A[i]) < len(colour_classes[i]):
                l += 1
                colour_classes[l] = DoublyLinkedList()
                # print("Splitting up colour class", i, "into", i, "and", l)

                for v in A[i]:
                    node = vertex_to_node[v]
                    colour_classes[i].remove(node)
                    colour_classes[l].append_node(node)
                    colouring[v] = l

                # If i in Queue: add l to the queue.
                if in_queue[i]:
                    queue.append(l)
                    in_queue[l] = True
                # If i not in Queue: add either i or l to the queue, depending on which of the new color classes is the smallest.
                else:
                    if len(colour_classes[i]) < len(colour_classes[l]):
                        queue.append(i)
                        in_queue[i] = True
                        in_queue[l] = False
                    else:
                        queue.append(l)
                        in_queue[l] = True
    return colouring


def create_colour_and_vertex_dicts(
    colouring: dict[Vertex, int]
) -> tuple[dict[int, DoublyLinkedList], dict[Vertex, Node]]:
    colour_classes: dict[int, DoublyLinkedList] = {}
    vertex_to_node: dict[Vertex, Node] = {}
    for v, c in colouring.items():
        if c not in colour_classes:
            colour_classes[c] = DoublyLinkedList()
        n = colour_classes[c].append_vertex(v)
        vertex_to_node[v] = n
    return colour_classes, vertex_to_node

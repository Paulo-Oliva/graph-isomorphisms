"""
This module contains an implementation of the colour refinement algorithm
and a function to check if two graphs are isomorphic.
"""
# Paulo Oliva

from graph import Graph, Vertex


def colour_refinement(vertices: list[Vertex],
                      colouring: dict[Vertex, int]) -> dict[Vertex, int]:
    """
    This function implements the colour refinement algorithm described in
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

    # print("Initial colouring: ", colouring)

    while True:
        colour = 0
        # print("\nStarting new iteration")
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

        # print("Checking if the colouring has changed")

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

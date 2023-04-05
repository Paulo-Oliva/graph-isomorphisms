"""
This module contains an implementation of the colour refinement algorithm
and a function to check if two graphs are isomorphic.
"""
# Paulo Oliva

from graph import Graph, Vertex


def colour_refinement(vertices: list[Vertex],
                      colouring: dict[Vertex, int]) -> dict[Vertex, int]:
    
    colours_to_vertices_dict = create_colours_to_vertices_dict(colouring)

    # standarise colours such that colours occur consequatively v very important
    min_colour = min(colours_to_vertices_dict.keys())
    min_colour_initially = min_colour
    max_colour = max(colours_to_vertices_dict.keys())
    # is_colour_in_queue = {col : True for col in colours_to_vertices_dict.keys()}
    queue = list(colours_to_vertices_dict.keys())
    while len(queue) > 0:
        refining_colour = queue.pop(0)
        vertices_with_refining_colour = colours_to_vertices_dict[refining_colour]
        new_colouring = colouring.copy()
        prev_max_colour = max_colour
        for colour in range(min_colour, max_colour+1):
            
            vertices = colours_to_vertices_dict[colour]
            number_of_neighbours_to_colour_dict = {}
            biggest_colour_class = None
            len_biggest_colour_class = 0
            colour_to_number_of_vertices_currently = {}
            vertex_to_number_dict = {}
            # refine_on_colour
            for v in vertices:
                number =  len(set(v.neighbours).intersection(vertices_with_refining_colour))
                vertex_to_number_dict[v] = number
                if number not in number_of_neighbours_to_colour_dict.keys():
                    max_colour+=1
                    number_of_neighbours_to_colour_dict[number] = max_colour
                    colours_to_vertices_dict[max_colour] = {v}
                    colour_to_number_of_vertices_currently[max_colour] = 1
                    if biggest_colour_class == None:
                        biggest_colour_class = max_colour
                        len_biggest_colour_class = 1
                    new_colouring[v] = max_colour
                else:
                    this_colour = number_of_neighbours_to_colour_dict[number]
                    colour_to_number_of_vertices_currently[this_colour] += 1
                    colours_to_vertices_dict[this_colour].add(v)
                    if colour_to_number_of_vertices_currently[this_colour] > len_biggest_colour_class:
                        biggest_colour_class = this_colour
                        len_biggest_colour_class = colour_to_number_of_vertices_currently[this_colour]
                    new_colouring[v] = this_colour
            for new_colour in set(number_of_neighbours_to_colour_dict.values()): # new min_colour and max_colour range
                if new_colour != biggest_colour_class:
                    queue.insert(0,new_colour)
        min_colour = prev_max_colour + 1
        colouring = new_colouring
    
    for v in colouring:
        colouring[v] -= (min_colour-min_colour_initially)
            
    return colouring


def create_colours_to_vertices_dict(colouring: dict[Vertex, int]) -> dict[int, set[Vertex]]:
    colours_to_vertices_dict = {}
    for v, col in colouring.items():
        if col not in colours_to_vertices_dict.keys():
            colours_to_vertices_dict[col] = {v}
        else:
            colours_to_vertices_dict[col].add(v)
    return colours_to_vertices_dict
    

def colour_refinement_1(vertices: list[Vertex],
                      colouring: dict[Vertex, int]) -> dict[Vertex, int]:
    """
    This function implements the colour refinement algorithm described in`
    the slides of the lecture. The main difference is that this function
    takes a list of vertices instead of a graph, instead of the graph itself.
    This allows us to run the algorithm on two graphs at the same time more
    easily, and thus, check if they are isomorphic.
`
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

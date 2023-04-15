"""
This module contains an implementation of the colour refinement algorithm
and a function to check if two graphs are isomorphic.
"""

from collections import deque

from doubly_linked_list import DoublyLinkedList, Node
from graph import Edge, Graph, Vertex
from graph_io import load_graph


def colour_refinement__(vertices: list[Vertex],
                        colouring: dict[Vertex, int]) -> dict[Vertex, int]:
    # Create a dictionary that maps colours to the vertices that have that colour
    colours_to_vertices_dict = create_colours_to_vertices_dict(colouring)
    # Standardize the colours so that the colours are 1, 2, 3, ...
    min_colour = min(colours_to_vertices_dict.keys())
    min_colour_initially = min_colour
    max_colour = max(colours_to_vertices_dict.keys())
    # Create a queue of colours to refine on
    queue = list(colours_to_vertices_dict.keys())
    # While there are still colours to refine on
    while len(queue) > 0:
        # Get the next colour to refine on
        refining_colour = queue.pop(0)
        # Get the vertices that have that colour
        vertices_with_refining_colour = colours_to_vertices_dict[
            refining_colour]
        # Create a new colouring
        new_colouring = colouring.copy()
        prev_max_colour = max_colour
        # For each colour in the colouring
        for colour in range(min_colour, max_colour + 1):
            # Get the vertices that have that colour
            vertices = colours_to_vertices_dict[colour]
            # Initialise the dictionary that maps the number of neighbours of a vertex to the colour of that vertex
            number_of_neighbours_to_colour_dict = {}
            biggest_colour_class = None
            len_biggest_colour_class = 0
            # Initialise the dictionary that maps the colour to the number of vertices that have that colour
            colour_to_number_of_vertices_currently = {}
            vertex_to_number_dict = {}
            # For each vertex in the vertices that have the colour
            for v in vertices:
                # Get the number of neighbours of that vertex that have the refining colour
                number = len(
                    set(v.neighbours).intersection(
                        vertices_with_refining_colour))
                # Add the number to the dictionary
                vertex_to_number_dict[v] = number
                # If the number is not in the dictionary that maps the number of neighbours to the colour
                if number not in number_of_neighbours_to_colour_dict.keys():
                    # Create a new colour
                    max_colour += 1
                    number_of_neighbours_to_colour_dict[number] = max_colour
                    # Add the vertex to the dictionary that maps the colour to the vertices that have that colour
                    colours_to_vertices_dict[max_colour] = {v}
                    colour_to_number_of_vertices_currently[max_colour] = 1
                    # If the biggest colour class is None, set it to the new colour
                    if biggest_colour_class == None:
                        biggest_colour_class = max_colour
                        len_biggest_colour_class = 1
                    # Set the colour of the vertex to the new colour
                    new_colouring[v] = max_colour
                # If the number is in the dictionary that maps the number of neighbours to the colour
                else:
                    this_colour = number_of_neighbours_to_colour_dict[number]
                    colour_to_number_of_vertices_currently[this_colour] += 1
                    colours_to_vertices_dict[this_colour].add(v)
                    # If the number of vertices that have the colour is bigger than the biggest colour class
                    # Set the biggest colour class to the new colour
                    if colour_to_number_of_vertices_currently[
                            this_colour] > len_biggest_colour_class:
                        biggest_colour_class = this_colour
                        len_biggest_colour_class = colour_to_number_of_vertices_currently[
                            this_colour]
                    # Set the colour of the vertex to the colour
                    new_colouring[v] = this_colour
            # For each colour in the dictionary that maps the number of neighbours to the colour
            for new_colour in set(
                    number_of_neighbours_to_colour_dict.values()):
                # If the colour is not the biggest colour class
                if new_colour != biggest_colour_class:
                    # Add the colour to the queue
                    queue.append(new_colour)
        # Set the colouring to the new colouring
        min_colour = prev_max_colour + 1
        colouring = new_colouring
    # Standardize the colours so that the colours are 1, 2, 3, ...
    for v in colouring:
        colouring[v] -= (min_colour - min_colour_initially)
    return colouring


def create_colours_to_vertices_dict(
        colouring: dict[Vertex, int]) -> dict[int, set[Vertex]]:
    colours_to_vertices_dict = {}
    for v, col in colouring.items():
        if col not in colours_to_vertices_dict.keys():
            colours_to_vertices_dict[col] = {v}
        else:
            colours_to_vertices_dict[col].add(v)
    return colours_to_vertices_dict


def colour_refinement(vertices: list[Vertex],
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


def colour_refinement(vertices: list[Vertex],
                      colouring: dict[Vertex, int]) -> dict[Vertex, int]:
    colour_classes, vertex_to_node = colouring_to_colour_classes_and_vertex_to_node(
        colouring)
    adjacency_list = create_adjacency_list(vertices)
    # Initialize queue with the first colour class
    queue = deque()
    queue.append(max(colour_classes.keys()))

    # a boolean variable InQueue[i] that indicates whether color i is in Queue
    in_queue = [False] * len(colour_classes)
    in_queue[0] = True

    while queue:
        # Pop the first colour class from the queue
        C = queue.popleft()
        # In time O(t), loop over all vertices in the colour class and vertices that are adjacent to them
        # and compute A list L of all colors i such that Ci contains a vertex adjacent to a vertex in C
        # The number A[i] of such states in Ci is also computed
        L = set()
        A = {}
        for v in colour_classes[C]:
            neighbours = adjacency_list[v]
            for n in neighbours:
                L.add(colouring[n])
                if colouring[n] not in A:
                    A[colouring[n]] = 1
                else:
                    A[colouring[n]] += 1

        # In time O(|L|) ≤ O(t), loop over L and compute:
        # • for each i ∈ L: whether Ci should split up (whether A[i] < |Ci|).
        # • if so, choose a new color l, and update Queue by adding i or l.
        # Whenever a refining operation splits a color class Ci into two new classes: One of them keeps color i, and the other receives the smallest unused color l
        # • If i in Queue: add l to the queue.
        # • If i not in Queue: add either i or l to the queue, depending on which of the new color classes is the smallest.
        for i in L:
            if A[i] < len(colour_classes[i]):
                l = len(colour_classes)
                colour_classes[l] = DoublyLinkedList()
                print("Splitting up colour class", i, "into", i, "and", l)

                # Split up the colour class
                for v in colour_classes[i]:
                    if colouring[v] == i:
                        if A[i] > 0:
                            colour_classes[i].remove(vertex_to_node[v])
                            colour_classes[l].append(v)
                            A[i] -= 1
                        else:
                            colour_classes[i].remove(vertex_to_node[v])
                            colour_classes[i].append(v)
                    else:
                        colour_classes[l].append(v)

                # Update the colouring
                for v in colour_classes[l]:
                    colouring[v] = l

                # Update the queue
                if in_queue[i]:
                    queue.append(l)
                    in_queue[l] = True
                else:
                    if len(colour_classes[i]) < len(colour_classes[l]):
                        queue.append(i)
                        in_queue[i] = True
                    else:
                        queue.append(l)
                        in_queue[l] = True
    return colouring


def create_adjacency_list(
        vertices: list[Vertex]) -> dict[Vertex, DoublyLinkedList]:
    adjacency_list: dict[Vertex, DoublyLinkedList] = {}
    for v in vertices:
        adjacency_list[v] = DoublyLinkedList()
        for n in v.neighbours:
            adjacency_list[v].append(n)
    return adjacency_list


def colouring_to_colour_classes_and_vertex_to_node(
    colouring: dict[Vertex, int]
) -> tuple[dict[int, DoublyLinkedList], dict[Vertex, Node]]:
    colour_classes: dict[int, DoublyLinkedList] = {}
    vertex_to_node: dict[Vertex, Node] = {}
    for v, c in colouring.items():
        if c not in colour_classes:
            colour_classes[c] = DoublyLinkedList()
        n = colour_classes[c].append(v)
        vertex_to_node[v] = n
    return colour_classes, vertex_to_node


if __name__ == "__main__":
    G = Graph(directed=False, n=5)
    G.add_edge(edge=Edge(G.vertices[0], G.vertices[1]))
    G.add_edge(edge=Edge(G.vertices[0], G.vertices[2]))
    G.add_edge(edge=Edge(G.vertices[0], G.vertices[3]))
    G.add_edge(edge=Edge(G.vertices[0], G.vertices[4]))

    print(colour_refinement(G.vertices, {v: 0 for v in G.vertices}))

    # with open("cr_tests/cref9vert_4_9.grl", "r") as f:
    #     graphs = load_graph(f, read_list=True)
    #     G = graphs[0][0]
    #     print(colour_refinement(G.vertices, {v: 0 for v in G.vertices}))
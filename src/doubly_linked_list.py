"""
This module contains the implementation of a doubly linked list.

Classes:
    - Node: A node of a doubly linked list.
    - DoublyLinkedList: A doubly linked list implementation for the vertices
        of a graph.
"""

from .graph import Vertex


class Node:
    """
    A node of a doubly linked list.

    Attributes:
        data: The data of the node.
        next: The next node in the list.
        prev: The previous node in the list.
    """

    def __init__(self, data: Vertex):
        self.data = data
        self.next: Node | None = None
        self.prev: Node | None = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self)


class DoublyLinkedList:
    """
    A doubly linked list implementation for the vertices of a graph.

    Attributes:
        head: The head of the list.
        tail: The tail of the list.
        size: The size of the list.
    """

    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size = 0

    def append_vertex(self, data: Vertex) -> Node:
        """
        Append a vertex to the list.

        This method also returns the node containing the vertex that was
        appended.

        Args:
            data (Vertex): The vertex to be appended.

        Returns:
            Node: The node containing the vertex that was appended.
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

        return new_node

    def append_node(self, node: Node):
        """
        Append a node to the list.

        Args:
            node (Node): The node to be appended.
        """
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.size += 1

    def remove(self, node: Node):
        """
        Remove a node from the list.

        The removed node also has its prev and next attributes set to None.

        Args:
            node (Node): The node to be removed.
        """
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        node.prev = None
        node.next = None

        self.size -= 1

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.next

    def __len__(self):
        return self.size

    def __str__(self):
        return str(list(iter(self)))

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return list(iter(self)) == list(iter(other))

    def __ne__(self, other):
        return not self == other

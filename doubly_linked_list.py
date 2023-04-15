from graph import Vertex


class Node:

    def __init__(self, data: Vertex):
        self.data = data
        self.next: Node | None = None
        self.prev: Node | None = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self)


class DoublyLinkedList:

    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def append(self, data: Vertex):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        # return a pointer to the new node
        return new_node

    def append_node(self, node: Node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def remove(self, node: Node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
            
        node.next = None
        node.prev = None

    def is_empty(self):
        return self.head is None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.next

    def __len__(self):
        return len(list(iter(self)))

    def __str__(self):
        return str(list(iter(self)))

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return list(iter(self)) == list(iter(other))

    def __ne__(self, other):
        return not self == other

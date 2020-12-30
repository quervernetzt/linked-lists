class Node:
    def __init__(self, value: object) -> None:
        """
        Constructor.
        """
        self.value: object = value
        self.next: object = None

    def __repr__(self: object) -> str:
        """
        Returns the value of the node as string.

        Returns
        ----------
        str
            Returns the value of the node as string.
        """
        return str(self.value)


class LinkedList:
    def __init__(self: object) -> None:
        """
        Constructor.
        """
        self.head = None

    def append(self: object, value: object) -> None:
        """
        Append a node to the linked list.

        Parameters
        ----------
        value: object, required
            The value of the node that is being appended.
        """
        if self.head is None:
            self.head: Node = Node(value)
            return

        node: Node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self: object) -> int:
        """
        Return the size or length of the linked list.

        Returns
        ----------
        int
            The size of the linked list.
        """
        size: int = 0
        current_node: Node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    def __str__(self: object) -> str:
        """
        Create a string representation of the linked list.

        Returns
        ----------
            Returns a string representation of the linked list.
        """
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string[:-3]

    def to_list(self: object) -> list:
        """
        Create a list representation of the linked list.

        Returns
        ----------
        list
            A list representation of the linked list.
        """
        result_list: list = list()
        if self.head is not None:
            node: Node = self.head
            while node:
                result_list.append(node.value)
                node = node.next

        return result_list

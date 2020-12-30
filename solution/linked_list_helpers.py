from solution.linked_list import LinkedList, Node


class LinkedListHelpers(object):
    def __init__(self: object) -> None:
        """
        Constructor.
        """
        pass

    def intersection(
            self: object,
            llist_1: LinkedList,
            llist_2: LinkedList) -> LinkedList:
        """
        Get all elements distinct that are in both linked lists.
        As there is no prescribed order sets are used what also results in an unordered, resulting linked list.

        Parameters
        ----------
        llist_1: LinkedList, required
            The first linked list.

        llist_2: LinkedList, required
            The second linked list.

        Returns
        ----------
        LinkedList
            All distinct elements that are in both lists as a single linked list.
            If one of the lists or both is / are None then None is returned.
        """
        if not llist_1 or not llist_2:
            #print("At least one of the linked lists is None...")
            return
        else:
            #print("Both lists are not None...")
            node_value_set_1: set = set()
            node_value_set_intersection: set = set()

            # Go through list 1 and add all to set
            current_node_1: Node = llist_1.head
            while current_node_1:
                node_value_set_1.add(current_node_1.value)
                current_node_1 = current_node_1.next

            # Go through list 2 and add to a second set if in first set
            current_node_2: Node = llist_2.head
            while current_node_2:
                if current_node_2.value in node_value_set_1:
                    node_value_set_intersection.add(current_node_2.value)
                current_node_2 = current_node_2.next

            # Then create linked list
            result_linked_list: LinkedList = LinkedList()
            for value in node_value_set_intersection: 
                result_linked_list.append(value)

            return result_linked_list

    def union(
            self: object,
            llist_1: LinkedList,
            llist_2: LinkedList) -> LinkedList:
        """
        Get all elements distinct from both linked lists.
        As there is no prescribed order sets are used what also results in an unordered, resulting linked list.

        Parameters
        ----------
        llist_1: LinkedList, required
            The first linked list.

        llist_2: LinkedList, required
            The second linked list.

        Returns
        ----------
        LinkedList
            All distinct elements from both lists as a single linked list.
            If one of the lists or both is / are None then None is returned.
        """

        if not llist_1 or not llist_2:
            #print("At least one of the linked lists is None...")
            return
        else:
            #print("Both lists are not None...")
            node_value_set: set = set()

            # Get values from first linked list
            current_node_1: Node = llist_1.head
            while current_node_1:
                node_value_set.add(current_node_1.value)
                current_node_1 = current_node_1.next

            # Get values from second linked list
            current_node_2: Node = llist_2.head
            while current_node_2:
                node_value_set.add(current_node_2.value)
                current_node_2 = current_node_2.next

            # Create new linked list
            result_linked_list: LinkedList = LinkedList()
            for value in node_value_set:
                result_linked_list.append(value)

            return result_linked_list

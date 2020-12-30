import unittest
from solution.linked_list import LinkedList
from solution.linked_list_helpers import LinkedListHelpers


class TestCasesLinkedListHelpers(unittest.TestCase):
    def execute_tests_both_linked_lists_none(self: object) -> None:
        # Arrange
        linked_list_helpers: LinkedListHelpers = LinkedListHelpers()
        linked_list_1: LinkedList = None
        linked_list_2: LinkedList = None

        # Act
        result_union: LinkedList = linked_list_helpers.union(
            linked_list_1, linked_list_2)
        result_intersection: LinkedList = linked_list_helpers.intersection(
            linked_list_1, linked_list_2)

        # Assert
        self.assertIsNone(result_union)
        self.assertIsNone(result_intersection)

    def execute_tests_both_linked_lists_first_is_none(self: object) -> None:
        # Arrange
        linked_list_helpers: LinkedListHelpers = LinkedListHelpers()
        linked_list_1: LinkedList = None

        linked_list_2: LinkedList = LinkedList()
        element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
        for i in element_2:
            linked_list_2.append(i)

        # Act
        result_union: LinkedList = linked_list_helpers.union(
            linked_list_1, linked_list_2)
        result_intersection: LinkedList = linked_list_helpers.intersection(
            linked_list_1, linked_list_2)

        # Assert
        self.assertIsNone(result_union)
        self.assertIsNone(result_intersection)

    def execute_tests_both_linked_lists_second_is_none(self: object) -> None:
        # Arrange
        linked_list_helpers: LinkedListHelpers = LinkedListHelpers()
        linked_list_1: LinkedList = LinkedList()
        element_1 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
        for i in element_1:
            linked_list_1.append(i)

        linked_list_2: LinkedList = None

        # Act
        result_union: LinkedList = linked_list_helpers.union(
            linked_list_1, linked_list_2)
        result_intersection: LinkedList = linked_list_helpers.intersection(
            linked_list_1, linked_list_2)

        # Assert
        self.assertIsNone(result_union)
        self.assertIsNone(result_intersection)

    def execute_tests_both_linked_lists_both_empty_lists(self: object) -> None:
        # Arrange
        linked_list_helpers: LinkedListHelpers = LinkedListHelpers()
        linked_list_1: LinkedList = LinkedList()
        linked_list_2: LinkedList = LinkedList()

        # Act
        result_union: LinkedList = linked_list_helpers.union(
            linked_list_1, linked_list_2)
        result_intersection: LinkedList = linked_list_helpers.intersection(
            linked_list_1, linked_list_2)

        # Assert
        self.assertEqual(result_union.size(), 0)
        self.assertEqual(result_intersection.size(), 0)

    def execute_tests_both_linked_lists_first_empty_list(self: object) -> None:
        # Arrange
        linked_list_helpers: LinkedListHelpers = LinkedListHelpers()
        linked_list_1: LinkedList = LinkedList()

        linked_list_2: LinkedList = LinkedList()
        element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
        for i in element_2:
            linked_list_2.append(i)

        # Act
        result_union: LinkedList = linked_list_helpers.union(
            linked_list_1, linked_list_2)
        result_intersection: LinkedList = linked_list_helpers.intersection(
            linked_list_1, linked_list_2)

        # Assert
        result_union_list: list = sorted(result_union.to_list())
        result_intersection_list: list = sorted(result_intersection.to_list())

        self.assertEqual(result_union.size(), 7)
        self.assertListEqual(result_union_list, [1, 4, 6, 9, 11, 21, 32])
        self.assertEqual(result_intersection.size(), 0)
        self.assertListEqual(result_intersection_list, [])

    def execute_tests_both_linked_lists_second_empty_list(self: object) -> None:
        # Arrange
        linked_list_helpers: LinkedListHelpers = LinkedListHelpers()
        linked_list_1: LinkedList = LinkedList()
        element_1 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
        for i in element_1:
            linked_list_1.append(i)

        linked_list_2: LinkedList = LinkedList()

        # Act
        result_union: LinkedList = linked_list_helpers.union(
            linked_list_1, linked_list_2)
        result_intersection: LinkedList = linked_list_helpers.intersection(
            linked_list_1, linked_list_2)

        # Assert
        result_union_list: list = sorted(result_union.to_list())
        result_intersection_list: list = sorted(result_intersection.to_list())

        self.assertEqual(result_union.size(), 7)
        self.assertListEqual(result_union_list, [1, 4, 6, 9, 11, 21, 32])
        self.assertEqual(result_intersection.size(), 0)
        self.assertListEqual(result_intersection_list, [])

    def execute_tests_both_lists_with_elements_and_overlap(self: object) -> None:
        # Arrange
        linked_list_helpers: LinkedListHelpers = LinkedListHelpers()
        linked_list_1: LinkedList = LinkedList()
        element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
        for i in element_1:
            linked_list_1.append(i)

        linked_list_2: LinkedList = LinkedList()
        element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
        for i in element_2:
            linked_list_2.append(i)

        # Act
        result_union: LinkedList = linked_list_helpers.union(
            linked_list_1, linked_list_2)
        result_intersection: LinkedList = linked_list_helpers.intersection(
            linked_list_1, linked_list_2)

        # Assert
        result_union_list: list = result_union.to_list()
        result_union_list_sorted: list = sorted(result_union_list)
        result_intersection_list: list = result_intersection.to_list()
        result_intersection_list_sorted: list = sorted(
            result_intersection_list)

        self.assertEqual(result_union.size(), 11)
        self.assertListEqual(result_union_list_sorted, [1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65])
        self.assertEqual(result_intersection.size(), 3)
        self.assertListEqual(result_intersection_list_sorted, [4, 6, 21])

    def execute_tests_both_lists_with_elements_and_no_overlap(self: object) -> None:
        # Arrange
        linked_list_helpers: LinkedListHelpers = LinkedListHelpers()
        linked_list_1: LinkedList = LinkedList()
        element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
        for i in element_1:
            linked_list_1.append(i)

        linked_list_2: LinkedList = LinkedList()
        element_2 = [32, 9, 1, 11, 1]
        for i in element_2:
            linked_list_2.append(i)

        # Act
        result_union: LinkedList = linked_list_helpers.union(
            linked_list_1, linked_list_2)
        result_intersection: LinkedList = linked_list_helpers.intersection(
            linked_list_1, linked_list_2)

        # Assert
        result_union_list: list = result_union.to_list()
        result_union_list_sorted: list = sorted(result_union_list)
        result_intersection_list: list = result_intersection.to_list()
        result_intersection_list_sorted: list = sorted(
            result_intersection_list)

        self.assertEqual(result_union.size(), 11)
        self.assertListEqual(result_union_list_sorted, [1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65])
        self.assertEqual(result_intersection.size(), 0)
        self.assertListEqual(result_intersection_list_sorted, [])

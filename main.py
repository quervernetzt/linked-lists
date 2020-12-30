from tests.tests_linked_list_helpers import TestCasesLinkedListHelpers
from solution.linked_list import LinkedList
from solution.linked_list_helpers import LinkedListHelpers

if __name__ == "__main__":
    ###################################
    # Tests
    ###################################
    tests: TestCasesLinkedListHelpers = TestCasesLinkedListHelpers()
    tests.execute_tests_both_linked_lists_none()
    tests.execute_tests_both_linked_lists_first_is_none()
    tests.execute_tests_both_linked_lists_second_is_none()
    tests.execute_tests_both_linked_lists_both_empty_lists()
    tests.execute_tests_both_linked_lists_first_empty_list()
    tests.execute_tests_both_linked_lists_first_empty_list()
    tests.execute_tests_both_linked_lists_second_empty_list()
    tests.execute_tests_both_lists_with_elements_and_overlap()
    tests.execute_tests_both_lists_with_elements_and_no_overlap()

    ###################################
    # Demo
    ###################################
    # Demo 1
    linked_list_helpers: LinkedListHelpers = LinkedListHelpers()

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    # like but can have different order: 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21
    print(linked_list_helpers.union(linked_list_1, linked_list_2))
    # like but can have different order: 4 -> 21 -> 6
    print(linked_list_helpers.intersection(linked_list_1, linked_list_2))

    # Demo 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    # like but can have different order: 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23
    print(linked_list_helpers.union(linked_list_3, linked_list_4))
    # like but can have different order: no output
    print(linked_list_helpers.intersection(linked_list_3, linked_list_4))

import pytest

from linked_list import LinkedList, Node, linked_list_zip


# Helper Test Function
def does_all_values_match(linkedList, expected_array):
    current = linkedList.head
    index = 0
    while current is not None:
        if current.value != expected_array[index]:
            return False
        index += 1
        current = current.next
    return True

def test_node_class_can_instantiate():
    node1 = Node("apple")
    actual = node1.value
    expected = "apple"
    assert actual == expected
    assert node1.next == None

def test_can_instantiate_an_empty_list():
    linkedlist1 = LinkedList()
    actual = linkedlist1.head
    expected = None
    assert actual == expected

def test_can_properly_insert_into_length_list():
    ll2 = LinkedList()
    ll2.insert("a")
    ll2.insert("b")
    actual = ll2.head.value
    expected = "b"
    assert actual== expected

def test_head_property_will_point_to_first_node():
    node1 = Node("a")
    ll1 = LinkedList(node1)
    actual = ll1.head.value
    expected = "a"
    assert actual == expected


def test_can_properly_insert_multiple_nodes_into_linked_list():
    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c")
    actual = ll1.head.value
    expected = "c"
    assert actual == expected

def test_will_return_true_when_finding_value_witin_the_linked_list():
    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c").insert("d")
    actual = ll1.includes("c")
    expected = True
    assert actual == expected

def test_will_return_false_when_value_is_not_within_list():
    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c").insert("d")
    actual = ll1.includes("h")
    expected = False
    assert actual == expected

def test_can_properly_return_a_collection_of_all_values_that_exist_in_list():
    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c").insert("d")
    actual = str(ll1)
    expected = "{'d'} -> {'c'} -> {'b'} -> {'a'} ->  None "
    assert actual == expected

def test_can_succesfully_add_a_node_to_the_end_of_the_list():
    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c").insert("d")
    ll1.append("Z")

    expected = ["d", "c", "b", "a", "Z"]

    current = ll1.head
    index = 0

    while current is not None:
        assert current.value == expected[index]
        index += 1
        current = current.next


def test_can_sucessfully_add_multiple_nodes_to_the_end_of_list():
    ll1 = LinkedList()
    ll1.append("a").append("b").append("c").append("d")

    expected = ["a", "b", "c", "d"]

    current = ll1.head
    index = 0

    while current is not None:
        assert current.value == expected[index]
        index += 1
        current = current.next


def test_can_succesfully_insert_a_node_before_a_node_in_middle_of_list():
    ll1 = LinkedList()
    ll1.append("a").append("b").append("c").append("d")
    ll1.insert_before("c", "Z")

    expected = ["a", "b", "Z", "c", "d"]

    current = ll1.head
    index = 0

    while current is not None:
        assert current.value == expected[index]
        index += 1
        current = current.next


def test_can_succesfully_insert_a_node_before_the_first_node_of_a_linked_list():
    ll1 = LinkedList()
    ll1.append("a").append("b").append("c").append("d")
    ll1.insert_before("a", "Z")

    expected = ["Z", "a", "b", "c", "d"]

    current = ll1.head
    index = 0

    while current is not None:
        assert current.value == expected[index]
        index += 1
        current = current.next


def test_Can_successfully_insert_after_a_node_in_the_middle_of_the_linked_list():
    ll1 = LinkedList()
    ll1.append("a").append("b").append("c").append("d")
    ll1.insert_after("b", "Z")

    expected = ["a", "b", "Z", "c", "d"]

    current = ll1.head
    index = 0

    while current is not None:
        assert current.value == expected[index]
        index += 1
        current = current.next


def test_Can_successfully_insert_a_node_after_the_last_node_of_the_linked_list():
    ll1 = LinkedList()
    ll1.append("a").append("b").append("c").append("d")

    ll1.insert_after("d", "Z")

    expected = ["a", "b", "c", "d", "Z"]

    current = ll1.head
    index = 0

    while current is not None:
        assert current.value == expected[index]
        index += 1
        current = current.next


# def test_Where_k_is_greater_than_the_length_of_the_linked_list():
#     ll1 = LinkedList()
#     ll1.append("a").append("b").append("c").append("d").append("e")

#     actual = ll1.kth_from_the_end(2)
#     expected = "c"

#     assert actual == expected


def linked_list_zip_can_zip_two_list_of_equal_length(llist):
    ll2 = LinkedList()
    ll2.append(1).append(2).append(3).append(4).append(5)
    actual = linked_list_zip(llist, ll2)
    expected = ["a", 1, "b", 2, "c", 3, "d", 4, "e", 5]
    assert does_all_values_match(actual, expected)

def linked_list_zip_can_zip_two_list_with_first_list_being_longer(llist):
    ll2 = LinkedList()
    ll2.append(1).append(2).append(3)
    actual = linked_list_zip(llist, ll2)
    expected = ["a", 1, "b", 2, "c", 3, "d", "e"]
    assert does_all_values_match(actual, expected)

def linked_list_zip_can_zip_two_list_with_second_list_being_longer(llist):
    ll2 = LinkedList()
    ll2.append(1).append(2).append(3).append(4).append(5).append(6).append(7)
    actual = linked_list_zip(llist, ll2)
    expected = ["a", 1, "b", 2, "c", 3, "d", 4, "e", 5, 6, 7]
    assert does_all_values_match(actual, expected)

def linked_list_will_return_first_list_if_second_is_empty(llist):
    # ll2 = LinkedList()
    # actual
    pass

def linked_list_will_return_second_list_if_first_is_empty(llist):
    pass
######################
# Fixtures
######################
@pytest.fixture

def llist():
    llist = LinkedList()
    llist.append("a").append("b").append("c").append("d").append("e")
    return llist
@pytest.fixture(autouse=True)

def clean():
    """runs before each test automatically
    There's also a more advanced way to run code after each test as well
    Check the docs for that. Hint: it uses yield
    """
    llist = None

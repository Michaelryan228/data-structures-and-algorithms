import pytest

from linked_list import LinkedList, Node

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



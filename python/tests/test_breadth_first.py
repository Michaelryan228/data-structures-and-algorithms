import pytest

from trees.trees import BinaryTree, BinarySearchTree, Node
from breadth_first.breadth_first import breadth_first


def test_can_instantiate_a_tree_node():
    node1 = Node()
    assert node1.value == None
    assert node1.left == None
    assert node1.right == None


def test_can_instantiate_a_binary_search_tree():
    tree1 = BinarySearchTree()
    tree1.root == None


def test_breadth_first_can_display_correct_order():
    tree1 = BinarySearchTree()
    input1 = [10, 15, 8, 6, 14, 20]
    for item in input1:
        tree1.addIteravily(item)
    actual = breadth_first(tree1)
    expected = [10, 8, 15, 6, 14, 20]
    assert actual == expected


def test_breadth_first_can_account_for_one_node():
    tree1 = BinarySearchTree()
    tree1.addIteravily(7)
    actual = breadth_first(tree1)
    assert actual == [7]


def test_breadth_first_can_account_for_empty_tree():
    tree1 = BinarySearchTree()
    actual = breadth_first(tree1)
    assert actual == []


def test_breadth_first_can_account_for_unordered_list():
    node1 = Node("a")
    node2 = Node("b")
    node3 = Node("c")
    node4 = Node("d")
    node5 = Node("e")
    node6 = Node("f")
    node7 = Node("g")

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    tree1 = BinaryTree(node1)
    actual = breadth_first(tree1)
    expected = ["a", "b", "c", "d", "e", "f", "g"]
    assert actual == expected

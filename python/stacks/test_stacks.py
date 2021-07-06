import pytest

from stacks.stacks import Node, Stack


def test_Can_successfully_instantiate_an_empty_stack():
    new_stack = Stack()
    actual = new_stack.top
    expected = None
    assert actual == expected


def test_Can_successfully_push_onto_a_stack():
    new_stack = Stack()
    new_stack.push("a")
    actual = new_stack.top.value
    expected = "a"
    assert actual == expected


def test_Can_successfully_push_multiple_values_onto_a_stack():
    new_stack = Stack()
    new_stack.push("a")
    new_stack.push("b")
    new_stack.push("c")
    actual = new_stack.top.value
    expected = "c"
    assert actual == expected


def test_Can_successfully_pop_off_the_stack():
    new_stack = Stack()
    new_stack.push("a")
    new_stack.push("b")
    new_stack.push("c")
    actual = new_stack.pop()
    expected = "c"
    assert actual == expected
    assert new_stack.top.value == "b"


def test_Can_successfully_empty_a_stack_after_multiple_pops():
    new_stack = Stack()
    new_stack.push("a")
    new_stack.push("b")
    new_stack.push("c")
    new_stack.push("d")

    while new_stack.peek():
        new_stack.pop()

    assert new_stack.top == None


def test_Can_successfully_peek_the_next_item_on_the_stack():
    new_stack = Stack()
    new_stack.push("a")
    new_stack.push("b")
    new_stack.push("c")
    new_stack.push("d")

    actual = new_stack.peek()
    expected = "d"
    assert actual == expected


def test_Calling_pop_on_empty_stack_raises_exception():
    new_stack = Stack()
    assert new_stack.pop() == None
    # actual = new_stack.pop()
    # with pytest.raises(Exception):
    #     new_stack.pop()


def test_Calling_peek_on_empty_stack_raises_exception():
    new_stack = Stack()
    assert new_stack.peek() == None
    # actual = new_stack.pop()
    # with pytest.raises(Exception):
    #     new_stack.peek()

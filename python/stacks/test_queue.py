import pytest

from queues.queues import Queue


def test_Can_successfully_instantiate_an_empty_queue():
    new_queue = Queue()
    assert new_queue.front == None
    assert new_queue.rear == None


def test_Can_successfully_enqueue_into_a_queue():
    new_queue = Queue()
    new_queue.enqueue("a")
    assert new_queue.front.value == "a"


def test_Can_successfully_enqueue_multiple_values_into_a_queue():
    new_queue = Queue()
    new_queue.enqueue("a")
    new_queue.enqueue("b")
    new_queue.enqueue("c")
    new_queue.enqueue("d")
    assert new_queue.front.value == "a"
    assert new_queue.rear.value == "d"


def test_Can_successfully_empty_a_queue_after_multiple_dequeues():
    new_queue = Queue()
    new_queue.enqueue("a")
    new_queue.enqueue("b")
    new_queue.enqueue("c")
    new_queue.enqueue("d")

    while new_queue.peek():
        new_queue.dequeue()

    assert new_queue.front == None


def test_Calling_dequeue_on_empty_queue_raises_exception():
    new_queue = Queue()
    assert new_queue.dequeue() == None


def test_Calling_peek_on_empty_queue_raises_exception():
    new_queue = Queue()
    assert new_queue.peek() == None

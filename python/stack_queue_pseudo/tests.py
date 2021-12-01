import pytest

from animal_shelter.animal_shelter import Animal_Shelter, Node

def test_can_successfully_instantiate_an_empty_node():
    node1 = Node()
    assert node1.value == None
    assert node1.next == None

def test_can_successfully_instantiate_an_empty_Animal_Shelter():
    new_shelter = Animal_Shelter()
    assert new_shelter.front == None
    assert new_shelter.rear == None
    assert new_shelter.length == 0

def test_can_successfully_enqueue_one_animal_into_animal_shelter():
    new_shelter = Animal_Shelter()
    input1 = {"animal": "dog"}
    new_shelter.enqueue(input1)
    assert new_shelter.front.value["animal"] == "dog"
    assert new_shelter.rear.value["animal"] == "dog"
    assert new_shelter.length == 1

def test_can_enqueue_multiple_animals_into_Animal_Shelter(new_shelter):
    assert new_shelter.front.value["animal"] == "dog"
    assert new_shelter.rear.value["animal"] == "cat"
    assert new_shelter.length == 5

def test_can_successfully_dequeue_pref_animal_in_front(new_shelter):
    actual = new_shelter.dequeue("dog")
    expected = "dog"
    assert actual == expected
    assert new_shelter.front.value["animal"] == "dog"
    assert new_shelter.length == 4

def test_can_successfully_dequeue_pref_animal_in_middle(new_shelter):
    actual = new_shelter.dequeue("cat")
    expected = "cat"
    assert actual == expected
    assert new_shelter.front.value["animal"] == "dog"
    assert new_shelter.rear.value["animal"] == "cat"
    assert new_shelter.length == 4

def test_can_successfully_dequeue_pref_animal_at_the_end(cat_last):
    actual = cat_last.dequeue("cat")
    expected = "cat"
    assert actual == expected
    assert cat_last.front.value["animal"] == "dog"
    assert cat_last.rear.value["animal"] == "dog"
    assert cat_last.length == 4

def test_calling_dequeue_on_empty_queue_raises_exception():
    empty_shelter = Animal_Shelter()
    with pytest.raises(Exception):
        empty_shelter.dequeue("dog")

def test_calling_dequeue_with_pref_animal_not_in_shelter(all_dogs):
    actual = all_dogs.dequeue("cat")
    expected = None
    assert actual == expected
    assert all_dogs.length == 5

@pytest.fixture
def new_shelter():
    new_shelter = Animal_Shelter()
    input1 = {"animal": "dog"}
    input2 = {"animal": "dog"}
    input3 = {"animal": "cat"}
    input4 = {"animal": "dog"}
    input5 = {"animal": "cat"}
    new_shelter.enqueue(input1)
    new_shelter.enqueue(input2)
    new_shelter.enqueue(input3)
    new_shelter.enqueue(input4)
    new_shelter.enqueue(input5)
    return new_shelter

@pytest.fixture
def all_dogs():
    all_dogs = Animal_Shelter()
    input1 = {"animal": "dog"}
    input2 = {"animal": "dog"}
    input3 = {"animal": "dog"}
    input4 = {"animal": "dog"}
    input5 = {"animal": "dog"}
    all_dogs.enqueue(input1)
    all_dogs.enqueue(input2)
    all_dogs.enqueue(input3)
    all_dogs.enqueue(input4)
    all_dogs.enqueue(input5)
    return all_dogs

@pytest.fixture
def cat_last():
    cat_last = Animal_Shelter()
    input1 = {"animal": "dog"}
    input2 = {"animal": "dog"}
    input3 = {"animal": "dog"}
    input4 = {"animal": "dog"}
    input5 = {"animal": "cat"}
    cat_last.enqueue(input1)
    cat_last.enqueue(input2)
    cat_last.enqueue(input3)
    cat_last.enqueue(input4)
    cat_last.enqueue(input5)
    return cat_last

@pytest.fixture(autouse=True)
def clean():
    """runs before each test automatically
    """
    new_shelter = None

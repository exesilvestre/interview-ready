import pytest
from ...stacks.animalShelter import AnimalShelter


def test_enqueue_and_dequeue_elements_from_queue():
    shelter = AnimalShelter()

    # Enqueue some animals
    shelter.enqueue("dog")
    shelter.enqueue("cat")
    shelter.enqueue("dog")

    # Dequeue any animal
    assert shelter.dequeueAny().type == "dog"  # Oldest animal is a dog
    assert shelter.dequeueAny().type == "cat"  # Oldest animal is a cat

    # Enqueue more animals
    shelter.enqueue("cat")
    shelter.enqueue("dog")

    # Dequeue a dog
    assert shelter.dequeueDog().type == "dog"  # Oldest dog

    # Enqueue another dog
    shelter.enqueue("dog")

    # Dequeue a cat
    assert shelter.dequeueCat().type == "cat"  # Oldest cat


def test_dequeue_methods_return_none_when_shelter_is_empty():
    shelter = AnimalShelter()

    assert shelter.dequeueAny() is None
    assert shelter.dequeueDog() is None
    assert shelter.dequeueCat() is None

import pytest
from ...stacks.stackOfPlates import StackOfPlates


def test_push_and_pop_elements_from_stack():
    stack = StackOfPlates(3)  # Capacity: 3

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None  # Stack is empty

    stack.push(4)
    stack.push(5)
    stack.push(6)

    assert stack.pop() == 6
    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() is None  # Stack is empty


def test_push_and_pop_elements_from_multiple_stacks():
    stack = StackOfPlates(2)  # Capacity: 2

    stack.push(1)
    stack.push(2)

    stack.push(3)  # New stack
    stack.push(4)

    stack.push(5)  # New stack

    assert stack.pop() == 5  # Pop from last stack
    assert stack.pop() == 4  # Pop from middle stack
    assert stack.pop() == 3  # Pop from middle stack
    assert stack.pop() == 2  # Pop from first stack
    assert stack.pop() == 1  # Pop from first stack
    assert stack.pop() is None  # Stack is empty


def test_pop_from_empty_stack_returns_none():
    stack = StackOfPlates(2)  # Capacity: 2

    assert stack.pop() is None


def test_push_beyond_capacity_creates_new_stack():
    stack = StackOfPlates(2)  # Capacity: 2

    stack.push(1)
    stack.push(2)

    stack.push(3)  # New stack
    stack.push(4)

    assert stack.pop() == 4  # Pop from last stack
    assert stack.pop() == 3  # Pop from last stack
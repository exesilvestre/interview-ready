import pytest
from ...stacks.threeStacks import ThreeStacks


def test_push_and_pop_elements_from_stack_1():
    three_stacks = ThreeStacks(9)  # Array length: 9

    three_stacks.push(0, 1)
    three_stacks.push(0, 2)
    three_stacks.push(0, 3)

    assert three_stacks.pop(0) == 3
    assert three_stacks.pop(0) == 2
    assert three_stacks.pop(0) == 1
    assert three_stacks.pop(0) is None  # Stack should be empty now


def test_push_and_pop_elements_from_stack_2():
    three_stacks = ThreeStacks(9)  # Array length: 9

    three_stacks.push(1, 4)
    three_stacks.push(1, 5)
    three_stacks.push(1, 6)

    assert three_stacks.pop(1) == 6
    assert three_stacks.pop(1) == 5
    assert three_stacks.pop(1) == 4
    assert three_stacks.pop(1) is None  # Stack should be empty now


def test_push_and_pop_elements_from_stack_3():
    three_stacks = ThreeStacks(9)  # Array length: 9

    three_stacks.push(2, 7)
    three_stacks.push(2, 8)
    three_stacks.push(2, 9)

    assert three_stacks.pop(2) == 9
    assert three_stacks.pop(2) == 8
    assert three_stacks.pop(2) == 7
    assert three_stacks.pop(2) is None  # Stack should be empty now


def test_pop_elements_from_empty_stack():
    three_stacks = ThreeStacks(3)  # Array length: 3

    # Attempt to pop from empty stacks should return None
    assert three_stacks.pop(0) is None
    assert three_stacks.pop(1) is None
    assert three_stacks.pop(2) is None


def test_peek_elements_from_stacks():
    three_stacks = ThreeStacks(3)  # Array length: 3

    three_stacks.push(0, 1)
    three_stacks.push(1, 2)
    three_stacks.push(2, 3)

    assert three_stacks.peek(0) == 1
    assert three_stacks.peek(1) == 2
    assert three_stacks.peek(2) == 3


def test_peek_elements_from_empty_stack():
    three_stacks = ThreeStacks(3)  # Array length: 3

    # Attempt to peek from empty stacks should return None
    assert three_stacks.peek(0) is None
    assert three_stacks.peek(1) is None
    assert three_stacks.peek(2) is None
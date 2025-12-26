from problems_python.strings.palindromePermutation import palindromePermutation


def test_empty_string():
    assert palindromePermutation("") is True


def test_single_character_string():
    assert palindromePermutation("a") is True


def test_palindrome_with_odd_length():
    assert palindromePermutation("taco cat") is True


def test_palindrome_with_even_length():
    assert palindromePermutation("rdeder") is True


def test_non_palindrome_with_odd_length():
    assert palindromePermutation("hello") is False


def test_non_palindrome_with_even_length():
    assert palindromePermutation("world") is False


def test_string_with_mixed_case():
    assert palindromePermutation("RaceCar") is True


def test_string_with_non_alphanumeric_characters():
    assert palindromePermutation("12321") is True


def test_string_with_no_possible_palindrome_permutation():
    assert palindromePermutation("abcdefg") is False

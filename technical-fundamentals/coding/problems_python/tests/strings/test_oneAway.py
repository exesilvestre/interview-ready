from problems_python.strings.oneAway import isOneAway


def test_one_away_replace():
    assert isOneAway("pale", "bale") is True   # Replacement
    assert isOneAway("bbaa", "bcca") is False  # Replacement


def test_one_away_replace_duplicate():
    assert isOneAway("pale", "bale") is True   # Replacement


def test_one_away_insert():
    assert isOneAway("pale", "ple") is True    # Insertion


def test_one_away_remove():
    assert isOneAway("pale", "pales") is True  # Removal


def test_same_strings():
    assert isOneAway("abc", "abc") is True     # No edits


def test_more_than_one_edit_away():
    assert isOneAway("abcd", "efgh") is False  # More than one edit away


def test_more_than_one_edit_away_2():
    assert isOneAway("palesa", "pale") is False  # More than one edit away #2


def test_empty_strings():
    assert isOneAway("", "") is True            # Zero edits away


def test_one_character_difference():
    assert isOneAway("a", "ab") is True         # One character difference


def test_empty_and_non_empty_string():
    assert isOneAway("", "a") is True           # Empty vs non-empty

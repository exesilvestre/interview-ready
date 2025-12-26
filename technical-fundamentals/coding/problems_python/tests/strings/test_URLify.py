from problems_python.strings.urlify import URLify


def test_replaces_spaces_in_a_string():
    assert URLify("ab c") == "ab%20c"


def test_handles_leading_and_trailing_spaces():
    assert URLify("  ab c  ") == "%20%20ab%20c%20%20"


def test_returns_empty_string_when_input_is_empty():
    assert URLify("") == ""


def test_does_not_modify_string_without_spaces():
    assert URLify("abc") == "abc"


def test_handles_multiple_consecutive_spaces():
    assert URLify("a  b   c") == "a%20%20b%20%20%20c"


def test_handles_special_characters():
    assert URLify("a b!c") == "a%20b!c"


def test_mr_3ohn_smith():
    assert URLify("Mr 3ohn Smith") == "Mr%203ohn%20Smith"
from problems_python.strings.stringRotation import stringRotation


def test_rotates_a_string():
    str1 = "Hello"
    str2 = "oHell"
    result = stringRotation(str1, str2)
    assert result is True


def test_rotates_another_string():
    str1 = "waterbottle"
    str2 = "erbottlewat"
    result = stringRotation(str1, str2)
    assert result is True

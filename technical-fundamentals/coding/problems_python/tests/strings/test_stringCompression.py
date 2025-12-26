from problems_python.strings.stringCompression import stringCompression


def test_compresses_string_with_repeated_characters():
    assert stringCompression("aabcccccaaa") == "a2b1c5a3"


def test_returns_original_string_if_compression_does_not_reduce_length():
    assert stringCompression("abcde") == "abcde"


def test_returns_empty_string_for_empty_input():
    assert stringCompression("") == ""


def test_returns_single_character_for_string_with_single_character():
    assert stringCompression("a") == "a"


def test_compresses_string_with_uppercase_and_lowercase_letters():
    assert stringCompression("AAAbbbCCCddd") == "A3b3C3d3"


def test_returns_original_string_if_no_repeated_characters():
    assert stringCompression("abcdef") == "abcdef"

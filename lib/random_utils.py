""" Utility methods for generating random values"""
import random
import string

# Define charsets
charsets = {
    "lowercase": string.ascii_lowercase,
    "uppercase": string.ascii_uppercase,
    "digits": string.digits,
    "punctuation": string.punctuation,
}


def _random_string(length: int, include_lowercase: bool = True, include_uppercase: bool = True,
                   include_digits: bool = True, include_punctuation: bool = True) -> str:
    """
    Generate a random string of a given length with the specified character sets.

    Args:
        length (int): Length of the random string to generate.
        include_lowercase (bool): Whether to include lowercase letters in the string. Defaults to True.
        include_uppercase (bool): Whether to include uppercase letters in the string. Defaults to True.
        include_digits (bool): Whether to include digits in the string. Defaults to True.
        include_punctuation (bool): Whether to include punctuation in the string. Defaults to True.

    Returns:
        str: Generated random string.
    """
    assert length > 0, "Length should be a positive integer."
    assert include_lowercase or include_uppercase or include_digits or include_punctuation, \
        "At least one character set should be included."

    charset = ''
    if include_lowercase:
        charset += charsets["lowercase"]
    if include_uppercase:
        charset += charsets["uppercase"]
    if include_digits:
        charset += charsets["digits"]
    if include_punctuation:
        charset += charsets["punctuation"]

    return ''.join(random.choice(charset) for _ in range(length))


def random_string(length: int, include_punctuation: bool = False) -> str:
    """
    Generate a random string of a given length, with an option to include punctuation.

    Args:
        length (int): Length of the random string to generate.
        include_punctuation (bool): Whether to include punctuation in the string. Defaults to False.

    Returns:
        str: Generated random string.
    """
    return _random_string(length, include_punctuation=include_punctuation)


def random_lowercase_string(length: int, include_digits: bool = False, include_punctuation: bool = False) -> str:
    """
    Generate a random string of a given length, with only lowercase letters, digits and punctuation based on input.

    Args:
        length (int): Length of the random string to generate.
        include_digits (bool): Whether to include digits in the string. Defaults to False.
        include_punctuation (bool): Whether to include punctuation in the string. Defaults to False.

    Returns:
        str: Generated random string.
    """
    return _random_string(length, include_uppercase=False, include_digits=include_digits,
                          include_punctuation=include_punctuation)


def random_uppercase_string(length: int, include_digits: bool = False, include_punctuation: bool = False) -> str:
    """
    Generate a random string of a given length, with only uppercase letters, digits and punctuation based on input.

    Args:
        length (int): Length of the random string to generate.
        include_digits (bool): Whether to include digits in the string. Defaults to False.
        include_punctuation (bool): Whether to include punctuation in the string. Defaults to False.

    Returns:
        str: Generated random string.
    """
    return _random_string(length, include_lowercase=False, include_digits=include_digits,
                          include_punctuation=include_punctuation)


def random_digits_string(length: int) -> str:
    """
    Generate a random string of a given length, with only digits.

    Args:
        length (int): Length of the random string to generate.

    Returns:
        str: Generated random string.
    """
    return _random_string(length, include_uppercase=False, include_lowercase=False,
                          include_punctuation=False)


def random_punctuation_string(length: int) -> str:
    """
    Generate a random string of a given length, with only punctuation.

    Args:
        length (int): Length of the random string to generate.

    Returns:
        str: Generated random string.
    """
    return _random_string(length, include_lowercase=False, include_uppercase=False, include_digits=False)


def random_letters_string(length: int) -> str:
    """
    Generate a random string of a given length, with only letters (lowercase and uppercase).

    Args:
        length (int): Length of the random string to generate.

    Returns:
        str: Generated random string.
    """
    return _random_string(length, include_digits=False, include_punctuation=False)

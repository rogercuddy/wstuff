""" Unit tests for the random_utils module. """
import string

import pytest

from lib import random_utils


@pytest.mark.repeat(10)
def test_random_string():
    """
    Test the generation of a random string of a specified length.

    This test checks that a generated string has the correct length and only contains alphanumeric characters.
    """
    t_val = random_utils.random_string(10)
    assert len(t_val) == 10 and all(c in string.ascii_letters + string.digits for c in t_val)


@pytest.mark.repeat(10)
def test_random_string_with_punctuation():
    """
    Test the generation of a random string with punctuation of a specified length.

    This test checks that a generated string has the correct length and only contains alphanumeric characters
    and punctuation.
    """
    t_val = random_utils.random_string(10, include_punctuation=True)
    assert len(t_val) == 10 and all(c in string.ascii_letters + string.digits + string.punctuation for c in t_val)


@pytest.mark.repeat(10)
def test_random_lowercase_string():
    """
    Test the generation of a random lowercase string of a specified length.

    This test checks that a generated string has the correct length and only contains lowercase alphanumeric characters.
    """
    t_val = random_utils.random_lowercase_string(10)
    assert len(t_val) == 10 and all(c in string.ascii_lowercase + string.digits for c in t_val)


@pytest.mark.repeat(10)
def test_random_uppercase_string():
    """
    Test the generation of a random uppercase string of a specified length.

    This test checks that a generated string has the correct length and only contains uppercase alphanumeric characters.
    """
    t_val = random_utils.random_uppercase_string(10)
    assert len(t_val) == 10 and all(c in string.ascii_uppercase + string.digits for c in t_val)


@pytest.mark.repeat(10)
def test_random_digits_string():
    """
    Test the generation of a random string of digits of a specified length.

    This test checks that a generated string has the correct length and only contains digit characters.
    """
    t_val = random_utils.random_digits_string(10)
    assert len(t_val) == 10 and all(c in string.digits for c in t_val)


@pytest.mark.repeat(10)
def test_random_punctuation_string():
    """
    Test the generation of a random string of punctuation characters of a specified length.

    This test checks that a generated string has the correct length and only contains punctuation characters.
    """
    t_val = random_utils.random_punctuation_string(10)
    assert len(t_val) == 10 and all(c in string.punctuation for c in t_val)


@pytest.mark.repeat(10)
def test_random_letters_string():
    """
    Test the generation of a random string of letters of a specified length.

    This test checks that a generated string has the correct length and only contains letter characters.
    """
    t_val = random_utils.random_letters_string(10)
    assert len(t_val) == 10 and all(c in string.ascii_letters for c in t_val)


# Test that exceptions are raised for invalid input
@pytest.mark.repeat(10)
def test_invalid_length():
    """
    Test that an exception is raised when the length of the string to generate is invalid (i.e., zero or negative).
    """
    with pytest.raises(AssertionError):
        random_utils.random_string(0)


def test_no_charset():
    """
    Test that an exception is raised when no charset is selected for the generation of the random string.
    """
    # pylint: disable=protected-access
    with pytest.raises(AssertionError):
        random_utils._random_string(10, include_lowercase=False, include_uppercase=False, include_digits=False,
                                    include_punctuation=False)


def test_random_string_min_length():
    """
    Test the generation of a random string with a minimum length of 1.

    This test checks that a generated string has the correct length and contains at least one alphanumeric character.
    """
    # pylint: disable=protected-access
    t_val = random_utils.random_string(1)
    assert len(t_val) == 1 and any(c in string.ascii_letters + string.digits for c in t_val)


@pytest.mark.repeat(10)
def test_random_lowercase_string_no_digits():
    """
    Test the generation of a random lowercase string of a specified length without digits.

    This test checks that a generated string has the correct length and only contains lowercase letter characters.
    """
    t_val = random_utils.random_lowercase_string(10, include_digits=False)
    assert len(t_val) == 10 and all(c in string.ascii_lowercase for c in t_val)


@pytest.mark.repeat(10)
def test_random_uppercase_string_no_digits():
    """
    Test the generation of a random uppercase string of a specified length without digits.

    This test checks that a generated string has the correct length and only contains uppercase letter characters.
    """
    t_val = random_utils.random_uppercase_string(10, include_digits=False)
    assert len(t_val) == 10 and all(c in string.ascii_uppercase for c in t_val)

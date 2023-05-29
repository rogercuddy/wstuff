import string

import pytest

import lib.random_utils as random_utils


@pytest.mark.repeat(10)
def test_random_string():
    s = random_utils.random_string(10)
    assert len(s) == 10
    assert all(c in string.ascii_letters + string.digits for c in s)


@pytest.mark.repeat(10)
def test_random_string_with_punctuation():
    s = random_utils.random_string(10, include_punctuation=True)
    assert len(s) == 10
    assert all(c in string.ascii_letters + string.digits + string.punctuation for c in s)


@pytest.mark.repeat(10)
def test_random_lowercase_string():
    s = random_utils.random_lowercase_string(10)
    assert len(s) == 10
    assert all(c in string.ascii_lowercase + string.digits for c in s)


@pytest.mark.repeat(10)
def test_random_uppercase_string():
    s = random_utils.random_uppercase_string(10)
    assert len(s) == 10
    assert all(c in string.ascii_uppercase + string.digits for c in s)


@pytest.mark.repeat(10)
def test_random_digits_string():
    s = random_utils.random_digits_string(10)
    assert len(s) == 10
    assert all(c in string.digits for c in s)


@pytest.mark.repeat(10)
def test_random_punctuation_string():
    s = random_utils.random_punctuation_string(10)
    assert len(s) == 10
    assert all(c in string.punctuation for c in s)


@pytest.mark.repeat(10)
def test_random_letters_string():
    s = random_utils.random_letters_string(10)
    assert len(s) == 10
    assert all(c in string.ascii_letters for c in s)


# Test that exceptions are raised for invalid input
@pytest.mark.repeat(10)
def test_invalid_length():
    with pytest.raises(AssertionError):
        random_utils.random_string(0)


def test_no_charset():
    with pytest.raises(AssertionError):
        random_utils._random_string(10, include_lowercase=False, include_uppercase=False, include_digits=False,
                                    include_punctuation=False)


def test_random_string_min_length():
    s = random_utils.random_string(1)
    assert len(s) == 1
    assert any(c in string.ascii_letters + string.digits for c in s)


@pytest.mark.repeat(10)
def test_random_lowercase_string_no_digits():
    s = random_utils.random_lowercase_string(10, include_digits=False)
    assert len(s) == 10
    assert all(c in string.ascii_lowercase for c in s)


@pytest.mark.repeat(10)
def test_random_uppercase_string_no_digits():
    s = random_utils.random_uppercase_string(10, include_digits=False)
    assert len(s) == 10
    assert all(c in string.ascii_uppercase for c in s)

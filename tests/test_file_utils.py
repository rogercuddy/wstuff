import os
import sys
import tempfile

import pytest

from lib.file_utils import check_permissions  # Assuming the function is in permissions.py

pytestmark = pytest.mark.skipif(sys.platform != 'linux', reason="runs only on linux")


def test_check_permissions_file():
    # Create a temporary file
    with tempfile.NamedTemporaryFile() as temp:
        # Get the permissions of the temporary file
        permissions = check_permissions(temp.name)

        # Assert the user has read and write permissions
        assert permissions['user']['read'] is True
        assert permissions['user']['write'] is True

        # The execute permission may vary based on the system configuration
        # Assert the group and others do not have write or execute permissions
        assert permissions['group']['write'] is False
        assert permissions['group']['execute'] is False
        assert permissions['others']['write'] is False
        assert permissions['others']['execute'] is False


def test_check_permissions_directory():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp:
        # Get the permissions of the temporary directory
        permissions = check_permissions(temp)

        # Assert the user has read, write, and execute permissions
        assert permissions['user']['read'] is True
        assert permissions['user']['write'] is True
        assert permissions['user']['execute'] is True

        # The permissions for group and others may vary based on the system configuration
        # Assert the group and others do not have write permissions
        assert permissions['group']['write'] is False
        assert permissions['others']['write'] is False


def test_check_permissions_non_existent_path():
    # Generate a non-existent path
    non_existent_path = os.path.join(tempfile.gettempdir(), 'non_existent_path')

    # Assert a FileNotFoundError is raised when trying to get the permissions of a non-existent path
    with pytest.raises(FileNotFoundError):
        check_permissions(non_existent_path)

import pathlib
import stat


def check_permissions(path):
    """
    This function checks the permissions of a file or directory.

    :param path: The path to the file or directory to check.
    :type path: str
    :return: A dictionary containing the permissions of the file or directory.
    :rtype: dict
    """
    # Initialize pathlib.Path object
    p = pathlib.Path(path)

    # Check if path exists
    if not p.exists():
        raise FileNotFoundError(f"The file or directory {path} does not exist.")

    # Get the file or directory's permissions
    permissions = p.stat().st_mode

    # Check the read, write, and execute permissions for the user, group, and others
    permission_dict = {
        'user': {
            'read': bool(permissions & stat.S_IRUSR),
            'write': bool(permissions & stat.S_IWUSR),
            'execute': bool(permissions & stat.S_IXUSR),
        },
        'group': {
            'read': bool(permissions & stat.S_IRGRP),
            'write': bool(permissions & stat.S_IWGRP),
            'execute': bool(permissions & stat.S_IXGRP),
        },
        'others': {
            'read': bool(permissions & stat.S_IROTH),
            'write': bool(permissions & stat.S_IWOTH),
            'execute': bool(permissions & stat.S_IXOTH),
        }
    }

    return permission_dict

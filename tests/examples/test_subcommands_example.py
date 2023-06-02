import argparse
import io
from unittest import mock

from examples.subcommand_example import procedure_a, procedure_b


# Test procedure_a
@mock.patch('sys.stdout', new_callable=io.StringIO)
def test_procedure_a(mock_stdout):
    # Create a mock Namespace object to simulate the args
    args = argparse.Namespace(count=2, option='custom_option', path='/custom/path/to/A', verbose=True)
    procedure_a(args)
    output = mock_stdout.getvalue()
    assert output == "Procedure A activated with options: custom_option, /custom/path/to/A, True\n" * 2


# Test procedure_b
@mock.patch('sys.stdout', new_callable=io.StringIO)
def test_procedure_b(mock_stdout):
    # Create a mock Namespace object to simulate the args
    args = argparse.Namespace(count=3, option='custom_option', path='/custom/path/to/B', verbose=False)
    procedure_b(args)
    output = mock_stdout.getvalue()
    assert output == "Procedure B activated with options: custom_option, /custom/path/to/B, False\n" * 3

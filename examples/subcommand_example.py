import argparse


# Define the procedures for the subcommands
def procedure_A(args):
    for _ in range(args.count):
        print(f"Procedure A activated with options: {args.option}, {args.path}, {args.verbose}")


def procedure_B(args):
    for _ in range(args.count):
        print(f"Procedure B activated with options: {args.option}, {args.path}, {args.verbose}")


# Create the top-level parser
parser = argparse.ArgumentParser()

# Create the subparsers for the two subcommands
subparsers = parser.add_subparsers()

# Create the parser for the "A" command
parser_A = subparsers.add_parser('A', help='A command')
parser_A.add_argument('--option', type=str, default='default_A', help='Option for A command')
parser_A.add_argument('--path', type=str, default='/path/to/A', help='Path for A command')
parser_A.add_argument('--verbose', action='store_true', help='Verbose mode for A command')
parser_A.add_argument('--count', type=int, default=1, help='Count for A command')
parser_A.set_defaults(func=procedure_A)

# Create the parser for the "B" command
parser_B = subparsers.add_parser('B', help='B command')
parser_B.add_argument('--option', type=str, default='default_B', help='Option for B command')
parser_B.add_argument('--path', type=str, default='/path/to/B', help='Path for B command')
parser_B.add_argument('--verbose', action='store_true', help='Verbose mode for B command')
parser_B.add_argument('--count', type=int, default=1, help='Count for B command')
parser_B.set_defaults(func=procedure_B)

# Parse the arguments
args = parser.parse_args()

# Call the appropriate function based on the provided subcommand
args.func(args)

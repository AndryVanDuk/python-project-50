import argparse


DESCRIPTION = 'Compares two configuration files and shows a difference.'


def cli():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('first_file',
                        help='Path to json or yml file')
    parser.add_argument('second_file',
                        help='Path to second file in same format')
    parser.add_argument('-f', '--format', default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help='set format of output: stylish, plain or json')
    return parser.parse_args()


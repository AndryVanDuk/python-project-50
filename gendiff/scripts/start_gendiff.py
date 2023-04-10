#!/usr/bin/env python3
import argparse
from gendiff import generate_diff
from gendiff.cli import cli


def main():
    args = cli()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()

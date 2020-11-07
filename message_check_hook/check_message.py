#!/usr/bin/env python3

import sys
import argparse
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('commit_msg_filepath')
    parser.add_argument('-r', '--regex', required=True)
    args = parser.parse_args()

    with open(args.commit_msg_filepath, 'r') as f:
        commit_msg = f.read()

    if re.match(args.regex, commit_msg):
        exit(0)
    else:
        print('Commit message did not comply with configured regex.\n'
              f'=> regex: \'{args.regex}\'',
              file=sys.stderr)
        exit(1)


if __name__ == '__main__':
    main()

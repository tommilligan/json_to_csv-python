#!/usr/bin/env python
"""
"""

import argparse
import logging
import sys

import json_to_csv
from json_to_csv.utils import getModuleLogger

logger = getModuleLogger(__name__)

def mainParser():
    """
    Command line parser
    """
    parser = argparse.ArgumentParser("json_to_csv")
    parser.add_argument("-v", "--verbose", action="store_true", help="Turn up logging")
    return parser

def main():
    """
    Command line entry point
    """
    logger.debug("Main called")

    # Setup logging
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARN)
    ch.setFormatter(logging.Formatter("%(asctime)s|%(levelname)s|%(name)s|%(message)s"))
    root = logging.getLogger()
    root.handlers = [ch]

    # Take cli arguments
    parser = mainParser()
    args = parser.parse_args()

    # Alter logging
    if args.verbose:
        ch.setLevel(logging.DEBUG)

    logger.debug(args)

    # Call module
    for line in json_to_csv.jsonToCsv(sys.stdin.read()):
        print(line, end='')
    
    logger.debug("Main completed")

if __name__ == "__main__":
    main()

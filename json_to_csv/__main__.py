#!/usr/bin/env python
"""
"""

import argparse
import json
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
    parser.add_argument("inputFile", help="Input JSON file")
    parser.add_argument("outputFile", help="Output CSV file")
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
    json_to_csv.jsonToCsv(args.inputFile, args.outputFile)
    
    logger.debug("Main completed")

if __name__ == "__main__":
    main()

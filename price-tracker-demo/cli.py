"""
CLI interface for the app
"""

import argparse


def load_cli():
    parser = argparse.ArgumentParser(
        prog="price-tracker-demo",
        description="A simple Python CLI app to track prices"
    )

    parser.add_argument("-a", "--add", dest="item_url")
    parser.add_argument("-l", "--list", action='store_true')

    args = parser.parse_args()

    return args

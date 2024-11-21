"""
-l => lines
-c => characters
-w => words
empty => all 3
"""

import argparse


def parse_args() -> tuple[list[str], str]:
    parser = argparse.ArgumentParser(
        description="Python implementation of the core-utils wc"
    )
    parser.add_argument("-l", "--lines", action="store_true")
    parser.add_argument("-w", "--words", action="store_true")
    parser.add_argument("-c", "--characters", action="store_true")
    parser.add_argument("filepath", type=str)

    args = parser.parse_args()

    return args


def count_lines(content: list[str]) -> int:
    return len(content)


def count_words(content: list[str]) -> int:
    words = get_words(content)
    return len(words)


def get_words(content):
    words = sum([line.split() for line in content], [])
    words = [word.strip() for word in words]
    return words


def count_characters(content: list[str]):
    words = get_words(content)
    characters = [len(word) for word in words]
    return sum(characters)


if __name__ == "__main__":
    args = parse_args()

    with open(args.filepath, "r") as fp:
        lines = fp.readlines()

    lines_count = count_lines(lines)
    words_count = count_words(lines)
    characters_count = count_characters(lines)

    if args.lines:
        print(lines_count, end=" ")
    if args.words == "-w":
        print(words_count, end=" ")
    if args.characters == "-c":
        print(characters_count, end=" ")
    if not any((args.lines, args.words, args.characters)):
        print(lines_count, words_count, characters_count)

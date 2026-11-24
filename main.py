"""Print the one-word username entry and hand it to the grader.

The entry lives in entry.txt next to this file. The program prints the
single word and also drops it into /output/entry.txt when that folder
is available, which is where the sealed scorer looks.
"""

import os
import sys


def load_word():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), encoding="utf-8") as handle:
        word = handle.read().strip()
    if not word or len(word) > 30 or any(ch.isspace() for ch in word):
        raise ValueError("entry must be one word of 1 to 30 characters")
    return word


def deliver(word):
    """Print the word and leave a copy where the sealed scorer looks."""
    print(word)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as handle:
            handle.write(word)
    except OSError:
        pass


def main():
    word = load_word()
    deliver(word)
    return 0


if __name__ == "__main__":
    sys.exit(main())

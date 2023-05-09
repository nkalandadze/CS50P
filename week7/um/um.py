# დავალება #42 - Regular, um, Expressions
import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\bum\b"
    count = len(re.findall(pattern, s, re.IGNORECASE))
    return count



if __name__ == "__main__":
    main()
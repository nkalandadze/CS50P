# დავალება #40 - Watch on Youtube
import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        match = re.search(r"((https?):\/\/(www\.)?youtube\.com\/embed\/)([a-zA-Z_0-9]+)", s)
        if match:
            url_list = match.groups()
            new_url = "https://youtu.be/" + url_list[3]
            return new_url



if __name__ == "__main__":
    main()
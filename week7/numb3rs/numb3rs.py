# დავალება #39 - NUMB3RS
import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^(?:\d{1,3}\.){3}\d{1,3}$", ip):
        numbers = ip.split(".")
        print(numbers)
        for number in numbers:
            if int(number) < 0 or int(number) > 255:
                return False
        return True
    else:
        return False



if __name__ == "__main__":
    main()
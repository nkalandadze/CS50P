# დავალება #32 - Lines of Code
import sys
def main():
    print(count_lines())


def count_lines():
    try:
        # check if user didn't enter any file name
        if len(sys.argv) == 1:
            sys.exit("Too few command-line arguments")
        # check if user entered more than 1 file name
        elif len(sys.argv) > 2:
            sys.exit("Too many command_line arguments")
        # check if file is in python format
        elif sys.argv[1][-3:] != ".py":
            sys.exit("Not a Python file ")
        else:
            with open(sys.argv[1]) as file:
                number_of_lines = 0
                for line in file:
                    line = line.strip()
                    # check if line is blank line
                    if line == "":
                        pass
                    # check if there is comment on the line
                    elif line[0] != "#":
                        number_of_lines += 1
            return number_of_lines
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
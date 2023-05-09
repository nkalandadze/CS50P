# დავალება #33 - Pizza Py

import sys
from tabulate import tabulate
import csv
def main():
    print(format_table())


def format_table():
    try:
        # check if user didn't enter any file name
        if len(sys.argv) == 1:
            sys.exit("Too few command-line arguments")
        # check if user entered more than 1 file name
        elif len(sys.argv) > 2:
            sys.exit("Too many command_line arguments")
        # check if file is in CSV format
        elif sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file ")
        else:
            with open(sys.argv[1]) as file:
                list = []
                csv_file = csv.reader(file)
                # add csv files rows to a list
                for row in csv_file:
                    list.append(row)
                # add first row as a header, and remaining as table content
                headers = list[0]
                table = list[1:]
                return tabulate(table, headers, tablefmt="grid")
            
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
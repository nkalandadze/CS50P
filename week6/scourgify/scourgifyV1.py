# დავალება #34 - Scourgify
import sys, csv
def main():
    format_file()

def format_file():
    try:
        # check if user didn't enter 2 file names
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        # check if user entered more than 2 file name
        elif len(sys.argv) > 3:
            sys.exit("Too many command_line arguments")
        # check if file is in CSV format
        elif sys.argv[1][-4:] != ".csv" and sys.argv[2][-4:] != ".csv":
            sys.exit("Not a CSV file ")
        else:
            with open(sys.argv[1]) as file:
                person = []
                first = ["first"]
                last = ["last"]
                house = []
                reader = csv.reader(file)
                for row in reader:
                    # split information into persons full name and house
                    person.append(row[0])
                    house.append(row[1])

                # split persons full name into first and last name
                for i in range(1, len(person)):
                    first.append(person[i].split(",")[1])
                    last.append(person[i].split(",")[0])
            # # write information into new file
            with open(sys.argv[2], "w", newline="") as file:
                writer = csv.writer(file)
                for i in range(len(first)):
                    row = (first[i].strip(),last[i].strip(),house[i].strip())
                    writer.writerow(row)
                return file
            
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
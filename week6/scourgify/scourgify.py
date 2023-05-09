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
                output = []
                reader = csv.DictReader(file)
                # split information into persons first name, last name and house
                for row in reader:
                    full_name = row["name"].split(",")
                    output.append({"first": full_name[1].lstrip(), "last": full_name[0], "house": row["house"] })
                   
            # write information into new file with writer
            with open(sys.argv[2], "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["first", "last", "house"])
                for row in output:
                    new_row = (row["first"], row["last"], row["house"])
                    writer.writerow(new_row)
                return file
            # write information into new file with DictWriter
            # with open(sys.argv[2], "w", newline="") as file:
            #     headers = ["first", "last", "house"]
            #     writer = csv.DictWriter(file, fieldnames=headers)
            #     writer.writeheader()
            #     for row in output:
            #         writer.writerow(row)
            #     return file
      
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
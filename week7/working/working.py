# დავალება #41 - Working 9 to 5
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # check time pattern
    pattern = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)

    #if pattern is found then split it to the hour, minute, meridiem groups
    if pattern:
        splitted_pattern = pattern.groups()
        if int(splitted_pattern[1]) > 12 or int(splitted_pattern[5]) > 12:
            raise ValueError
        
        # format start time
        start_time = format_date(splitted_pattern[1], splitted_pattern[2], splitted_pattern[3])

        # format end time
        end_time = format_date(splitted_pattern[5], splitted_pattern[6], splitted_pattern[7])

        return start_time + " to " + end_time
    else:
        # return ValueError if format is not correct
        raise ValueError

def format_date(hour, minute, meridiem):
    # if meridiem is AM, 12:00 is actually 00:00, other hours are the same
    if meridiem == "AM":
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    # if meridiem is PM,  12:00 is the same, are hours are added 12
    if meridiem == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    
    # if minutes are None, so only hours were entered and minutes are 00 
    if minute == None:
        new_minute = "00"
        new_time = f"{new_hour:02}" + ":" + new_minute
    else:
        new_time = f"{new_hour:02}" + ":" + minute
    return new_time


if __name__ == "__main__":
    main()
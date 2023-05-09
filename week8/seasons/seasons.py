# დავალება #36 - Seasons of Love
from datetime import date, datetime
import sys
import inflect


def main():
    usr_birthday = input("Date of Birth: ")
    check_format(usr_birthday)
    print(get_minutes(usr_birthday))
    
   
def get_minutes(user_data):

    # convert dates into datetime object
    date1 = datetime.strptime(str(date.today()), '%Y-%m-%d')
    date2 = datetime.strptime(user_data, '%Y-%m-%d')

    # find difference between dates in minutes
    difference = date1 - date2
    minutes = int(difference.total_seconds()) / 60

    # check if user entered date before today
    if minutes <= 0:
        sys.exit("Ivalid date")
    else:
        words  = inflect.engine().number_to_words(minutes)
        words = words.replace(" and", "")
        words = words.replace("point zero", "minutes")
        return words.capitalize()
    

# check if user enters correct format dates
def check_format(data):
    try:
        y, m, d = data.split("-")
        if len(y) != 4:
            sys.exit("Invalid date")
        if int(m) > 12 or int(m) <= 0:
            sys.exit("Invalid date")
        if int(d) > 31 or int(d) <= 0:
            sys.exit("Invalid date")
    except ValueError:
        sys.exit("Invalid date")
        

if __name__ == "__main__":
    main()
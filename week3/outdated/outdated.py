# დავალება #21 - Outdated

month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# ask user to input date
while True:
    user_input = input("Date: ").strip()

    # try to split input by "/"
    try:
        m, d, y = user_input.split("/")

        # check if d is between 1 and 31, and month is between 1 and 12
        if (1 <= int(m) <= 12) and (1 <= int(d) <= 31):
            break
    except:

        # try remove "," and split input by space 
        if "," in user_input:
            try:
                m, d, y = user_input.replace(",", "").split(" ")
                
                # find a number of month
                m = month.index(m.title()) + 1


                # check if d is between 1 and 31, and month is between 1 and 12
                if (1 <= int(m) <= 12) and (1 <= int(d) <= 31):
                    break
            except:
                pass

# if day or month is less than 10, add 0 before 
print(f"{y}-{int(m):02}-{int(d):02}")

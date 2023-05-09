# დავალება #10 - Meal Time

def main():
    time = input("What time is it? ")
    time_number = convert(time)
    if 7 <= time_number <= 8:
        print("breakfast time")
    elif 12 <= time_number <= 13:
        print("lunch time")
    elif 18 <= time_number <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + (float(minutes) / 60)


if __name__ == "__main__":
    main()


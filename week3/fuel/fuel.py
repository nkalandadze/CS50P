# დავალება #18 - Fuel Gauge
def main():
    fraction = round(get_fraction())

    if fraction <= 1:
      print("E")
    elif fraction >= 99:
      print("F")
    else:
      print(f"{fraction}%")


def get_fraction():
    while True: 
        user_input = input("Fraction: ")
        try:
            x,y = user_input.split("/")
            f = int(x) / int(y) * 100
            if f <= 100:
               return f
        except (ValueError, ZeroDivisionError):
            pass

main()


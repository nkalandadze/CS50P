# დავალება #31 - Refueling
def main():
   while True:
      fraction = input("Fraction: ")
      try:
         percentage = convert(fraction)
         output = gauge(percentage)
         print(output)
         break
      except (ValueError, ZeroDivisionError):
         pass


def convert(fraction):
    try:
      x,y = fraction.split("/")
      x = int(x)
      y = int(y)
      f = x / y * 100
      if x > y or x < 0 or y < 0:
          raise ValueError
      if y == 0:
          raise ZeroDivisionError
      return f
    except (ValueError, ZeroDivisionError):
       raise


def gauge(percentage):
    if percentage <= 1:
      return ("E")
    elif percentage >= 99:
      return ("F")
    else:
      return (f"{percentage}%")

if __name__ == "__main__":
   main()
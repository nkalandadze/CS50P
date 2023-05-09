# დავალება #24 - Adieu, Adieu
import inflect
p = inflect.engine()

# create emply list for names
names = []

# while user press ctrl D, create a list of names he/she will enter
while True:
  try:
    names.append(input("Enter name: "))
  # break the while loop after user press ctrl D
  except EOFError:
    break

names = p.join(names)
print(f"Adieu, adieu, to {names}")

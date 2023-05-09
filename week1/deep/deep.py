# დავალება #7 - Deep Thought
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# Version 1
# if answer == "42" or answer.lower() == "forty-two" or answer.lower() == "forty two":
#     print("Yes")
# else:
#     print("No")

# Version 2
match answer.lower().strip():
  case "42" | "forty-two" | "forty two":
    print("Yes")
  case _:
    print("No")
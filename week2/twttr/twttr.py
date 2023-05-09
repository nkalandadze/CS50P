# დავალება #15 - Just setting up my twttr

vowels = ["a", "e", "i", "o", "u"]

user_input = input("Input: ").strip()
output = ""

for i in range(len(user_input)):
    if user_input[i].lower() in vowels:
        continue
    else:
        output = output + user_input[i]

print(f"Output: {output}")
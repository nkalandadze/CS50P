# დავალება #22 - Emojize
import emoji

# ask user to input name of emoji
user_input = input("Input: ")

# convert inputed text to real emoji
output = emoji.emojize(user_input, language='alias')


print(f"Output: {output}")


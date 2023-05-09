# დავალება #23 - Frank, Ian and Glen’s Letters
from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
# get list of fonts
fonts = figlet.getFonts()

# get random font if user doesn't get any font name
if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(fonts))

# check if user gets correct font name and assing is to font name
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
    figlet.setFont(font = sys.argv[2])

# exit with "ivalid usage" text printed
else:
    sys.exit("Invalid usage")

# ask user to input text
txt = input("Input: ")

# print text with new font
print(figlet.renderText(txt))

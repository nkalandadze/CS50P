# დავალება #35 - CS50 P-Shirt
import sys
from PIL import Image, ImageOps
from os.path import splitext

def main():
    check_inputs()
    try:
        # try to open file
        input_image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist ")

    # open shirt image
    shirt_image = Image.open("shirt.png")
    # get size of shirt image
    size = shirt_image.size
    # resize image to fit shirt
    new_image = ImageOps.fit(input_image, size)
    # Paste shirt in new image
    new_image.paste(shirt_image, shirt_image)
    # Create output image
    new_image.save(sys.argv[2])


def check_inputs():

    # check if user didn't enter 2 file names
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # check if user entered more than 2 file name
    elif len(sys.argv) > 3:
        sys.exit("Too many command_line arguments")
    # check if input file is Image format 
    elif splitext(sys.argv[1])[1] not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Input does not exist")
     # check if output file is Image format 
    elif splitext(sys.argv[2])[1] not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid output")
     # check if input file and output file have same extension
    elif splitext(sys.argv[1])[1] != splitext(sys.argv[2])[1]:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
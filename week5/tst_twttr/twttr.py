# დავალება #15 - Just setting up my twttr

def main():
    user_input = input("Input: ").strip()
    output = shorten(user_input)
    print(f"Output: {output}")
    


def shorten(word):
    output = ""
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(len(word)):
        if word[i].lower() in vowels:
            continue
        else:
            output = output + word[i]

    return(output)

if __name__ == "__main__":
    main()
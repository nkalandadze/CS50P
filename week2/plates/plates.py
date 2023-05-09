# დავალება #16 - Vanity Plates
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
    # check if plate size is more than 2 characters and equal or less than 6 characters
    if len(s) < 2 or len(s) > 6:
        return False
    
    # check if first and second characters are letters
    elif s[0].isdigit() or s[1].isdigit():
        return False
    
    # check if any periods, spaces, or punctuation are used
    if not s.isalnum():
        return False
    
    # check if first digit is 0
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i-1] == "0" and s[i-2].isalpha():
                return False
            
            # check if letter used after digit
            for j in range(i, len(s)):
                if s[j].isalpha():
                    return False
                
    return True


main()
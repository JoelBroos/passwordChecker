# Project: Password checker
# Joel Broos 

# ASCII table: numbers:48-57, CAPITALS:65-90, lowerCase:97-122

def pWordSet(pWordList):
    count = 0
    twoDigCount = 0
    if len(pWordList) >= 8:  # Check if length of password is at least eight
        for a in pWordList:
            # Conditional statement to check if certain character in password is a number or letter
            if (48 <= ord(a) <= 57) or (65 <= ord(a) <= 90) or (97 <= ord(a) <= 122):
                count += 1
        # If count equals the length of the password that means all the characters are alphanumeric
        if count == len(pWordList):
            for b in pWordList:
                # Check if password contains at least two numbers
                if 48 <= ord(b) <= 57:
                    twoDigCount += 1
                # If twoDigCount is >= than two that means there are at least two numbers
                    if twoDigCount >= 2:
                        return True


def main():
    password = input('Enter a string for password: ')
    pWordList = list(password)
    if pWordSet(pWordList):
        print("Valid password")
    else:
        print('Invalid password')

main()
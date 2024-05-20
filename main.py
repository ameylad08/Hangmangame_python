import random

print("Welcome To HangMan")
print("--------------------------------------------------------")

worddictionary = ["python", "coding", "Youtube", "SmartPhone", "Cabbage", "Jewelry", "Oil", "Lantern", "Keyboard"]

# Choosing a Random Word
randomword = random.choice(worddictionary)

for x in randomword:
    print("_", end=" ")


def print_hangman(wrong):
    if (wrong == 0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif (wrong == 1):
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif (wrong == 2):
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif (wrong == 3):
        print("\n+---+")
        print(" O   |")
        print("/|   |")
        print("     |")
        print("    ===")
    elif (wrong == 4):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("     |")
        print("    ===")
    elif (wrong == 5):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/    |")
        print("    ===")
    elif (wrong == 6):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("    ===")


def printword(guessedletter):
    counter = 0
    rightletter = 0
    for char in randomword:
        if (char in guessedletter):
            print(randomword[counter], end=" ")
            rightletter += 1
        else:
            print(" ", end=" ")
        counter += 1
    return rightletter


def printlines():
    print("\r")
    for char in randomword:
        print("\u203E", end=" ")


length_of_word_to_guess = len(randomword)
amount_of_times_wrong = 0
current_guess_index = 0
current_letter_guessed = []
current_letter_right = 0

while (amount_of_times_wrong != 6 and current_letter_right != length_of_word_to_guess):
    print("\nLetters Guessed So Far: ")
    for letter in current_letter_guessed:
        print(letter, end=" ")
    # prompt the user for the input
    letterGuessed = input("\nGuess a Letter: ")
    # user is right
    if (randomword[current_guess_index] == letterGuessed):
        print_hangman(amount_of_times_wrong)
        # print word
        current_guess_index += 1
        current_letter_guessed.append(letterGuessed)
        current_letter_right = printword(current_letter_guessed)
        printlines()
    # user is wrong
    else:
        amount_of_times_wrong += 1
        current_letter_guessed.append(letterGuessed)
        # update the drawing
        print_hangman(amount_of_times_wrong)
        #printword
        current_letter_right = printword(current_letter_guessed)
        printlines()

print("Game is Over !!!!! \t Thank you For Playing :)")

import random

# Part 1: Ask the user to guess a word
def guess_word():
    
    # A. Ask the user to guess a 5 letter word and store it in a varible called guess
    
    # B. Keep asking until the word has exactly 5 letters
    while ______________________________:
        guess = input("Guess must be a 5-letter word. Try again: ").lower()
    
    return guess


def generate_output(secret, guess):
    GREEN = "🟩"   # Letter guessed in the correct position
    YELLOW = "🟨"  # Letter exists in the word but not in this position
    WHITE = "⬜"   # Letter does not exist in the word

    visual_chars = ""     # Stores the letters in the guess
    color_positions = ""  # Stores the matching color boxes

    # A. Loop through each letter in the guess
    for i in range(_____):
        # B. If the letter in guess at this position is the same as the letter in secret at this position
        if ____________________________:
            # C. append the letter to visual_chars and append GREEN to color_positions
        # D. Else if the current letter is in the secret
        elif ____________________________:
            #E.append the letter to visual_chars and append YELLOW to color_positions
        # F. Else if neither of th above is true
        else:
            # G. append the letter to visual_chars and append WHITE to color_positions

    # H. Print out visual_chars and color_positions  



def main():
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    print("Welcome to wordle! Type a 5 letter word to begin!")

    num_guesses = 0
    secret = random.choice(words)
    correct_guess = False
    while (num_guesses < 5):
        guess = guess_word()
        generate_output(secret, guess)

        if (guess == secret):
            print("Conrgats! You guessed in " + str(num_guesses + 1) + " guessed")
            correct_guess = True
            break
        num_guesses += 1
    if (not correct_guess):
        print("The words was " + secret + " - Try again next time")
    
main()
import random

def guess_word():
    guess = input("Enter a 5 letter word:").lower()
    while(len(guess) < 5 or len(guess) > 5):
        guess = input("Guess must be a 5 letter word: Enter a word ").lower()
    return guess



def generate_output(secret, guess):
    GREEN = "🟩"
    YELLOW = "🟨"
    WHITE = "⬜"
    visual_chars = ""
    color_positions = ""
    for i in range(5):
        if guess[i] == secret[i]:
            visual_chars += guess[i] + " "
            color_positions += GREEN

        elif guess[i] in secret:
            visual_chars += guess[i] + " "
            color_positions += YELLOW

        else:
            visual_chars += guess[i] + " "
            color_positions += WHITE
            
    print(visual_chars)
    print(color_positions)



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
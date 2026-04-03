import random


# PART 1: Ask user to guess the word
def guess_word():
    # A. Ask the user to guess the word once and save their answer in a variable

    # B. Using a loop, check if the user's guess is 5 letters. If it is not, ask the user to guess again.

    # C. Once the user has typed in a 5-letter word, return it.
    


# PART 2: Determine the outcome of each guess
def generate_output(secret, guess):
    GREEN = "🟩"   # Letter guessed in the correct position
    YELLOW = "🟨"  # Letter exists in the word but not in this position
    WHITE = "⬜"   # Letter does not exist in the word

    visual_chars = ""     # Stores the letters in the guess
    color_positions = ""  # Stores the matching color boxes
    
    # A. Write a loop that runs 5 times
   
   
        # B. If the letter in guess at this position is the same as the letter in secret at this position
      
      
            # C. if so, append the letter to visual_chars and append GREEN to color_positions
           
           
        # D. Else if the current letter is in the secret
       
       
            # E. Append the letter to visual_chars and append YELLOW to color_positions
          
        
        # F. Else if neither of th above is true
   
   
            # G. Add the current letter to visual_chars and add WHITE to color_positions
          
          
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
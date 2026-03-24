import random

# Predefined word list
words = ["apple", "tiger", "chair", "table", "pizza"]

# Choose random word
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("🎮 Welcome to Hangman Game!")

# Game loop
while wrong_guesses < max_attempts:
    display_word = ""
    
    # Show guessed letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\nWord:", display_word.strip())
    print("Wrong attempts left:", max_attempts - wrong_guesses)
    
    # Check win condition
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break
    
    # Take input
    guess = input("Enter a letter: ").lower()
    
    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Enter a single valid letter!")
        continue
    
    # Check if already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue
    
    guessed_letters.append(guess)
    
    # Check correct or wrong
    if guess not in word:
        wrong_guesses += 1
        print("❌ Wrong guess!")

# If user loses
if wrong_guesses == max_attempts:
    print("\n💀 Game Over! The word was:", word)
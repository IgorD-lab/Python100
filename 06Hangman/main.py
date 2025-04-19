import random
from resources.hangman_words import word_list
from resources.art import stages, logoHangman

# Initial setup
print(logoHangman)
correct_guesses = []
wrong_guesses = []
lives = 6
end_of_game = False
word = random.choice(word_list)

print(f'Psst, the solution is {word}.')

for i in word:
    correct_guesses.append("_")

# Guessing
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in correct_guesses or wrong_guesses:
        print(f"You've already guessed {guess}")
    
    if guess not in word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        wrong_guesses.append(guess) 
        if lives == 0:
            print("You lose.")
            end_of_game = True
             
    for i in range(len(word)):
        if guess == word[i]:
            correct_guesses[i] = guess
   
    print(f"Wrong guesses: {wrong_guesses}") 
    print(f"{' '.join(correct_guesses)}")
    
    if "_" not in correct_guesses:
        end_of_game = True
        print("You win.")    
    
    print(stages[lives]) 
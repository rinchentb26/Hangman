import random
from hangman_art import stages,logo
from hangman_words import word_list

#variables endGame and lives initially set to False and 6
endGame=False
lives=6

print(logo)
chosen_word=random.choice(word_list)
print(chosen_word)

#create a list display[] which will eventually reveal the secret word as the user guesses
display=[]
for _ in chosen_word:
    display.append('_')

#main loop that runs until endGame=True 
while not endGame:
    guess=input("Guess a letter: ").lower()
    #if user hasn't already guessed that letter
    if guess not in display:
        for pos in range(len(chosen_word)):
            if guess==chosen_word[pos]:
                display[pos]=guess
        if guess not in chosen_word:
            lives-=1
            print(f"You guessed {guess},that's not in the word.You lose a life.")
            if lives==0:
              endGame=True
              print("Game over 💀 . You lost all your lives.")
        if "_" not in display:
            endGame=True
            print("Victory 🥳 .You guessed the word.")
    #if user has already guessed that letter
    else:
        print(f"You've already guessed {guess}. Try again!")
    print(" ".join(display))
    print(stages[lives])






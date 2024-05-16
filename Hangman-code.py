# Hangman Game:

import random 
import words
from rich.console import Console

stages = ["""
    +---+
    |   |
        |
        |
        |
        |
    =========  
      
""","""
    +---+
    |   |
    O   |
        |
        |
        |
    =========

""","""
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    
""","""
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    
""","""
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
    
""","""
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
    
""","""
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========  
      
"""]

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
                   

print(logo)

any_letter = random.choice(words.word_list)

lst = []
for _ in any_letter:
    lst.append("_")

count = 0
while True:
    guess = input("Guess a letter:").lower()
    
    if (guess in lst):
        print(f"\nYou have already guessed '{guess}'.Guessed Another letter.\n")
        guess = input("Guess a letter:").lower()
        
    console = Console()
    console.clear()
        
    for item in range(len(any_letter)):
        if (guess == any_letter[item]):
            lst[item] = any_letter[item]
                  
    for j in lst:
        print(j, end = " ")
    print("\n")  
    
    if (guess in any_letter):
        print(f"You choose '{guess}' which is in word. Keep Going!")
        print(stages[count])
    else:
        count += 1
        print(f"You choose '{guess}' which is not in word. You lose a life.")
        print(stages[count])
        if (count > len(stages)-2):
            print("You Lose\n")
            print(f"Correct answer is {any_letter}\n")
            break
        
    if ("_" not in lst):
        print("You Win.")
        break

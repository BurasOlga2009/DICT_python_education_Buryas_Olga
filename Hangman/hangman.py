print("HANGMAN")
print("The game will be available soon.")
print("HANGMAN")
word = input("Guess the word: > ")
if word == "python":
    print("You survived!")
else:
    print("You lost!")
import random
print("HANGMAN")
words =['python','java','javascript','php']
target_word = random.choice(words)
word = input("Guess the word: > ")
if word == target_word:
    print("You survived!")
else:
    print("You lost!")
import random
print("HANGMAN")
words =['python','java','javascript','php']
target_word = random.choice(words)
hint = target_word[:3] + '-' * (len(target_word) - 3)
word = input(f"Guess the word {hint}: > ")
if word == target_word:
    print("You survived!")
else:
    print("You lost!")
import random
print("HANGMAN")
words =['python','java','javascript','php']
target_word = random.choice(words)
guessed_word = ['-'] * len(target_word)
attempts = 8
while attempts > 0:
    print()
    print("".join(guessed_word))
    user_input = input("Input a letter: > ")
    if user_input in target_word:
        for i, letter in enumerate(target_word):
            if letter == user_input:
                guessed_word[i] = user_input
    else:
        print("That letter doesn`t appear in the word")
    attempts -=1
print("Thanks for playing!")
print("We`ll see how well you in the next stage")
import random
print("HANGMAN")
words = ['python', 'java', 'javascript', 'php']
target_word = random.choice(words)
guessed_word = ['-'] * len(target_word)
attempts = 8
while attempts > 0:
    print()
    print("".join(guessed_word))
    if '-' not in guessed_word:
        print("You guessed the word!")
        print("You survived!")
        break
    user_input = input("Input a letter: > ")
    if user_input in target_word:
        if user_input in guessed_word:
            print("No improvements")
            attempts -= 1
        else:
            for i, letter in enumerate(target_word):
                if letter == user_input:
                    guessed_word[i] = user_input
    else:
        print("That letter doesn't appear in the word")
        attempts -= 1
else:
    print("You lost!")
import random

print("HANGMAN")
words = ['python', 'java', 'javascript', 'php']
target_word = random.choice(words)
guessed_word = ['-'] * len(target_word)
guessed_letters = set()
attempts = 8
while attempts > 0:
    print()
    print("".join(guessed_word))
    if '-' not in guessed_word:
        print("You guessed the word!")
        print("You survived!")
        break
    user_input = input("Input a letter: > ")
    if len(user_input) != 1:
        print("You should input a single letter.")
        continue
    if not ('a' <= user_input <= 'z'):
        print("Please enter a lowercase English letter.")
        continue
    if user_input in guessed_letters:
        print("You've already guessed this letter.")
        continue
    guessed_letters.add(user_input)
    if user_input in target_word:
        for i, letter in enumerate(target_word):
            if letter == user_input:
                guessed_word[i] = user_input
    else:
        print("That letter doesn't appear in the word")
        attempts -= 1
else:
    print("You lost!")






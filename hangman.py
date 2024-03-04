import random
from words import *

cho_word=random.choice(words)
word_display=['_' for _ in cho_word]
print(word_display)
attempt=10
print("welcome to hangman")

while attempt >0 and "_" in word_display:
    print("\n" + ' ' .join(word_display))
    guess=input("guess a letter: ").lower()
    if guess in cho_word:
        for index,letter in enumerate(cho_word):
            if letter==guess:
                word_display[index]=guess
    else:
        print("thst letter doesnot appear in the word")
        attempt-=1

if '_' not in word_display:
    print("you guessed the word")
    print(' '.join(word_display))
    print("you survived")
else:
    print("you ran out of attempts the word was :"+cho_word)
    print("you lost")
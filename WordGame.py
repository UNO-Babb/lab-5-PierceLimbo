#Pierce Limbo Word Game 9/28/2025

import random
from collections import Counter

def inWord(letter, word):
    if not letter or not word:
        return false
    return letter.lower() in word.lower()


def inSpot(letter, word, spot):
    if not letter or not word:
        return false
    if spot < 0 or spot >= len(word):
        return false
    return word[spot].lower() == letter.lower()
    

def rateGuess(myGuess, word):
    guess = myguess.lower()
    target = word.lower()
    n = len(target)
    result = ['*'] * n

counts = counter(target)

for i in range(n):
        if guess[i] == target[i]:
            result[i] = guess[i].upper()
            counts[guess[i]] -= 1  

    for i in range(n):
        if result[i] == '*':
            ch = guess[i]
            if counts.get(ch, 0) > 0:
                result[i] = ch.lower()
                counts[ch] -= 1

    return "".join(result)

def load_words():
    try:
        with open("words.txt", "r", encoding="utf-8") as f:
            words = [w.strip().lower() for w in f.read().splitlines() if len(w.strip()) == 5 and w.strip().isalpha()]
            if words:
                return words
    except FileNotFoundError:
        pass

    return [
        "apple", "brace", "crane", "delta", "eager",
        "flame", "grape", "humid", "ivory", "jelly",
        "lemon", "noble", "ocean", "pride", "round",
        "scene", "truth", "ultra", "vigor", "woven"
    ]

def main():
    wordList = load_words()
    todayWord = random.choice(wordList)
    
    attempts = 6
    print("Guess the word")

    for turn in range(1, attempts + 1):
        while True:
            myGuess = input(f"Attempt {turn}/{attempts} - keep guessing!: ").strip().lower()
            if len(myGuess) == 5 and myGuess.isalpha():
                break
            print("Your guess needs to be 5 letters.")

        if myGuess == todayWord:
            print("".join([c.upper() for c in myGuess]))
            print("Correct :)")
            return
        else:
            feedback = rateGuess(myGuess, todayWord)
            print(feedback)

    print(f"\n FAIL!!!!! The word was: {todayWord.upper()}")

if __name__ == '__main__':
    main()



if __name__ == '__main__':
  main()

guessedLetters = []

for i in range(0, 5):
    currGuess = input("추측 문자: ").strip().lower()
    guessedLetters.append(currGuess)

guessedLetters.sort()

# print(guessedLetters) <= dirty

for letter in guessedLetters:
    print(letter)

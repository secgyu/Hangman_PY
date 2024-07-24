guessedLetters = []

# Test
# for i in range(0, 5):
# currGuess = input("추측 문자: ").strip().lower()
# guessedLetters.append(currGuess)

if len(guessedLetters) > 0:
    youTried = ""

    for letter in guessedLetters:
        youTried += letter

    print("시도한 문자: ", youTried)

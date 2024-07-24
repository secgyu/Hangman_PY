gameWord = "apocalypse"
guessedLetters = ["a", "e"]
maskChar = "_"

displayWord = ""

for letter in gameWord:

    if letter in guessedLetters:
        displayWord += letter
    else:
        displayWord += maskChar

print("원래 단어: ", gameWord)
print("마스킹한 단어: ", displayWord)

import random


def draw_hangman(lives_used):
    print(" |---------")
    print(" | /      |")
    print(" |/       |")
    if lives_used >= 1:
        print(" |       ( )")
    else:
        print(" |")
    if 2 <= lives_used <= 3:
        print(" |        |")
    elif lives_used == 4:
        print(" |       /|")
    elif lives_used >= 5:
        print(" |       /|\\")
    else:
        print(" |")
    if 2 <= lives_used <= 3:
        print(" |        |")
    elif lives_used == 4:
        print(" |      / |")
    elif lives_used >= 5:
        print(" |      / | \\")
    else:
        print(" |")
    if lives_used >= 3:
        print(" |        |")
    else:
        print(" |")
    if lives_used == 6:
        print(" |       /")
    elif lives_used == 7:
        print(" |       / \\")
    else:
        print(" |")
    print("---")
    print()


maxLives = 7
maskChar = "_"
livesUsed = 0
guessedLetters = []
gameWords = ["anvil", "boutique", "cookie", "fluff", "jazz", "pneumonia",
             "sleigh", "society", "topaz", "tsunami", "yummy", "zombie"]
gameWord = random.choice(gameWords)
displayWord = maskChar * len(gameWord)

while gameWord != displayWord and livesUsed < maxLives:
    print(displayWord)

    if len(guessedLetters) > 0:
        youTried = "".join(guessedLetters)
        print("시도한 문자:", youTried)

    print(maxLives - livesUsed, "번 남았습니다.")

    draw_hangman(livesUsed)
    currGuess = input("추측 문자: ").lower()

    while len(currGuess) != 1:
        currGuess = input("한 문자씩 입력하세요.").lower()

    if currGuess in guessedLetters:
        print("이미 추측한 문자입니다.", currGuess)
    else:
        guessedLetters.append(currGuess)
        guessedLetters.sort()
        displayWord = ""
        for letter in gameWord:
            if letter in guessedLetters:
                displayWord += letter

            else:
                displayWord += maskChar

        if currGuess in gameWord:
            print("올바른 추측입니다.")

        else:
            print("틀렸습니다.")
            livesUsed += 1

if displayWord == gameWord:
    print("여러분이 이겼습니다. 단어는", gameWord, "입니다!")
else:
    print("여러분이 졌습니다. 정답:", gameWord)
draw_hangman(livesUsed)

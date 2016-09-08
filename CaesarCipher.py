import enchant


def solveCaesarCipher(text):
    dictionary = enchant.Dict("en_US")

    print("\n")
    print("\tRunning Caesar Cipher on input string " + text)
    print("\tAll possible solution strings : \n")
    possibleAnswers = []
    for i in range(1, 26):
        newStr = ""
        for l in text:
            if ord("a") <= ord(l) <= ord("z"):  # lower case
                newStr += chr(ord(l) + i) if ord(l) + i <= ord("z") else chr(ord(l)+i-26)
            elif ord("A") <= ord(l) <= ord("Z"):  # upper case
                newStr += chr(ord(l) + i) if ord(l) + i <= ord("Z") else chr(ord(l)+i-26)
            else:
                newStr += l

        print("\t" + newStr + "\n")
        wordsInStr = newStr.split(" ")
        correctness = 0
        for word in wordsInStr:
            result_word = ""
            for l in word:
                if l.isalnum() and l != " ":
                    result_word += l
            result_word.strip()
            try:
                correctness += 1 if dictionary.check(result_word) else -.5
            except:
                pass

        if correctness > 0:
            possibleAnswers.append(newStr)
    print("Caesar Cipher Detected Likely Answers: \n________________________________________________")
    for answer in possibleAnswers:
        print("\t" + answer)
    print("________________________________________________\n")
    if len(possibleAnswers) != 0:
        return possibleAnswers

# Test comment
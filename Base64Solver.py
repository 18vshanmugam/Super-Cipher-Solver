import enchant
import base64


def solvebase64values(text):

    dictionary = enchant.Dict("en_US")

    print("\n")
    print("\tRunning Base 64 Decoder on input string " + text)
    print("\tAll Possible Solutions strings : \n")

    text.strip()
    try:
        result = base64.standard_b64decode(text)
        result = result.decode("unicode_escape")
    except:
        print("base64 aborted")
        return ""

    print("\t" + result)

    result.strip()
    result_words = result.split(" ")
    correctness = 0

    for word in result_words:
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
        return result





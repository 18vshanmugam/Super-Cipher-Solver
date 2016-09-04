import enchant


def solveAtbashCipher(text):
    dictionary = enchant.Dict("en_US")

    print("\n")
    print("\tRunning Atbash Cipher on input string " + text + "\n")
    print("Atbash Ciphered Response")

    uppercase_shift = ord("A")
    lowercase_shift = ord("a")
    shifted_upper_z = ord("Z") - uppercase_shift
    shifted_lower_z = ord("z") - lowercase_shift

    result_string = ""
    for l in text:
        if ord("A") <= ord(l) <= ord("Z"):
            result_string += chr((shifted_upper_z - (ord(l)-uppercase_shift))+uppercase_shift)
        elif ord("a") <= ord(l) <= ord("z"):
            result_string += chr((shifted_lower_z - (ord(l)-lowercase_shift))+lowercase_shift)
        else:
            result_string += l

    print("________________________________________________")
    print("\t" + result_string)
    print("________________________________________________")

    result_string.strip()
    result_words = result_string.split(" ")
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
        return result_string


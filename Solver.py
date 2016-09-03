import CaesarCipher as c


def try_solve(text, allTests, caesar, RSA, base64):
    if caesar or allTests:
        c.solveCaesarCipher(text)
    print("c")

    print("%s couldn't be solved :(" % text)
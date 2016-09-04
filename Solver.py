import CaesarCipher as c
import Atbash as a
import AsciiValues as av

def try_solve(text, allTests, caesar, RSA, base64, atbash):
    solved = []

    text_type = input_is_num_or_hex(text)       # to avoid redundant checks i.e. testing a number for caesar shifts
    if text_type == "s" or text_type == "h":    # we have to test string ciphers for hex to because it is possible that
                                                # a hex valid string is also a valid cipher text sadly
        if caesar or allTests:
            solved.append(c.solveCaesarCipher(text))
        if atbash or allTests:
            solved.append(a.solveAtbashCipher(text))

    if text_type == "n" or text_type == "h":
        solved.append(av.solveAsciiValues(text, text_type))

    if len(solved) == 0 or solved[0] is None:
        print("""\n \tWe couldn't solve %s :(  We may not currently support the ciphertype that encrypts your message,
        or the translated message may not have appeared in our dictionary. If this is the case, you can check all of the
        output above to check if your solution was generated.""" % text)


    else:
        print("""\n\n\tAll likely solutions to the inputted text:
________________________________________________
        """)
        for s in solved:
            print("\t" + str(s))
        print("________________________________________________")


def input_is_num_or_hex(text):
    text = text.split(" ")
    try:
        for t in text:
            t = int(t, 10)
        return "n"
    except ValueError:
        try:
            for h in text:
                h = int(h, 16)
            return "h"
        except ValueError:
            return "s"


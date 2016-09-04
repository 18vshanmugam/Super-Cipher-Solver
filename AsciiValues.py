import enchant

def solveAsciiValues(text, text_type):
    dictionary = enchant.Dict("en_US")
    print("Attempting number to ascii conversion...")

    results = []
    text = text.split(" ")
    if text_type == "n":
        print("Treating number as base 10")
        possible_string = ""
        for q in text:
            try:
                possible_string += chr(int(q))
            except:
                print("Decimal Representation Aborted - Could not convert\n")
        try:
            print("\n" + possible_string + "\n")

            possible_string.strip()
            result_words = possible_string.split(" ")
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
                results.append(possible_string)


        except:
            print("Decimal Representation Aborted - Could not convert")


    print("Treating number as hexadecimal")
    possible_string = ""
    for q in text:
        try:
            possible_string += chr(int(q, 16))
        except:
            print("Hexadecimal Representation Aborted -  Could not convert")
            return
    try:
        print("\n" + possible_string + "\n")

        possible_string.strip()
        result_words = possible_string.split(" ")
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
            results.append(possible_string)

    except:
        print("Hexadecimal Representation Aborted -  Could not convert")


    return results


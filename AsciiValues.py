def solveAsciiValues(text, text_type):
    print("Attempting number to ascii conversion...")

    results = []
    text = text.split(" ")
    if text_type == "n":
        print("Treating number as base 10")
        result_string = ""
        for q in text:
            try:
                result_string += chr(int(q))
            except:
                print("Decimal Representation Aborted - Could not convert\n")
        try:
            print(result_string)

            results.append(result_string)
        except:
            print("Decimal Representation Aborted - Could not convert")


    print("Treating number as hexadecimal")
    result_string = ""
    for q in text:
        try:
            result_string += chr(int(q, 16))
        except:
            print("Hexadecimal Representation Aborted -  Could not convert")
            return
    try:
        print(result_string)
        results.append(result_string)
    except:
        print("Hexadecimal Representation Aborted -  Could not convert")

    return results
def solveCaesarCipher(text):
    print("\n")
    print("\tRunning Caesar Cipher...")
    print("\tAll possible solution strings : \n")
    for i in range (1, 26):
        newStr = ""
        for l in text:
            if ord("a") <= ord(l) <= ord("z"): #lower case
                newStr += chr(ord(l) + i) if ord(l) + i <= ord("z") else chr(ord(l)+i-26)
            elif ord("A") <= ord(l) <= ord("Z"):
                newStr += chr(ord(l) + i) if ord(l) + i <= ord("Z") else chr(ord(l)+i-26)
            else:
                newStr += l
        print("\t" + newStr + "\n")

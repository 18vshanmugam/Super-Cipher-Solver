def solveCaesarCipher(text):
    for i in range (1, 26):
        newStr = ""
        for l in text:
            if l == " ":
                newStr += l
            else:
                if ord(l) > ord("Z"): #lower case
                    newStr += chr(ord(l) + i) if ord(l) + i <= ord("z") else chr(ord(l)+i-26)
                else:
                    newStr += chr(ord(l) + i) if ord(l) + i <= ord("Z") else chr(ord(l)+i-26)
        print(newStr)

import sys
import Solver as s

if len(sys.argv) == 1:
    print("You need arguments! Call this program with the argument 'help' For help.")

elif len(sys.argv) == 2:
    if sys.argv[1] == 'help':
        print("""
        Welcome to Super Cipher Solver! With this utility you can solve some types of ciphers.
        We currently support base64 decoding, caesar ciphers, and certain RSA decryption techniques. \n
        Run this program by inputting your text, as well as any number of flags from below:

        -f or -fi or -file  :  Read input from a text file rather than inputting it into the command line \n
        -a or -all or -alltests : Run the full suite of cipher tests. Useful if you don't know what cipher you're dealing
        with \n
        -c or -caesar : Test the input against a Caesar Cipher only\n
        -b or -b64 or -base64 : Decode the string as base64 only\n
        -e or -example : See an example of a caesar shift being solved\n
        IMPORTANT : Multi-word text should be surrounded by quotes as such "I have too many words"

        """)
    elif sys.argv[1] == 'rhelp' or sys.argv[1] == 'rsahelp':
        print("""
        RSA is currently not functional. Check back later!""")
    elif sys.argv[1] == "-e" or sys.argv[1] == "-example":
        s.try_solve("Fhcre Pvcure Fbyire vf Fhcre Pbby!", False, True, False, False, False, False)

    else:  # 1 Arg, text to solve
        if input("Would you like to run the full suite of tests on this input? (Y/N)") == "Y":
            print("Running Full Suite...")
            s.try_solve(sys.argv[1], True, False, False, False, False, False)
        else:
            print("""You can run specific methods by using command line flags. Call this program with 'Help' for more
            information""")

else:  # > 1 args, some are flags
    file_input = False
    allTests = False
    caesar = False
    RSA = False
    base64 = False
    atbash = False
    ascii = False
    # other ciphers here

    for arg in sys.argv:
        if arg.lower() == "-f" or arg.lower() == "-fi" or arg.lower() == "-file":
            file_input = True
        elif arg.lower() == "-a" or arg.lower() == "-all" or arg.lower() == "-alltests":
            allTests = True
        elif arg.lower() == "-c" or arg.lower() == "-caesar":
            caesar = True
        elif arg.lower() == "-as" or arg.lower() =="-ascii":
            ascii = True
        elif arg.lower() == "-b" or arg.lower() == "-b64" or arg.lower() == "-base64":
            base64 = True
        elif arg.lower() == "-at" or arg.lower() == "-atbash":
            atbash = True
        else:
            if file_input:
                print("Attempting to read file " + arg + "...")
                with open(arg, "r") as file:
                    s.try_solve(file.read().strip(),  allTests, caesar, RSA, base64, atbash, ascii)
            else:
                s.try_solve(arg.strip(),  allTests, caesar, RSA, base64, atbash, ascii)


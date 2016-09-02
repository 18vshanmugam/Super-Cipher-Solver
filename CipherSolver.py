import sys
import Solver as s

if len(sys.argv) == 1:
    print("You need arguments! Call this program with the argument 'help' For Help!")

elif len(sys.argv) == 2:
    if sys.argv[1] == 'help':
        print("Placeholder help template")
    else:
        s.trySolve(sys.argv[1])

# elif len(sys.argv) == 3:
#     if sys.argv[1] == 'file':
#         with open(sys.argv[2], 'r') as file:
#             s.trySolve(file.read())
#             print(file.read)
# Broken rn


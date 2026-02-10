import sys

print("Script:", sys.argv[0])
print("Arguments:", sys.argv[1:])

if len(sys.argv) > 1:
    print("First arg:", sys.argv[1])

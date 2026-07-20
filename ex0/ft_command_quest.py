import sys

print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")

#arg_count = len(sys.argv) - 1

#if arg_count == 0:
#    print("No arguments provided!")
#else:
#    print(f"Arguments received: {arg_count}")
#    for i in range(arg_count):
#        print(f"Argument {i + 1}: {sys.argv[i + 1]}")
arg_count = len(sys.argv)
if (arg_count == 1):
    print("No arguments provided!")
else:
    all = sys.argv[1:]
    n = 1
    for i in all:
        print(f"Argument {n}: {i}")
        n = n + 1

print(f"Total arguments: {arg_count}")

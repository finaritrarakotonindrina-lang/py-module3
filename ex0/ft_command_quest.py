import sys

print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")

arg_count = len(sys.argv) - 1

if arg_count == 0:
    print("No arguments provided!")
else:
    print(f"Arguments received: {arg_count}")
    for i in range(arg_count):
        print(f"Argument {i + 1}: {sys.argv[i + 1]}")

print(f"Total arguments: {len(sys.argv)}")

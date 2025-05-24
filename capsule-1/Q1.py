name = input("What's your name? ")
print(f"Hello, {name}!")
a = input("Enter first number: ")
b = input("Enter second number: ")
print(f"These are the original numbers: {a} and {b}")
def swap(a, b):
    a, b = b, a
    return a, b
a, b = swap(a, b)
print(f"These are the swapped numbers: {a} and {b}")
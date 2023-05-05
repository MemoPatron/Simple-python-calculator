print(
    "Hi, this is an application that acts as a calculator. \nYou put in 2 numbers, A and B, and it will give you the sum of the 2 numbers."
)

while True:
    try:
        a = int(input("A: "))
        if a == int:
            continue

    except ValueError:
        print("Please enter valid numbers")

    else:
        break

while True:
    try:
        b = int(input("B: "))
        if b == int:
            continue

    except ValueError:
        print("Please enter valid numbers")

    else:
        break

print("Sum of A and B is", a + b)

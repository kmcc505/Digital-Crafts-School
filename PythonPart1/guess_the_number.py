secret_number = 5
print("I am thinking of a number between 1 and 10.")
while True:
    total = input("What is the number? ")
    if total != '5':
        print("Nope, try again. ")
    else:
        print("Yes! You Win! ")
        break


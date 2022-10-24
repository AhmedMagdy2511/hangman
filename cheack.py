def cheacker(num):
    if num%3 == 0 and num%5 == 0:
        print("FizzBuzz")
    elif num%3 == 0:
        print("Fizz")
    elif num%5 == 0:
        print("Buzz")
    else:
        print("this isn't divideable by 3 or 5")
number=int(input("enter number"))
cheacker(number)

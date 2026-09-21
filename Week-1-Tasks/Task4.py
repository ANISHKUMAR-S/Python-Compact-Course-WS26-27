def factorial_calculator(Num):
        factorial = 1
        for i in range(Num):
            factorial *= (Num - i)
        return factorial

if __name__ == '__main__':
    Num = int(input("Enter a number to calculate its factorial: "))
    if Num < 0:
        print("Negative numbers do not have factorials")
    else:
        print(f"The factorial of {Num} is: {factorial_calculator(Num)}")
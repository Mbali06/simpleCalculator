def add(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return "error: division by 0"
    else:
        return x / y

def calculator():
    print('Simple Calculator')
    print('1 Addition')
    print('2 Subtraction')
    print('3 Multiplication')
    print('4 Division')

    choice = input('Enter your choice(1/2/3/4): ')

    if choice in ('1','2','3','4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, '+', num2, '=', add(num1, num2))

        elif choice == '2':
            print(num1, '-', num2, '=', subtraction(num1, num2))


        elif choice == '3':
            print(num1, '*', num2, '=', multiplication(num1, num2))

        elif choice == '4':
            result = divide(num1, num2)
            print(num1, '/', num2, '=', result)

        else:
            print('Invalid choice')

        repeat = input("Do you want to Calculate again(y/n)?: ")
        if repeat.lower() == 'y':
            calculator()
        else:
            print('Goodbye!!')

calculator()
            
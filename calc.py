def add(x,y):
    result = int(x) + int(y)
    print(f'{x} plus {y} equals {result}')

def subtract(x,y):
    result = int(x) - int(y)
    print(f'{x} minus {y} equals {result}')

def multiply(x,y):
    result = int(x) * int(y)
    print(f'{x} times {y} equals {result}')

def divide(x,y):
    result = int(x) / int(y)
    print(f'{x} divided by {y} equals {result}')

if __name__ == '__main__':
    op = input('What kind of math are you trying to do? ')
    num_1 = input('number 1: ')
    num_2 = input('number 2: ')
    if op == 'add':
        add(num_1, num_2)
    elif op == 'subtract':
        subtract(num_1, num_2)
    elif op == 'multiply':
        multiply(num_1,num_2)
    elif op == 'divide':
        divide(num_1, num_2)
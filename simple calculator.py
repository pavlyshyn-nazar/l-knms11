while True:
 a = float(input('num 1 '))
 b = float(input('num 2 '))
 c = input('Please choose math operation')

 if c == '+':
    print (a + b)
 elif c == '*':
    print (a * b)
 elif c == '-':
    print(a - b)
 elif c == '/':
    if ( b==0):
        print('Realy? repeat math')
    else:
        print(a / b)
 else:print ('Lol, please choose math operation')
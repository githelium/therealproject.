try:
    print(eval(input()))
except (NameError, TypeError, ZeroDivisionError,SyntaxError):
    print('?')
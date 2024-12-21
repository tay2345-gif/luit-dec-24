try:
    value = int(input('Enter an integar: '))
    print('The inverse of', value, 'is', 1/value)
except ValueError:
    print('you did not provide a number, so i will not calculate the inverse')
except ZeroDivisionError:
    print('you provided 0 an divison by 0 is not possible')
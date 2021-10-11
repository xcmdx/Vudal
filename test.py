def check(string):
    try:
        string = int(string)
    except ValueError:
        print('\n',
            'aazdsad',
            '\n')
    return string

print(type(check(input())))
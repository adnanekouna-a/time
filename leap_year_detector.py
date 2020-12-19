
while True:
    input = input('Year : ')
    if input == '':
        exit()
    else:
        try:
            year = int(input)
            if year <= 0:
                raise ValueError
            else:
                if year % 4 == 0:
                    print(f'The year "{year}" is a leap year!')
                else:
                    print(f'The year "{year}" is a common year!')
        except ValueError:
            print('Enter a positive number!')

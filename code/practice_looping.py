total = 0

while True:
    user_input = input('Input a positive number [done to finish]: ')

    if user_input in ['done', 'finish', '0']:
        break
    elif int(user_input) > 100 or int(user_input) < 1:
        pass
    else:
        total += int(user_input)

print(f'total angka {total}')
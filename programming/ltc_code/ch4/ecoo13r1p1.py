next_number = int(input())

num_late = 0
num_waiting = 0

line = ''

while line != 'EOF':
    line = input()
    if line == 'TAKE':
        num_late = num_late + 1
        num_waiting = num_waiting + 1
        next_number = next_number + 1
        if next_number == 1000:
            next_number = 1
    elif line == 'SERVE':
        num_waiting = num_waiting - 1
    elif line == 'CLOSE':
        print(num_late, num_waiting, next_number)
        num_late = 0
        num_waiting = 0

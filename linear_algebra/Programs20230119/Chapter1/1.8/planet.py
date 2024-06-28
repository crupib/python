C = {'Earth': '3rd', 'Mars': '4th', 'Jupiter': '5th'}
for x in C:
    print(f'{x} is the {C[x]} planet in the solar system.')
print()
for x in sorted(C):
    print(f'{x} is the {C[x]} planet in the solar system.')

'''
Earth is the 3rd planet in the solar system.
Mars is the 4th planet in the solar system.
Jupiter is the 5th planet in the solar system.

Earth is the 3rd planet in the solar system.
Jupiter is the 5th planet in the solar system.
Mars is the 4th planet in the solar system.
'''

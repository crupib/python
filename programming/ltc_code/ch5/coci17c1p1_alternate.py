# Overall approach:
# Maintain a list of remaining cards, and remove cards that are picked up.
# Compared to the other provided solution, we have to maintain a longer list,
# and we need a loop to find the cards that are greater.


cards = ([2] * 4 + [3] * 4 + [4] * 4 + [5] * 4 + [6] * 4 + [7] * 4 + [8] * 4 +
         [9] * 4 + [10] * 16 + [11] * 4)

n = int(input())

in_hand = 0

for i in range(n):
    card_val = int(input())
    in_hand = in_hand + card_val
    cards.remove(card_val)

x = 21 - in_hand

num_greater = 0

for card in cards:
    if card > x:
        num_greater = num_greater + 1

if num_greater > 52 - n - num_greater:
    print('DOSTA')
else:
    print('VUCI')

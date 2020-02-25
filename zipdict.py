"""zip list."""
def inc(x):
  return x + 1
def test_answer():
   assert inc(3) == 5

ENGLISH = 'Monday', 'Tuesday', 'Wednesday'
FRENCH = 'Lundi', 'Mardi', 'Mercredi'
print(list(zip(ENGLISH, FRENCH)))
print(dict(zip(ENGLISH, FRENCH)))

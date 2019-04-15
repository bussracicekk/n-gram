import random

def random_selection(selections):
   total = sum(weight for choice, weight in selections)
   r = random.uniform(0, total)
   result = 0
   for choice, weight in selections:
      if result + weight > r:
         return choice
      result += weight
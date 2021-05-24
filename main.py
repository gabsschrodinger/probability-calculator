import copy
import random
import math

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for i, j in kwargs.items():
      for k in range(j):
        self.contents.append(i)

  def draw(self, n):
    if(n > len(self.contents)): return self.contents
    removed = []
    indexes = []
    for i in range(n):
      x = math.floor(random.random() * len(self.contents))
      while x in indexes:
        x = math.floor(random.random() * len(self.contents))
      indexes.append(x)
      removed.append(self.contents[x])
      self.contents.remove(removed[-1])
    removed.sort()
    return removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0
  for i in range(num_experiments):
    expected_balls_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    balls_drawn = hat_copy.draw(num_balls_drawn)
    for j in balls_drawn:
      if(j in expected_balls_copy): expected_balls_copy[j] -= 1
    success += 1
    for j in expected_balls_copy.values():
      if(j > 0):
        success -= 1
        break
  return success / num_experiments
import random

class CoinPrivatizer:
  _headsProbability = 0.5

  def __init__(self, headsProbability=0.5):
    self._headsProbability = headsProbability

  def privatize(self, data):
    if (type(data) != list):
      raise ValueError('Not a valid data input')
    return data

  def privatizeSingleAnswer(self, truth): 
    if (type(truth) != bool):
      raise ValueError('Truth is not a bool value')

    if (random.uniform(0, 1) > self._headsProbability): return truth
    if (random.uniform(0, 1) > self._headsProbability): return True
    return False
    
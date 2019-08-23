import random
import abstractPrivatizer

class CoinPrivatizer(abstractPrivatizer.AbstractPrivatizer):
  _headsProbability = 0.5

  def __init__(self, headsProbability=0.5):
    self.setHeadsProbability(headsProbability)
  
  def setHeadsProbability(self, probability):
    if (type(probability) != float):
      raise ValueError('Not a valid headsProbability value. It must be a float')
    if (probability < 0 or probability > 1):
      raise ValueError('Not a valid headsProbability value. It must be between 0 and 1')

    self._headsProbability = probability

  def privatizeSingleAnswer(self, value): 
    if (type(value) != bool):
      raise ValueError('Value is not a bool value')

    if (random.uniform(0, 1) > self._headsProbability): return value
    if (random.uniform(0, 1) > self._headsProbability): return True
    return False
    
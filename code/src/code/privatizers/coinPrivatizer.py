import random

class CoinPrivatizer:
  _headsProbability = 0.5

  def __init__(self, headsProbability=0.5):
    self.setHeadsProbability(headsProbability)
  
  def setHeadsProbability(self, probability):
    if (type(probability) != float):
      raise ValueError('Not a valid headsProbability value. It must be a float')
    if (probability < 0 or probability > 1):
      raise ValueError('Not a valid headsProbability value. It must be between 0 and 1')

    self._headsProbability = probability

  def privatize(self, data):
    if (type(data) != list):
      raise ValueError('Not a valid data input')
    
    resultData = []

    for listData in data:
      resultData.append(self.privatizeList(listData))
    
    return resultData

  def privatizeList(self, listData):
    if (type(listData) != list):
      raise ValueError('Not a list')
    resultList = []
    for singleData in listData:
      if (type(singleData) != bool):
        raise ValueError('Invalid value in list')
      resultList.append(self.privatizeSingleAnswer(singleData))
    return resultList

  def privatizeSingleAnswer(self, truth): 
    if (type(truth) != bool):
      raise ValueError('Truth is not a bool value')

    if (random.uniform(0, 1) > self._headsProbability): return truth
    if (random.uniform(0, 1) > self._headsProbability): return True
    return False
    
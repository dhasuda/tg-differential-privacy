import numpy as np

class LaplacePrivatizer:
  _mean = 0.0
  _scale = 1.0

  def __init__(self, scale=1.):
    if (type(scale) != float):
      raise ValueError('Not a valid scale')
    if (scale <= 0.0):
      raise ValueError('Not a valid scale')
    self._scale = scale

  def privatize(self, data):
    if (type(data) != list):
      raise ValueError('Not a list')
    
    privatizedData = []
    for value in data:
      privatizedList = self.privatizeList(value)
      privatizedData.append(privatizedList)
    return privatizedData

  def privatizeList(self, data):
    if (type(data) != list):
      raise ValueError('Not a list')
    
    privatizedList = []
    for value in data:
      privateValue = self.privatizeSingleAnswer(value)
      privatizedList.append(privateValue)
    return privatizedList

  def privatizeSingleAnswer(self, truth):
    sanitizedTruth = 0
    try:
      sanitizedTruth = float(truth)
    except:
      raise ValueError('Not valid value to be privatized')
    noise = np.random.laplace(self._mean, self._scale, 1)[0]
    return float(sanitizedTruth + noise)
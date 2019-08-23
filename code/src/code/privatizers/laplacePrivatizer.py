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
    if (type(data) == list):
      privatizedData = []
      for value in data:
        privatizedData.append(self.privatize(value))
      return privatizedData
    else:
      return self.privatizeSingleAnswer(data)

  def privatizeSingleAnswer(self, truth):
    sanitizedTruth = 0
    try:
      sanitizedTruth = float(truth)
    except:
      raise ValueError('Not valid value to be privatized')
    noise = np.random.laplace(self._mean, self._scale, 1)[0]
    return float(sanitizedTruth + noise)
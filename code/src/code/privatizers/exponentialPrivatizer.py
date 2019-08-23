import numpy as np
import abstractPrivatizer

class ExponentialPrivatizer(abstractPrivatizer.AbstractPrivatizer):
  _mean = 0.0
  _scale = 1.0

  def __init__(self, scale=1.):
    if (type(scale) != float):
      raise ValueError('Not a valid scale')
    if (scale <= 0.0):
      raise ValueError('Not a valid scale')
    self._scale = scale

  def privatizeSingleAnswer(self, value):
    sanitizedTruth = 0
    try:
      sanitizedTruth = float(value)
    except:
      raise ValueError('Not valid value to be privatized')
    noise = np.random.exponential(self._scale, 1)[0]
    return float(sanitizedTruth + noise)
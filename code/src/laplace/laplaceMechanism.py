import numpy as np

class LaplacianMethod:
  _mean, _scale = 0., 1.
  def __init__(self, mean = 0., scale = 1.):
    self._mean = mean
    self._scale = scale

  def generatePrivateAnswer(self, truth):
    sanitizedTruth = 0
    try:
      sanitizedTruth = float(truth)
    except:
      return 0
    noise = np.random.laplace(mean, scale, 1)[0]
    return sanitizedTruth + noise
  

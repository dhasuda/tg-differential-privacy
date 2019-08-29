import numpy as np

def fromRaw(rawData):
  if (type(rawData) != np.ndarray):
    raise ValueError('Raw data must be a numpy ndarray')

  adaptedData = []
  for data in rawData:
    if (type(data) != np.ndarray):
      raise ValueError('Raw data values must be numpy ndarrays')
    floatList = []
    for value in data:
      floatList.append(float(value))
    adaptedData.append(list(floatList))

  return adaptedData
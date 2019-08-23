from abc import ABC, abstractmethod

class AbstractPrivatizer(ABC):
  def privatize(self, data):
    if (type(data) == list):
      privatizedData = []
      for value in data:
        privatizedData.append(self.privatize(value))
      return privatizedData
    else:
      return self.privatizeSingleAnswer(data)
    
  @abstractmethod
  def privatizeSingleAnswer(self, value):
    pass
    
from abc import ABC, abstractmethod

class AbstractPrivatizer(ABC):
  def privatize(self, data, sensitivityValue=0.001):

    if (type(data) == list):
      privatizedData = []
      counter = 0
      sensitivity = sensitivityValue

      sensitivityList = []
      if (type(data[0]) == list):
          for i in range(len(data[0])):
            column = [row[i] for row in data]
            singleSensitivityValue = abs(max(column) - min(column))
            sensitivityList.append(singleSensitivityValue)

      for value in data:
        if (type(value) == list):
          sensitivity = sensitivityList
        else:
          if (type(sensitivityValue) == float):
            sensitivity = sensitivityValue
          else:
            sensitivity = sensitivityValue[counter]

        privatizedData.append(self.privatize(value, sensitivity))
        counter += 1
      
      return privatizedData

    else:
      return self.privatizeSingleAnswer(data, sensitivityValue)
    
  @abstractmethod
  def privatizeSingleAnswer(self, value):
    pass
    
from abc import ABC, abstractmethod

class AbstractPrivatizer(ABC):
  def privatize(self, data, averageValue=0.001):

    if (type(data) == list):
      privatizedData = []
      counter = 0
      average = averageValue

      averageList = []
      if (type(data[0]) == list):
          for i in range(len(data[0])):
            column = [row[i] for row in data]
            singleAverageValue = sum(column) / len(column)
            averageList.append(singleAverageValue)

      for value in data:
        if (type(value) == list):
          average = averageList
        else:
          if (type(averageValue) == float):
            average = averageValue
          else:
            average = averageValue[counter]

        privatizedData.append(self.privatize(value, average))
        counter += 1
      
      return privatizedData

    else:
      return self.privatizeSingleAnswer(data, averageValue)
    
  @abstractmethod
  def privatizeSingleAnswer(self, value):
    pass
    
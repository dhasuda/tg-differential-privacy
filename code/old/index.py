from coin import coinPrivacy
from laplace import laplaceMechanism
from fileHandler import FileHandler
from Plot import plotResults

def main():


  inputValues = FileHandler('../data/test.txt')
  coinOutputValues = FileHandler('../data/coinAnswer50.txt', 'w')
  laplaceOutputValues = FileHandler('../data/laplaceAnswer50.txt', 'w')

  coinMethod = coinPrivacy.CoinPrivateMethod()
  laplaceMethod = laplaceMechanism.LaplacianMethod()
  
  laplaceMean = 0.
  counter = 1
  originalYeses = 0
  originalNos = 0
  coinYeses = 0
  coinNos = 0

  for answer in inputValues.readLines():
    # Coin
    privateCoinAnswer = coinMethod.generatePrivateAnswer(True if answer == 'yes' else False)
    coinOutputValues.writeLine('yes' if privateCoinAnswer else 'no')

    # Laplace
    privateLaplaceAnswer = laplaceMethod.generatePrivateAnswer(1. if answer == 'yes' else -1.)
    laplaceMean = ((laplaceMean * counter) + privateLaplaceAnswer) / (counter + 1)
    counter += 1
    laplaceOutputValues.writeLine(str(privateLaplaceAnswer))

    # Data to plot
    if (answer == 'yes'):
      originalYeses += 1
    else:
      originalNos += 1
    if (privateCoinAnswer):
      coinYeses += 1
    else:
      coinNos += 1
    

  laplaceOutputValues.writeLine("Mean = " + str(laplaceMean))
  del coinOutputValues
  del laplaceOutputValues
  del inputValues

  total = originalNos + originalYeses

  print((originalYeses, coinYeses, coinYeses-total/4), (originalNos, coinNos, coinNos-total/4), ('Original', 'Coin mechanism', 'Processed'))
  plotResults.Plot.plot((originalYeses, coinYeses, coinYeses-total/4), (originalNos, coinNos, coinNos-total/4), ('Original', 'Coin mechanism', 'Processed'))

if __name__ == '__main__':
  main()
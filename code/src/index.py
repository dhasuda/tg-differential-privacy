from coin import coinPrivacy
from laplace import laplaceMechanism
from fileHandler import FileHandler

def main():
  inputValues = FileHandler('../data/test.txt')
  coinOutputValues = FileHandler('../data/coinAnswer50.txt', 'w')
  laplaceOutputValues = FileHandler('../data/laplaceAnswer50.txt', 'w')

  coinMethod = coinPrivacy.CoinPrivateMethod()
  laplaceMethod = laplaceMechanism.LaplacianMethod()
  
  laplaceMean = 0.
  counter = 1

  for answer in inputValues.readLines():
    # Coin
    privateCoinAnswer = coinMethod.generatePrivateAnswer(True if answer == 'yes' else False)
    coinOutputValues.writeLine('yes' if privateCoinAnswer else 'no')

    # Laplace
    privateLaplaceAnswer = laplaceMethod.generatePrivateAnswer(1. if answer == 'yes' else -1.)
    laplaceMean = ((laplaceMean * counter) + privateLaplaceAnswer) / (counter + 1)
    counter += 1
    laplaceOutputValues.writeLine(str(privateLaplaceAnswer))

  laplaceOutputValues.writeLine("Mean = " + str(laplaceMean))
  del coinOutputValues
  del laplaceOutputValues
  del inputValues

if __name__ == '__main__':
  main()
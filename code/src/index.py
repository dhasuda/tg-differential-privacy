from coin import coinPrivacy
from fileHandler import FileHandler

def main():
  print('Starting work')
  coinMethod = coinPrivacy.CoinPrivateMethod()
  coinMethod.printProb()

  inputValues = FileHandler('../data/test.txt')
  outputValues = FileHandler('../data/coinAnswer50.txt', 'w')
  for answer in inputValues.readLines():
    privateAnswer = coinMethod.generatePrivateAnswer(True if answer == 'yes' else False)
    outputValues.writeLine('yes' if privateAnswer else 'no')
  del inputValues
  del outputValues

if __name__ == '__main__':
  main()
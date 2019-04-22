import random

class CoinPrivateMethod:
  _headsProbability = 0.5
  def __init__(self, headsProbability=0.5):
    self._headsProbability = headsProbability

  def printProb(self):
    print(self._headsProbability)

  def generatePrivateAnswer(self, truth): 
    if (random.uniform(0, 1) > self._headsProbability): return truth
    if (random.uniform(0, 1) > self._headsProbability): return True
    return False


def main():
  print('This is the coin toss module')
  coinMethod = CoinPrivateMethod()
  coinMethod.printProb()

if __name__ == '__main__':
  main()
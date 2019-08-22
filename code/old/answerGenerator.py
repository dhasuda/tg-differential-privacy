import random
from fileHandler import FileHandler

FILE_NAME = '../data/test.txt'
YES_PROPORTION = 0.75
NUMBER_OF_PARTICIPANTS = 10000

def getRandomAnswer():
  if (random.uniform(0, 1) <= YES_PROPORTION): return True
  return False

def main():
  testFile = FileHandler(FILE_NAME, 'w')
  for _ in range(NUMBER_OF_PARTICIPANTS):
    answer = 'yes' if getRandomAnswer() else 'no'
    testFile.writeLine(answer)
  del testFile


if __name__ == '__main__':
  main()
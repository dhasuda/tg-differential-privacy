from fileHandler import FileHandler

def main():
  inputValues = FileHandler('../data/test.txt')
  coinOutputValues = FileHandler('../data/coinAnswer50.txt')

  original = []
  coin = []

  for answer in inputValues.readLines():
    original.append(True if answer == 'yes' else False)
  
  for answer in coinOutputValues.readLines():
    coin.append(True if answer == 'yes' else False)
  
  
  match = 0
  noMatch = 0
  for i in range(len(original)):
    if original[i] == coin[i]:
      match += 1
    else:
      noMatch += 1

  print (match, noMatch)

if __name__ == '__main__':
  main()
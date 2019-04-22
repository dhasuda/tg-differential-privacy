class FileHandler:
  def __init__(self, fileName, mode='r'):
    self._fileName = fileName
    self._mode = self.validMode(mode)
    self._file = open(fileName, mode)

  def readLines(self):
    return self._file.read().splitlines()

  def writeLine(self, content):
    if (self._mode == 'r'): return
    self._file.write(content + '\n')

  def __del__(self):
    self._file.close()

  def validMode(self, mode):
    if (mode == 'r' or mode == 'w' or mode == 'a'): return mode
    return 'r'

def main():
  print('This module handles read and write from .txt files')

if __name__ == '__main__':
  main()
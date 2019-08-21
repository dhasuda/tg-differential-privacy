import unittest
import coinPrivatizer

class PrivatizersTests(unittest.TestCase):
  _coinPrivatizer = coinPrivatizer.CoinPrivatizer()

  def testCoinPrivitizerInvalidDataInput(self):
    with self.assertRaises(ValueError) as context:
      self._coinPrivatizer.privatize(1)
    self.assertTrue('Not a valid data input' in context.exception)

  def testCoinSingleAnswerInvalidInput(self):
    with self.assertRaises(ValueError) as context:
      self._coinPrivatizer.privatizeSingleAnswer(2)
    self.assertTrue('Truth is not a bool value' in context.exception)

if __name__ == "__main__":
  unittest.main()
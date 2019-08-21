import unittest
import coinPrivatizer

class PrivatizersTests(unittest.TestCase):
  _coinPrivatizer = coinPrivatizer.CoinPrivatizer()

  def testCoinInitializer(self):
    with self.assertRaises(ValueError) as stringContext:
      coinPrivatizer.CoinPrivatizer('a')
    self.assertTrue('Not a valid headsProbability value. It must be a float' in stringContext.exception)

    with self.assertRaises(ValueError) as negativeContext:
      coinPrivatizer.CoinPrivatizer(-0.5)
    self.assertTrue('Not a valid headsProbability value. It must be between 0 and 1' in negativeContext.exception)

    with self.assertRaises(ValueError) as tooBigContext:
      coinPrivatizer.CoinPrivatizer(1.5)
    self.assertTrue('Not a valid headsProbability value. It must be between 0 and 1' in tooBigContext.exception)

    coinPrivit = coinPrivatizer.CoinPrivatizer(0.1)
    self.assertEqual(0.1, coinPrivit._headsProbability)
    coinPrivit.setHeadsProbability(0.6)
    self.assertEqual(0.6, coinPrivit._headsProbability)
  
  def testCoinPrivitizerInvalidDataInput(self):
    with self.assertRaises(ValueError) as context:
      self._coinPrivatizer.privatize(1)
    self.assertTrue('Not a valid data input' in context.exception)

  def testCoinSingleAnswerInvalidInput(self):
    with self.assertRaises(ValueError) as context:
      self._coinPrivatizer.privatizeSingleAnswer(2)
    self.assertTrue('Truth is not a bool value' in context.exception)

  def testCoinSingleAnswer(self):
    coinPrivit = coinPrivatizer.CoinPrivatizer(0.0)
    self.assertEqual(True, coinPrivit.privatizeSingleAnswer(True))
    self.assertEqual(False, coinPrivit.privatizeSingleAnswer(False))

    coinPrivit.setHeadsProbability(1.0)
    self.assertEqual(False, coinPrivit.privatizeSingleAnswer(True))
    self.assertEqual(False, coinPrivit.privatizeSingleAnswer(False))

if __name__ == "__main__":
  unittest.main()
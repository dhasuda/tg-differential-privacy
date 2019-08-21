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
  
  def testCoinPrivatizerInvalidDataInput(self):
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

  def testCoinPrivatizeListInvlidInput(self):
    with self.assertRaises(ValueError) as context:
      self._coinPrivatizer.privatizeList(True)
    self.assertTrue('Not a list' in context.exception)

    with self.assertRaises(ValueError) as context:
      self._coinPrivatizer.privatizeList([0, 1])
    self.assertTrue('Invalid value in list' in context.exception)


  def testCoinPrivatizeList(self):
    coinPriv = coinPrivatizer.CoinPrivatizer(1.0)
    testList = [True, False, True, False]
    resultList = coinPriv.privatizeList(testList)
    self.assertEqual([False, False, False, False], resultList)

    coinPriv.setHeadsProbability(0.0)
    testList = [True, False, True, False]
    resultList = coinPriv.privatizeList(testList)
    self.assertEqual([True, False, True, False], resultList)

    resultList = coinPriv.privatizeList([])
    self.assertEqual([], resultList)

  def testCoinPrivatizeInvalidInput(self):
    with self.assertRaises(ValueError) as context:
      self._coinPrivatizer.privatize(True)
    self.assertTrue('Not a valid data input' in context.exception)

  def testCoinPrivatize(self):
    coinPriv = coinPrivatizer.CoinPrivatizer(1.0)
    testData = [[True, False], [True, True], [False, False]]
    resultData = coinPriv.privatize(testData)
    self.assertEqual([[False, False], [False, False], [False, False]], resultData)

    coinPriv.setHeadsProbability(0.0)
    testData = [[True, False], [True, True], [False, False]]
    resultData = coinPriv.privatize(testData)
    self.assertEqual([[True, False], [True, True], [False, False]], resultData)

    resultList = coinPriv.privatize([])
    self.assertEqual([], resultList)

if __name__ == "__main__":
  unittest.main()
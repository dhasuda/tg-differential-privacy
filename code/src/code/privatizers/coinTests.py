import unittest
import coinPrivatizer

class CoinPrivatizersTests(unittest.TestCase):
  _coinPrivatizer = coinPrivatizer.CoinPrivatizer()

  def testCoinInitializer(self):
    self.assertRaises(ValueError, lambda: coinPrivatizer.CoinPrivatizer('a'))
    self.assertRaises(ValueError, lambda: coinPrivatizer.CoinPrivatizer(-0.5))
    self.assertRaises(ValueError, lambda: coinPrivatizer.CoinPrivatizer(1.5))

    coinPrivit = coinPrivatizer.CoinPrivatizer(0.1)
    self.assertEqual(0.1, coinPrivit._headsProbability)
    coinPrivit.setHeadsProbability(0.6)
    self.assertEqual(0.6, coinPrivit._headsProbability)

  def testCoinSingleAnswerInvalidInput(self):
    self.assertRaises(ValueError, lambda: self._coinPrivatizer.privatizeSingleAnswer(1))

  def testPrivatizeInvalidInput(self):
    self.assertRaises(ValueError, lambda: self._coinPrivatizer.privatize([True, False, 1]))
    self.assertRaises(ValueError, lambda: self._coinPrivatizer.privatize([[True, False], [1, 2]]))
    self.assertRaises(ValueError, lambda: self._coinPrivatizer.privatize([[True, False], 1]))

  def testCoinSingleAnswer(self):
    coinPrivit = coinPrivatizer.CoinPrivatizer(0.0)
    self.assertEqual(True, coinPrivit.privatizeSingleAnswer(True))
    self.assertEqual(False, coinPrivit.privatizeSingleAnswer(False))

    coinPrivit.setHeadsProbability(1.0)
    self.assertEqual(False, coinPrivit.privatizeSingleAnswer(True))
    self.assertEqual(False, coinPrivit.privatizeSingleAnswer(False))

  def testCoinPrivatizeList(self):
    coinPriv = coinPrivatizer.CoinPrivatizer(1.0)
    testList = [True, False, True, False]
    resultList = coinPriv.privatize(testList)
    self.assertEqual([False, False, False, False], resultList)

    coinPriv.setHeadsProbability(0.0)
    testList = [True, False, True, False]
    resultList = coinPriv.privatize(testList)
    self.assertEqual([True, False, True, False], resultList)

    resultList = coinPriv.privatize([])
    self.assertEqual([], resultList)

  def testCoinPrivatizeRecursiveList(self):
    coinPriv = coinPrivatizer.CoinPrivatizer(1.0)
    testData = [[True, False], [True, True], [False, False]]
    resultData = coinPriv.privatize(testData)
    self.assertEqual([[False, False], [False, False], [False, False]], resultData)

    testData = [[True, False], [True, True], [False, False], False, True]
    resultData = coinPriv.privatize(testData)
    self.assertEqual([[False, False], [False, False], [False, False], False, False], resultData)

    coinPriv.setHeadsProbability(0.0)
    testData = [[True, False], [True, True], [False, False]]
    resultData = coinPriv.privatize(testData)
    self.assertEqual([[True, False], [True, True], [False, False]], resultData)

    testData = [[True, False], [True, True], [False, False], True, False]
    resultData = coinPriv.privatize(testData)
    self.assertEqual([[True, False], [True, True], [False, False], True, False], resultData)

    resultList = coinPriv.privatize([])
    self.assertEqual([], resultList)

if __name__ == "__main__":
  unittest.main()
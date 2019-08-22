import unittest
import exponentialPrivatizer

class ExponentialPrivatizerTests(unittest.TestCase):

  def testInitializer(self):
    with self.assertRaises(ValueError) as stringContext:
      exponentialPrivatizer.ExponentialPrivatizer('a')
    self.assertTrue('Not a valid scale' in stringContext.exception)

    with self.assertRaises(ValueError) as negativeContext:
      exponentialPrivatizer.ExponentialPrivatizer(0.)
    self.assertTrue('Not a valid scale' in negativeContext.exception)

    with self.assertRaises(ValueError) as zeroContext:
      exponentialPrivatizer.ExponentialPrivatizer(-1.)
    self.assertTrue('Not a valid scale' in zeroContext.exception)

    priv = exponentialPrivatizer.ExponentialPrivatizer()
    self.assertEqual(1., priv._scale)

    priv = exponentialPrivatizer.ExponentialPrivatizer(0.5)
    self.assertEqual(0.5, priv._scale)

  def testPrivatizeSingleAnswer(self):
    priv = exponentialPrivatizer.ExponentialPrivatizer()
    with self.assertRaises(ValueError) as context:
      priv.privatizeSingleAnswer('a')
    self.assertTrue('Not valid value to be privatized' in context.exception)

    answer = priv.privatizeSingleAnswer(1.0)
    self.assertTrue(type(answer) == float)

  def testPrivatizeList(self):
    priv = exponentialPrivatizer.ExponentialPrivatizer()

    with self.assertRaises(ValueError) as context:
      priv.privatizeList(1.0)
    self.assertTrue('Not a list' in context.exception)

    emptyList = priv.privatizeList([])
    self.assertEqual([], emptyList)

    notEmptyList = priv.privatizeList([-1., 0., 1., 2.])
    self.assertEqual(len(notEmptyList), len([-1., 0., 1., 2.]))
    for value in notEmptyList:
      self.assertTrue(type(value) == float)

  def testPrivatize(self):
    priv = exponentialPrivatizer.ExponentialPrivatizer()

    with self.assertRaises(ValueError) as context:
      priv.privatize(1.0)
    self.assertTrue('Not a list' in context.exception)

    emptyList = priv.privatize([])
    self.assertEqual([], emptyList)

    notEmptyList = priv.privatize([[-1., 0., 1., 2.], [-1., 0.]])
    self.assertEqual(len(notEmptyList), len([[-1., 0., 1., 2.], [-1., 0.]]))
    for value in notEmptyList:
      self.assertTrue(type(value) == list)




if __name__ == "__main__":
  unittest.main()
import unittest
import exponentialPrivatizer

class ExponentialPrivatizerTests(unittest.TestCase):

  def testInitializer(self):
    self.assertRaises(ValueError, lambda: exponentialPrivatizer.ExponentialPrivatizer('a'))
    self.assertRaises(ValueError, lambda: exponentialPrivatizer.ExponentialPrivatizer(0.))
    self.assertRaises(ValueError, lambda: exponentialPrivatizer.ExponentialPrivatizer(-1.))

    priv = exponentialPrivatizer.ExponentialPrivatizer()
    self.assertEqual(1., priv._scale)

    priv = exponentialPrivatizer.ExponentialPrivatizer(0.5)
    self.assertEqual(0.5, priv._scale)

  def testPrivatizeSingleAnswer(self):
    priv = exponentialPrivatizer.ExponentialPrivatizer()
    self.assertRaises(ValueError, lambda: priv.privatizeSingleAnswer('a'))

    answer = priv.privatizeSingleAnswer(1.0)
    self.assertTrue(type(answer) == float)

  def testPrivatizeList(self):
    priv = exponentialPrivatizer.ExponentialPrivatizer()

    emptyList = priv.privatize([])
    self.assertEqual([], emptyList)

    notEmptyList = priv.privatize([-1., 0., 1., 2.])
    self.assertEqual(len(notEmptyList), len([-1., 0., 1., 2.]))
    for value in notEmptyList:
      self.assertTrue(type(value) == float)

  def testPrivatize(self):
    priv = exponentialPrivatizer.ExponentialPrivatizer()

    emptyList = priv.privatize([])
    self.assertEqual([], emptyList)

    notEmptyList = priv.privatize([[-1., 0., 1., 2.], [-1., 0.]])
    self.assertEqual(len(notEmptyList), len([[-1., 0., 1., 2.], [-1., 0.]]))
    for value in notEmptyList:
      self.assertTrue(type(value) == list)

    notEmptyList = priv.privatize([[-1., 0., 1., 2.], [-1., 0.], 1., 0.])
    self.assertEqual(len(notEmptyList), len([[-1., 0., 1., 2.], [-1., 0.], 1., 0.]))
    self.assertTrue(type(notEmptyList[-1]) == float)
    

if __name__ == "__main__":
  unittest.main()
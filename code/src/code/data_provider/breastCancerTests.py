import unittest
import breastCancerDataProvider

class BreastCancerDataProviderTests(unittest.TestCase):
  
  def testSingleton(self):
    firstInstance = breastCancerDataProvider.BreastCancerDP()
    secondInstance = breastCancerDataProvider.BreastCancerDP()
    self.assertEqual(firstInstance.instance, secondInstance.instance)
    self.assertIsNotNone(firstInstance.instance)

  def testSingletonMaxSize(self):
    firstInstance = breastCancerDataProvider.BreastCancerDP(100)
    secondInstance = breastCancerDataProvider.BreastCancerDP(200)
    self.assertEqual(firstInstance.maxSize, secondInstance.maxSize)

if __name__ == "__main__":
  unittest.main()
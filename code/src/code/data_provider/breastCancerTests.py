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
    self.assertEqual(200, firstInstance.maxSize)

  def testGetAllData(self):
    dataProvider = breastCancerDataProvider.BreastCancerDP()
    self.assertEqual(list, type(dataProvider.getAllData()))
    self.assertEqual(30, len(dataProvider.getAllData()[0]))

  def testGetAllTargets(self):
    dataProvider = breastCancerDataProvider.BreastCancerDP()
    self.assertEqual(list, type(dataProvider.getAllTargets()))

if __name__ == "__main__":
  unittest.main()
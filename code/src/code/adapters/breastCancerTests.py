import unittest
import numpy as np
import breastCancerAdapter as adapter

class BreastCancerAdapterTests(unittest.TestCase):

  def testInvalidInputs(self):
    self.assertRaises(ValueError, lambda: adapter.fromRaw('a'))
    self.assertRaises(ValueError, lambda: adapter.fromRaw([1]))
  
  def testOutputFormat(self):
    array = np.ndarray(shape=(2,2), dtype=float, order='F')
    output = adapter.fromRaw(array)
    self.assertEqual(list, type(output))
    self.assertEqual(list, type(output[0]))
    self.assertEqual(float, type(output[0][0]))

if __name__ == "__main__":
  unittest.main()
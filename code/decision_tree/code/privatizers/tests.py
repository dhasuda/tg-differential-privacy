import unittest
import coin_privatizer

class PrivatizersTests(unittest.TestCase):
  
  def test_coin_privitizer_invalid_data_input(self):
    with self.assertRaises(ValueError) as context:
      coin_privatizer.privatize(1)
    self.assertTrue('Not a valid data input' in context.exception)

if __name__ == "__main__":
  unittest.main()
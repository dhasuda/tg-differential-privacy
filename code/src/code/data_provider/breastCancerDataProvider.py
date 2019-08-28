from sklearn.datasets import load_breast_cancer

class BreastCancerDP:
  instance = None
  class __BreastCancerDPSingleton:
    maxSize = None
    def __init__(self, maxSize=None):
      x = 1
      self.maxSize = maxSize

  def __init__(self, maxSize=None):
    if not BreastCancerDP.instance:
      BreastCancerDP.instance = BreastCancerDP.__BreastCancerDPSingleton()
    
  def __getattr__(self, name):
    return getattr(self.instance, name)

# def get_data():
#   data = load_breast_cancer()
#   return data.

# def get_data_result():
  
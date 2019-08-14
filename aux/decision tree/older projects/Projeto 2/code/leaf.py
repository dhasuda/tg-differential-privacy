def classCount(table):
    counts = {}
    for row in table:
        label = row[-1] # Element in the last column
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

"""
    This class only stores a table
"""
class Leaf:
    
    def __init__(self, table):
        self.predictions = classCount(table)
    
    def printPredictions(self):
        answer = '{'
        isFirst = 1
        for label in self.predictions:
            if isFirst==1:
                isFirst=0
            else:
                answer += ', '
            answer += str(label) + ': '
            answer += str(self.predictions[label])
        answer += '}'
        return answer
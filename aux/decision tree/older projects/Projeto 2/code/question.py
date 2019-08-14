"""
    This class divides a node of the decision tree into two, by asking a question
"""
class Question:
    def __init__(self, column, value, header):
        self.column = column
        self.value = value
        self.header = header

    def isTrue(self, singleData):
        val = singleData[self.column]
        thisHeader = self.header[self.column]
        if thisHeader == 'UserID':
            return val == self.value
        elif thisHeader == 'MovieID':
            return val == self.value
        elif thisHeader == 'TimeStamp':
            return val == self.value
        elif thisHeader == 'Title':
            return val == self.value
        elif thisHeader == 'Genres':
            return val.find(self.value) > -1
        elif thisHeader == 'Gender':
            return val == self.value
        elif thisHeader == 'Age':
            return val >= self.value
        elif thisHeader == 'Ocuupation':
            return val == self.value
        elif thisHeader == 'Zip-code':
            return val == self.value
        elif thisHeader == 'Rating':
            return val == self.value
    
    def toString(self):
        condition = '=='
        thisHeader = self.header[self.column]
        if thisHeader == 'Age':
            condition = '>='
        return "Is %s %s %s?" % (self.header[self.column], condition, str(self.value))
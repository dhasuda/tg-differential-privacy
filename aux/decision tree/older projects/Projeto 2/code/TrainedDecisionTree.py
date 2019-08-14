import sys
from question import Question
from leaf import Leaf
from node import Node
import pickle

def classify(data, node):
    if isinstance(node, Leaf):
        return node.predictions
    
    if node.question.isTrue(data):
        return classify(data, node.trueBranch)
    return classify(data, node.falseBranch)

if __name__ == '__main__':
    me = pickle.load(open("myobject", "rb"))

    data = [1, 1, 1, 'a']

    genre = input("What genre?")
    data.append(genre)
    gender = input("M or F?")
    data.append(gender)
    age = int(input("Age?"))
    data.append(age)
    occupation = int(input("Occupation?"))
    data.append('123')
    data.append(1)

    print(classify(data, me))


import sys
from question import Question
from leaf import Leaf
from node import Node
import pickle

def printTree(node, spacing=''):
    
    if isinstance(node, Leaf):
        print(spacing + 'Predict ' + node.printPredictions())
        return
    
    print(node.question.toString())
    print(spacing + 'True branch:')
    printTree(node.trueBranch, spacing + '  ')

    print(spacing + 'False branch:')
    printTree(node.falseBranch, spacing + '  ')

if __name__ == '__main__':
    me = pickle.load(open("myobject", "rb"))
    printTree(me)

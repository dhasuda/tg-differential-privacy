import sys
from question import Question
from leaf import Leaf
from node import Node
import pickle

def readFiles():

    trainingData = []

    if sys.version_info[0] == 3:
        # Python3
        f = open('movies.dat', encoding ='ISO-8859-1')
    else :
        # Python 2
        f = open('movies.dat', 'r')

    for line in f:
        x = line.strip('\n')
        array = x.split('::')
        # print(array)
        trainingData.append(array)
    

    return trainingData

def readRatingsFile():
    ratings = []

    if sys.version_info[0] == 3:
        # Python3
        f = open('ratings.dat', encoding ='ISO-8859-1')
    else :
        # Python 2
        f = open('ratings.dat', 'r')

    # i = 0
    for line in f:
        x = line.strip('\n')
        array = [int(val) for val in x.split('::')]

        ratings.append(array)
        # if i==5:
        #     break
        # i += 1
    
    return ratings

def readUsersFile():
    users = {}

    if sys.version_info[0] == 3:
        # Python3
        f = open('users.dat', encoding ='ISO-8859-1')
    else :
        # Python 2
        f = open('users.dat', 'r')

    for line in f:
        x = line.strip('\n')
        array = x.split('::')
        userId = int(array.pop(0))
        array[1] = int(array[1])
        array[2] = int(array[2])
        users[userId] = array
    
    return users

def readMoviesFile():
    movies = {}

    if sys.version_info[0] == 3:
        # Python3
        f = open('movies.dat', encoding ='ISO-8859-1')
    else :
        # Python 2
        f = open('movies.dat', 'r')

    for line in f:
        x = line.strip('\n')
        array = x.split('::')
        movieId = int(array.pop(0))
        movies[movieId] = array
    
    return movies
    
def getTrainingData():
    trainingData = readRatingsFile()
    movies = readMoviesFile()
    users = readUsersFile()

    for i in range(len(trainingData)):
        trainingData[i] = trainingData[i] + movies[trainingData[i][1]] + users[trainingData[i][0]]
        # Rating is the last column
        rating = trainingData[i].pop(2)
        trainingData[i].append(rating)

    return trainingData

def getHeaders():
    return ['UserID', 'MovieID', 'TimeStamp', 'Title', 'Genres', 'Gender', 'Age', 'Ocuupation', 'Zip-code', 'Rating']

def possibleValues(table, column):
    return set(row[column] for row in table)

def classCount(table):
    counts = {}
    for row in table:
        label = row[-1] # Element in the last column
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

def partition(table, question):
    trueTable = []      # New table only with true answers to question
    falseTable = []     # New table only with false answers to question
    
    for row in table:
        if question.isTrue(row):
            trueTable.append(row)
        else:
            falseTable.append(row)
    return trueTable, falseTable

def getImpurity(table):
    counts = classCount(table)
    impurity = 1
    for label in counts:
        probabilityOfLabel = counts[label] / float(len(table))
        impurity -= probabilityOfLabel**2
    return impurity

def getGain(leftNode, rightNode, currentImpurity):
    p = float(len(leftNode)) / (len(leftNode) + len(rightNode))
    return currentImpurity - p*getImpurity(leftNode) - (1-p) * getImpurity(rightNode)

def allPossibleValues(column):
    if column == 4:
        return [
            'Action',
            'Adventure',
            'Animation',
            'Children\'s',
            'Comedy',
            'Crime',
            'Documentary',
            'Drama',
            'Fantasy',
            'Film-Noir',
            'Horror',
            'Musical',
            'Mystery',
            'Romance',
            'Sci-Fi',
            'Thriller',
            'War',
            'Western'
        ]
    elif column == 5:
        return ['M', 'F']
    elif column == 6:
        return [
            1,
            18,
            25,
            35,
            45,
            50,
            56
        ]
    elif column == 7:
        return [
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
             10,
             11,
             12,
             13,
             14,
             15,
             16,
             17,
             18,
             19,
             20
        ]
    
    return []

def findBestQuestion(table):
    
    bestGain = 0
    bestQuestion = None
    currentImpurity = getImpurity(table)
    n = len(table[0]) - 1 # Number of columns

    for column in range(n):
        values = allPossibleValues(column)
        for val in values:
            question = Question(column, val, getHeaders())
            trueTable, falseTable = partition(table, question)
            
            # The question must divide the dataset
            if len(trueTable) == 0 or len(falseTable) == 0:
                continue
            
            gain = getGain(trueTable, falseTable, currentImpurity)

            if gain >= bestGain:
                bestGain, bestQuestion = gain, question

    return bestGain, bestQuestion

def buildTree(table):
    gain, question = findBestQuestion(table)

    if gain == 0:
        return Leaf(table)
    
    trueTable, falseTable = partition(table, question)

    trueNode = buildTree(trueTable)
    falseNode = buildTree(falseTable)

    return Node(question, trueNode, falseNode)

def printTree(node, file, spacing=''):
    
    if isinstance(node, Leaf):
        file.write(spacing + 'Predict ' + node.printPredictions())
        return
    
    file.write(node.question.toString())
    file.write(spacing + 'True branch:')
    printTree(node.trueBranch, file, spacing + '  ')

    file.write(spacing + 'False branch:')
    printTree(node.falseBranch, file, spacing + '  ')

def classify(data, node):
    if isinstance(node, Leaf):
        return node.predictions
    
    if node.question.isTrue(data):
        return classify(data, node.trueBranch)
    return classify(data, node.falseBranch)

if __name__ == '__main__':
    print('Starting...')
    trainingData = getTrainingData()
    print('done reading')
    myTree = buildTree(trainingData)
    print('done training')
    
    pickle.dump(myTree, open("myobject", "wb"))
    # me = pickle.load(open("myobject", "rb"))
    
    
    
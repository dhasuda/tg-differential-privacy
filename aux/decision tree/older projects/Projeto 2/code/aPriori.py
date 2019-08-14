import sys

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

if __name__ == '__main__':
    print('Starting...')
    trainingData = getTrainingData()
    print('done reading')
    
    media = trainingData[0][-1]
    moda = {}

    counter = 0
    for rate in trainingData:
        media = ((counter*media) + rate[-1]) / (counter + 1)
        counter += 1
        if rate[-1] not in moda:
            moda[rate[-1]] = 0
        moda[rate[-1]] += 1

    print('media: ', media)
    print('contagem: ', moda)

    print('média truncada: ', int(media))

    modaVal = 1
    mostUsed = -1
    for val in moda:
        if moda[val] > mostUsed:
            mostUsed = moda[val]
            modaVal = val
    print('resultado moda: ', modaVal)

    
    
    
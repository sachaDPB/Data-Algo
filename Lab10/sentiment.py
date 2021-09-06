""" This file was created by Sacha de Poyen-Brown in August and September of 2021
with the purpose of evaluating the sentiments associated with various words found
in movie reviews."""


def stripFile():
    """Purpose: to turn the file input into list of words that contain no
    newline characters
    Parameters: none
    Return: filler, a list of the filler words obtained by stripping stopwords.txt"""

    filler = []
    w = open("stopwords.txt", 'r')
    for line in w:
        line = line.strip()
        filler.append(line)

    return filler

def readFile(filler):
    """Purpose: to read a file into a list
    Parameters: filler, a list of words to ignore
    Return: listOfWordList, a list of the words from each line split into indivi-
    dual lines
    """
    totalList = []
    listOfWordList = []
    scoreList = []
    reviews = open("movieReviews.txt", 'r')
    for line in reviews:
        lineList = []
        wordList = []
        lineList = line.split()
        score = int(lineList[0])
        score = score - 2
        lineList = lineList[1:]
        for i in range(len(lineList)):
            isIn = binarySearchBool(lineList[i].lower(), filler)
            if lineList[i].isalpha() == True and isIn == False:
                wordList.append(lineList[i])



        listOfWordList.append(wordList)
        scoreList.append(score)


    return listOfWordList, scoreList


def binarySearchBool(x, L):
    """Purpose: to search through a list and return a boolean stating if a speci-
    fic value is present in that list
    Parameters: x, the value in question, and L, the list to be searched through
    Return: isIn, a boolean stating whether the value is in the list or not"""

    isIn = False
    low = 0
    high = len(L) - 1
    mid = (high + low) // 2

    while low <= high:
        mid = (high + low) // 2
        if L[mid] > x:
            high = mid - 1

        elif L[mid] < x:
            low = mid + 1

        elif L[mid] == x:
            isIn = True
            return isIn

        elif L[high] == x:
            isIn = True
            return isIn

        elif L[low] == x:
            isIn = True
            return isIn


    return isIn

def binarySearch(x, L):
    """Purpose: to find the position of an item in a list given a value and a
    list
    Parameters: x, the value in question, and L, the list to be searched through
    Return: index, the index of the item in the list, if the item isn't in the list,
    return the last location searched. """

    low = 0
    high = len(L) - 1
    mid = (high + low) // 2

    while low <= high:
        midLast = mid
        mid = (high + low) // 2

        if L[mid][0] > x:
            highLast = high
            high = mid - 1

        elif L[mid][0] < x:
            lowLast = low
            low = mid + 1

        elif L[mid][0] == x:
            return mid

        elif L[high][0] == x:
            return high

        elif L[low][0] == x:
            return low

        elif high - low == 1:
            return low


    if low > high:
        return high

    elif high < low:
        return low

    return -1



def isUnique(totalList, wordList, score):
    """Purpose: to combine wordList and score into one list, while making sure
    there is only one item with a given name in the list
    Parameters: totalList, the larger list containing all previous iterations of
    wordList, wordList, all of the words in a given review, and score, the rating
    given by a critic in each review
    Return: totalList, and updated list containing all words and their scores
    (and also the number of times they appear in the reviews so I can do the log
    scale add-on)"""

    if len(totalList) == 0:
        for i in range(len(wordList)):
            totalList.append([wordList[i], score, 1])


    else:
        for i in range(len(wordList)): #changing the list iterated over
            index = binarySearch(wordList[i], totalList)

            if totalList[index][0] == wordList[i]:
                totalList[index][1] = totalList[index][1] + score
                totalList[index][2] = totalList[index][2] + 1

            else:
                assert(wordList[i] != totalList[index])
                totalList = totalList[:index + 1] + [[wordList[i], score, 1]] + totalList[index+1:]

    return totalList





def process(wordList):
    """Purpose: to clean up wordlist so it contains only lowercase letters and so
    that there are no duplicates
    Parameters: wordList, the list of words in question
    Return: wordList, same as before but with the modifications mentioned in purpose"""

    x = []
    newWordList = []
    for i in range(len(wordList)):
        wordList[i] = wordList[i].lower()

    wordList = mySort(wordList)
    for i in range(len(wordList) - 1):
        if wordList[i] == wordList[i + 1]:
            x.append(i)


    for i in range(len(wordList)):
        isIn = binarySearchBool(i, x)
        if isIn == False:
            newWordList.append(wordList[i])


    return newWordList


def mySort(L):
    """Purpose: to sort a list
    Parameters: the list in question
    Return: a sorted list """
    n = len(L)
    if n == 0:
        return L

    x = L[0]
    L1 = []
    L2 = []
    L3 = []
    for i in range(1, n):
        if L[i] < x:
            L1.append(L[i])

        if L[i] > x:
            L2.append(L[i])

        if L[i] == x:
            L3.append(L[i])


    if 0 <= len(L1) and len(L1) <= 1 and 0 <= len(L2) and len(L2) <= 1:
        L = L1 + [x] + L3 + L2
        return L

    else:
        L1 = mySort(L1)
        L2 = mySort(L2)
        L = L1 + [x] + L3 + L2
        return L

def mySortNum(L):
    """Purpose: to sort a list of lists
    Parameters: the list in question
    Return: A sorted list"""
    n = len(L)
    if n == 0:
        return L

    x = L[0]
    L1 = []
    L2 = []
    L3 = []
    for i in range(1, n):
        if L[i][1] < x[1]:
            L1.append(L[i])

        if L[i][1] > x[1]:
            L2.append(L[i])

        if L[i][1] == x[1]:
            L3.append(L[i])


    if 0 <= len(L1) and len(L1) <= 1 and 0 <= len(L2) and len(L2) <= 1:
        L = L1 + [x] + L3 + L2
        return L

    else:
        L1 = mySortNum(L1)
        L2 = mySortNum(L2)
        L = L1 + [x] + L3 + L2
        return L

def main():
    score = 0
    listOfWordList = []
    totalList = []
    filler = []
    filler = stripFile()
    listOfWordList, scoreList = readFile(filler)

    for i in range(len(listOfWordList)):
        wordList = process(listOfWordList[i])
        totalList = isUnique(totalList, wordList, scoreList[i])

    totalList = mySortNum(totalList)
    for i in range(len(totalList) - 1, -1, -1):
        print(totalList[i][1], totalList[i][0])

main()

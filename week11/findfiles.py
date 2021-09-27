"""
This program was created by Sacha de Poyen-Brown in September of 2021 with the
purpose of searching through a directory.
"""



from os import listdir
from os.path import isdir, expanduser

def dirSearch(path, pattern, finds, new, dirList):
    """
    Purpose: to recursively search through a directory and find all occurences of
    a pattern
    Parameters: path - the current path being searched, pattern - the string to
    search for, finds - a list of occurences of the pattern, dirList - a list of
    current directories
    Returns: finds - a list of occurrences of the pattern
    """

    if new == True:
        try: dirList = listdir(path)

        except OSError:
            return

    if len(dirList) == 0:
        return finds

    if pattern in dirList[0]:
        finds += [dirList[0]]

    newPath = path + "\\" + dirList[0]
    if isdir(newPath) == True:
        ##print("hi")
        dirSearch(newPath, pattern, finds, True, 0)

    new = False
    dirList = dirList[1:]
    return dirSearch(path, pattern, finds, new, dirList)

if __name__ == '__main__':
    global depth
    depth = 0
    home = expanduser("~")
    ##print(home)
    path = input("Enter a path: ")
    pattern = input("Enter a pattern: ")
    dirList = listdir(path)
    finds = dirSearch(path, pattern, [], True, 0)
    print(finds)

import matplotlib.pyplot as plt
import time
plt.style.use('ggplot') #This one line code fragment came from https://benalexkeen.com/bar-charts-in-matplotlib/

import tkinter as Tk


def drawList(drawL):
    """Purpose: to draw the current list in the form of a bar graph
    Parameters: drawL, a list of lists containing the swaps involved in the sorting
    Return: none"""

    print(drawL[-1])
    plot1 = plt.figure()
    labels = range(len(drawL[0]))
    p1 = plt.bar(labels, drawL[0])
    plt.show(block = False)
    plt.pause(.5)
    for i in range(1, len(drawL)):
        for j in range(len(p1)):
            p1[j].set_height(drawL[i][j])
        plt.pause(.05)
        plt.show(block=False)


def insertionSort(L):
    """Purpose: to sort a list using insertion sort
    Parameters: the list in question
    Return: none, but it passes a list of lists containing all the swaps to drawlist"""

    n = len(L)
    drawL = []
    for i in range(n, 1, -1):
        for j in range(1, i):
            if L[j] < L[j - 1]:
                L[j], L[j - 1] = L[j - 1], L[j]
                drawL.append(0)
                drawL[-1] = L.copy()
    drawList(drawL)

    return L

root = Tk.Tk()

if __name__ == "__main__":

    from random import shuffle

    N = int(input("How many bars would you like:"))
    L = []
    listCopy = []
    for i in range(N):
        L.append(i)
        listCopy.append(i)

    shuffle(L)
    insertionSort(L)
    assert L == listCopy


    Tk.mainloop()

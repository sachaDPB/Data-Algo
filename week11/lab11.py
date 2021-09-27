"""
This program was created by Sacha de Poyen-Brown in September 2021 with the purpose
of creating a recursive/fractal drawing.
"""


from tkinter import *
from tkinter.ttk import Frame
import sys

sys.setrecursionlimit(1500)

class Data():
    """
    Purpose: to store and calculate the points to draw.
    Parameters: self - instance variable, num - the iteration currently being drawn
    data - the previous instance of self
    Return: data - all of the data needed to draw the current iterative layer
    """

    def __init__(self, num, data):
        """
        Purpose: Constructor, starts the class going, and does what is mentioned above
        Parameters: same as class
        Return: none
        """
        self.notOut = [4]
        self.listOfPoints = []
        self.listOfPoints1 = []
        self.num = num
        if type(data) != int:
            self.points1 = data.points1
            self.points = data.points
            if self.num != 1:
                self.notOut = [0, 1, 2, 3]
                self.recurCoords(data)
            else:
                self.getCoords()
        else:
            self.getCoords()

    def recurCoords(self, data):
        if len(data.listOfPoints1) == 0:
            return
        else:
            self.points1 = data.listOfPoints1[0]
            self.getCoords()
            self.notOut = self.notOut[1:] + [self.notOut[0]]
            data.listOfPoints1 = data.listOfPoints1[1:]

        self.recurCoords(data)


    def getCoords(self):
        """
        Purpose: to calcule where the points should be drawn
        Parameters: self - instance variable of the class
        Returns: (not really) listOfPoints and listOfPoints1 - lists containing
        the coordinates of the polygons in each layer
        """

        if self.num == 0:
            xc = [400]
            yc = [300]
        else:
            xc = self.points1[::2]
            yc = self.points1[1::2]

        o1 = 200 // 2 ** self.num #grn size
        x1 = (o1 / (2 ** .5) ) #blu size
        for i in range(len(xc)):

            if bool(i == self.notOut[0]) == bool(self.num != 0) or bool(i == self.notOut[0]) == bool(self.num != 1) :
                self.points1 = [xc[i] + x1, yc[i] + x1, xc[i] - x1, yc[i] + x1, xc[i] - x1, yc[i] - x1, xc[i] + x1, yc[i] - x1]
                self.points = [xc[i], yc[i] + o1, xc[i] + o1, yc[i], xc[i], yc[i] - o1, xc[i] - o1, yc[i]]
                self.listOfPoints1 += [self.points1.copy()]
                self.listOfPoints += [self.points.copy()]


def getUserInput():
    """
    Purpose: to validate user Input
    Parameters: None
    Returns: x - validated user input
    """
    x = input("Recursion Depth: ")
    try:
        x = int(x)
    except ValueError:
        x = getUserInput()
    return x

def recurDraw(num, data):
    """
    Purpose: to draw polygons
    Parameters: num - indicator of what layer the program is on, data - instance
    of the Data class
    Returns: data - instance of the data class
    Calls: recurDraw - itself, Data - data processing class, toDraw - drawing
    intermediary function
    """
    if num == 0:
        return num
    num -= 1
    data = recurDraw(num, data)
    data = Data(num, data)
    #print(data.listOfPoints1)
    toDraw(data)
    return data

"""def toDraw(num, data):
    for i in range(len(data.listOfPoints1)):
        drawStuff(num, data.listOfPoints1[i], data.listOfPoints[i])"""

def toDraw(data):
    """
    Purpose: recursively determine which data to use to make shapes
    Parameters: data - a data object from the Data class
    Returns: none
    Calls: drawStuff
    """
    if type(data) != list:
        data = [data.listOfPoints1.copy(), data.listOfPoints.copy()]
        #print(data)
    if len(data[0]) == 0:
        return
    drawStuff(data[0][0], data[1][0])
    data = [data[0][1:], data[1][1:]]
    data = toDraw(data)



def drawStuff(points1, points):
    """
    Purpose: to draw two polygons
    Paramaters: points 1 and points - lists of points to make polygons out of
    Return: none
    """

    canvas.create_polygon(points1, outline="#f11", fill="#4287f5", width=2)
    canvas.create_polygon(points, outline="#f11", fill="#1f1", width=2)

if __name__ == "__main__":
    root = Tk()
    canvas = Canvas()
    canvas.pack(fill=BOTH, expand=1)
    root.geometry("800x600")
    root.update_idletasks()
    #degree = getUserInput()
    recurDraw(4, root)
    root.mainloop()

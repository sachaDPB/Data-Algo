"""This program was created by Sacha de Poyen-Brown in september 2021 with the
purpose of removing a given input from a string"""


def cleanString(string, clean):
    """
    Purpose: to remove the character from the string
    Variables: string - the string to remove a char from, clean - the char to remove
    """
    if len(string) == 0:
        return ""
    thing = string[0]
    string = string[1:]
    string = cleanString(string, clean)
    if thing != clean:
        string = thing + string
    return string




def checkClean():
    """
    Purpose: To make sure the input to remove is a single character.
    Inputs: None
    Returns: A single character to remove
    """
    clean = input("Select a letter: ")
    if len(clean) == 1:
        return clean
    else:
        print("Please pick a single character.")
        clean = checkClean()
    return clean

if __name__ == '__main__':
    string = input("Select a string: ")
    clean = checkClean()
    newString = cleanString(string, clean)
    print(newString)

"""
This project was created by the right honorable sir Alexander de Poyen-Brown, in
the year of Our Lord two thousand and twenty one for the purpose of being silly.
"""


def sillyText(word, num):
    """
    Purpose: To duplicate each character in a string
    Parameters: word - the string in question, num - the number of duplications
    Return: word - the duplicated word
    """
    if len(word) == 0:
        return ""
    thing = word[0]
    word = word[1:]
    word = sillyText(word, num)
    word = thing * 2 + word
    return word

def getUserInput():
    """
    Purpose: to validate user Input
    Parameters: None
    Returns: x - validated user input
    """
    x = input("Number of repeats: ")
    try:
        x = int(x)
    except ValueError:
        x = getUserInput()
    return x



def main():
    word = input("Word: ")
    num = getUserInput()
    silly = sillyText(word, num)
    print(silly)

main()

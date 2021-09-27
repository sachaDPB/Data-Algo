def isPalindrome(x):
    if len(x) == 0 or len(x) == 1:
        return True
    elif x[0] == x[-1]:
        x = x[1:len(x)-1]
        x = isPalindrome(x)
        return x
    else:
        return False



if __name__ == "__main__":
    x = "abuuba"
    pal = isPalindrome(x)
    assert pal == True

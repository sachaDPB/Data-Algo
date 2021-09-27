from random import randint

def sumNum(x):
    x -= 1
    if x == 1:
        return x
    x1 = sumNum(x)
    x = x * x1
    return x

def coinFlip(n):
    n -= 1
    if n == 0:
        return n
    n = coinFlip(n)
    n += randint(0,1)
    return n



def main():
    y = 0
    #x = int(input("Number: "))
    x = 10
    y = coinFlip(x + 1)
    print(y)

main()

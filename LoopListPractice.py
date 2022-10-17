#A method whihc can take in a list of intergers and return
#The difference between the largest and smallest interger
# [2, 5, 3, 1, 9, 7] --> 8
def bigDiff(l):
    maxNum = l[0]
    minNum = l[0]
    for elem in l:
        if elem > maxNum:
            maxNum = elem
        if elem < minNum:
            minNum = elem

    return maxNum - minNum
# A method which can take in a list of intergers and return
# The mean of all numbers excluding the maximum and minimum
# [2, 5, 3, 1, 9, 7] --> 4.25
def centeredAvg(l):
    maxNum = l[0]
    minNum = l[0]
    for elem in l:
        if elem > maxNum:
            maxNum = elem
        if elem < minNum:
            minNum = elem
    l.remove(maxNum)
    l.remove(minNum)

    total = 0
    for elem in l:
        total = total + elem

    return total / len(l)

def main():
    print(bigDiff([2, 5, 3, 1, 9, 7]))
    print(centeredAvg([2, 5, 3, 1, 9, 7]))























if __name__ == "__main__":
    main()

import math
import random

#problem 1
def problem1(x, y, z):

    mean = (x + y + z)/3
    L = [x, y, z]
    L.sort()
    median = L[1]

    return mean, median

#problem 2
def problem2(a, L):
    if a % L[0] == 0:
        print(a)
    else:
        return False
    if a % L[1] == 0:
        print(a)
    else:
        return False
    if a % L[2] == 0:
        print(a)
    else:
        return False

#problem 3
def problem3(L1):
    maxNum = L1[0]
    minNum = L1[0]
    for elem in L1:
        if elem > maxNum:
            maxNum = elem
        if elem < minNum:
            minNum = elem

    print(maxNum)
    print(minNum)
    print(maxNum - minNum)

#problem 4
def problem4():
    La = []
    x = input("enter x = ")
    x = int(x)
    y = input ("enter y = ")
    y = int(y)
    pi = 22/7
    h = math.sqrt(x*x + y*y)
    angle= math.asin(y/h)*(180/pi) 
    print(angle)
    La.append(h)
    La.append(angle)
    print(La)
    
#problem 5
def problem5():
    total = 0
    name = input("enter a name in capital: ")
    L2 = ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"]
    L3 = ["D", "G"]
    L4 = ["B", "C", "M", "P"]
    L5 = ["F", "H", "V", "W", "Y"]
    L6 = ["K"]
    L7 = ["J", "X"]
    L8 = ["Q", "Z"]
    for char in name:
        if char in L2:
            print("1 point")
            total = total + 1
        if char in L3:
            print("2 point")
            total = total + 2
        if char in L4:
            print("3 point")
            total = total + 3
        if char in L5:
            print("4 point")
            total = total + 4
        if char in L6:
            print("5 point")
            total = total + 5
        if char in L7:
            print("6 point")
            total = total + 6
        if char in L8:
            print("7 point")
            total = total + 7
    print(str(total) + " points")
    
    
    
    
    


def main():
    # problem 1
    print(problem1(5, 10, 42))

    #problem 2
    L = [2, 3, 5]
    a = random.randint(1, 100)
    print(problem2(a, L))

    #problem 3
    L1 = []
    for i in range(10):
        L1.append(random.randint(1, 50))
    print(problem3(L1))

    #problem 4
    print(problem4())

    #problem 5
    print(problem5())
    

    
    
        
    



























if __name__ == "__main__":
    main()

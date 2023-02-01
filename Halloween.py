# General average rating of 25 houses.
# Row, col of the first house to visit.
# Visit "num" houses by looping "num" times, each step try to find the house with maximum rating in firstHouse
# Add the house with maximum rating to path
# Add house with max candies to total of current path.
# Add all neighbors of new house to firstHouse.
# Remove all houses that already visited from firstHouse.
# If average of houses in path greater than general average, return path.


import random
class House:
    def __init__(self):
        self.rating = random.randint(1, 10)

    def getRating(self):
        return self.rating

def calculatePath(m, num):
    path = []
    Sum = 0
    for row in range(5):
        for col in range(5):
            house = m[row][col]
            Sum = Sum + house.getRating()

    avg = Sum/25
    print("avg = " + str(avg))

    for row in range(5):
        for col in range(5):
            print("Start at row " + str(row) + " ,col " + str(col))
            path = []
            firstHouse = []
            totalCandies = 0
            
            firstHouse.append([row, col])

            for step in range (num):
                maxCandies = 0
                nextRow = 0
                nextCol = 0
                for other in firstHouse:
                    otherRow = other[0]
                    otherCol = other[1]
                    otherHouse = m[otherRow][otherCol]
                    if otherHouse.getRating() > maxCandies:
                       nextRow = otherRow
                       nextCol = otherCol
                       maxCandies = otherHouse
                
                path.append([nextRow, nextCol])

                totalCandies = totalCandies + maxCandies

                firstHouse.append(getNeighbors(nextRow, nextCol))



                for visitedHouse in path:
                    if visitedHouse in firstHouse:
                        firstHouse.remove(visitedHouse)
            print("total candies found in the path " + str(totalCandies))

            if totalCandies/num >= avg:
                print ("Best path found with the average of" + str(totalCandies/num) + "candies")
                return path
                        


        

      

          
                

                

# Get all neigbor in 4 directions: left, right, up, down
def getNeighbors(row, col):
    list = []
    if row > 0:
        list.append([row - 1, col])
    if row < 4:
        list.append([row + 1, col])
    if col > 0:
        list.append([row, col - 1])
    if col < 4:
        list.append([row, col + 1])
    return list


def main():

    m = [[], [], [], [], []]
    for l in m:
        for i in range(5):
            l.append(House())
    


    print(m)
    print("how many houses")
    num = int(input())

    path = calculatePath(m, num)
    print(path)




if __name__ == "__main__":
    main()

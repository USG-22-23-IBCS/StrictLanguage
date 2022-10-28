import random

class House:

    def __init__(self):
        self.rating = random.randint(1,10)

    def getRating(self):
        return self.rating

def randPath(m, num):
    #create an empty path
    p = []

    #try to add coordinates to the path
    #if the path were to get stuck or be 'unfinished' in anyway, try again
    #only finish once a fair path is generated
    while (len(p) < num):
        p = []
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        pVal = m[x][y]
        p.append([x, y])

        #keep track of the value of the path
        #choose a random coordinate to start at



        #add neighbors to the path at a randomly chosen direction
        #keep track of whether we get stuck. If we get stuck, break
        for i in range(num - 1):
            neighbors = [[x, y-1], [x+1, y], [x-1, y], [x, y+1]]
            bad = []   

            for  n in neighbors:
                 if (n[0] > 4) or (n[0] < 0):
                    bad.append(n)
                 elif (n[1] > 4) or (n[1] < 0):
                    bad.append(n)
                 elif n in p:
                    bad.append(n)
            for b in bad:
                neighbors.remove(b)

            if len(neighbors) == 0:
                break

            nextHouse = random.choice(neighbors)
            p.append(nextHouse)
            x = nextHouse[0]
            y = nextHouse[1]
            pVal = pVal + m[x][y]
                #choose a random direction and attempt to add the neighbor
                #do not add the neighbor to the path if it is outside of the 5x5
                #or if the neighbor is already in the path
                #break the while loop if it was a successful addition or if stuck
                
    return pVal, p
    

                                  
  
def main():
    m = [[], [], [], [], []]
    for l in m:
        for i in range(5):
            h = House()
            l.append(h.getRating())

    for i in range(5):
        print(m[0][i], m[1][i], m[2][i], m[3][i], m[4][i]) 

    num = int(input("How many houses?\n"))
    total = 0
    for i in range(5):
        for j in range(5):
            total = total + m[i][j]
    average = total/25
    pVal, p = randPath(m, num)
    while (average > pVal/num):
        pVal, p = randPath(m, num)
    print(p)
    print("The average value in the path is: " + str(pVal/num))
    print("The average value in the neighborhood is: " + str(average))
    
    

    #calculate the average rating of a house in the neighborhood

    
    #while the average of value of the house is greater than the
    #average of the path randomly chosen, try getting another random
    #path. stop, once it is better, and print it.

            

        

if __name__ == "__main__":
    main()

import random

class House:

    def __init__(self):
        self.rating = random.randint(1,10)

    def getRating(self):
        return self.rating

def randPath(m, num):
    #create an empty path
    p = []
    x = random.ranint(0, 4)
    y = random.ranint(0, 4)
    p.append([x, y])
    pVal = m[x][y]

    #try to add coordinates to the path
    #if the path were to get stuck or be 'unfinished' in anyway, try again
    #only finish once a fair path is generated
    while (len(p) < num):
        p = []
        
 
        #keep track of the value of the path
        #choose a random coordinate to start at



        #add neighbors to the path at a randomly chosen direction
        #keep track of whether we get stuck. If we get stuck, break
        for i in range(num - 1):
            neighbors = [[x, y-1], [x+1, y], [x-1, y], [x, y+1]]
                
            while True:

                #choose a random direction and attempt to add the neighbor
                stuck = True
                neighbor = random.choice(neighbors)
                p.append(neighbor)
                #do not add the neighbor to the path if it is outside of the 5x5
                x = neighbor[0]
                y = neighbor[1]
                if (neighbor[0] < 5) and (neighbor[0] > -1):
                    if (neighbor[1] < 5) and (neighbor[1] > -1):
                        if neighbor not in p:
                            stuck = False
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

    #calculate the average rating of a house in the neighborhood

    
    #while the average of value of the house is greater than the
    #average of the path randomly chosen, try getting another random
    #path. stop, once it is better, and print it.

            

        

if __name__ == "__main__":
    main()

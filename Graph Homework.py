# each node represents ít teritory and represent its "neighbor"
# if it is not the connected by a line, then it can be the same color
# graph G(V, E) set at verticies (nodes) and set at edges (lines)
# degree is the number of edges (lines) connected to a node 
# maxDegree is the max number of lines
# cycle is any path that can start and stop at the same node

from button import*
import random
import time

class Node:
    def __init__(self, x, y, win, name):
        self.center = Point(x, y)
        self.C = Circle(self.center, 30)
        self.neighbors = []
        self.name = name
        self.T = Text(self.center, self.name)
    
    def draw(self, win):
        self.C.draw(win)
        self.T.draw(win)

    def undraw(self):
        self.C.undraw()
        self.T.undraw()

    def calcDegree(self):
        return len(self.neighbors)

    def getName(self):
        return self.name

    def addNeighbor(self, n):
        self.neighbors.append(n)

    def getCenter(self):
        return self.center

    def getNeighbors(self):
        return self.neighbors

    def color(self, c):
        self.C.setFill(c)

class Graph:

    def __init__(self, n, e, win):
        self.nodes = []
        self.E = []
        Xpositions = []
        Ypositions = []
        names = ["A", "B", "C", "D", "E", "F", "J", "H", "I", "J", "K"]
        numN = 0
        while True:
            x = random.randint(140, 740)
            y = random.randint(50, 550)
            foundNode = True
            for posX in Xpositions:
                if x - 70 < posX < x + 70:
                    for posY in Ypositions:
                        if y - 70 < posY < y + 70:
                            foundNode = False
            if foundNode:
                Xpositions.append(x)
                Ypositions.append(y)
                name = names[numN]
                N = Node(x, y, win, name)
                self.nodes.append(N)
                numN += 1

            if numN == n:
                break
        
        edges = 0
        while edges < e:
            n1 = random.choice(self.nodes)
            n2 = random.choice(self.nodes)
            if n1 != n2:
                if n1 not in n2.getNeighbors():
                    p1 = n1.getCenter()
                    p2 = n2.getCenter()
                    L = Line(p1, p2)
                    self.E.append(L)
                    L.draw(win)
                    edges += 1
                    n1.addNeighbor(n2)
                    n2.addNeighbor(n1)

        for node in self.nodes:
            node.draw(win)
            node.color("white")
            print(str(node.calcDegree()) + ":" + node.getName())
            
           
               
    def minDegree(self):
        minD = len(self.nodes)
        for node in self.nodes:
            neighbors = node.getNeighbors()
            minD = min(minD,len(neighbors))
        
        print("The min degree is: " + str(minD))
        
    def maxDegree(self):
        maxD = 0
        for node in self.nodes:
            neighbors = node.getNeighbors()
            maxD = max(maxD,len(neighbors))
        
        print("The max degree is: " + str(maxD))

    #def hasCycle(D):
       
        
        
     

    


    def delete(self):
        for e in self.E:
            e.undraw()
        for n in self.nodes:
            n.undraw()
            
        
        
def main():

    win = GraphWin("Graphy thingy", 800, 600)
    Q = Button(win, Point(20, 530), Point(100, 590), "purple3", "QUIT!")
    Gen = Button(win, Point(20, 430), Point(100, 490), "purple1", "Generate!")
    G = Graph(1, 0, win)
    
    while True:
        m = win.getMouse()
        if Q.isClicked(m):
            break
        if Gen.isClicked(m):
            G.delete()
            G = Graph(4, 4, win)
            G.minDegree()
            G.maxDegree()
            
    win.close()

if __name__ == "__main__":
    main()

# each node represents ít teritory and represent its "neighbor"
# if it is not the connected by a line, then it can be the same color
# graph G(V, E) set at verticies (nodes) and set at edges (lines)
# degree is the number of edges (lines) connected to a node 
# maxDegree is the max number of lines
# cycle is any path that can start and stop at the same node

from button import*
from graphics import*
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

    def calcDegree(self):
        return len(self.neighbors)

    def getName(self):
        return self.name

    def undraw(self):
        self.C.undraw()
        self.T.undraw()

    def addNeighbor(self, n):
        self.neighbors.append(n)

    def getCenter(self):
        return self.center

    def getNeighbors(self):
        return self.neighbors

    def color(self, c):
        self.C.setFill(c)

    def printNeighbors(self):
        l = []
        for n in self.neighbors:
            l.append(n.getName())
        return l

class Graph:

    def __init__(self, n, e, win):
        self.nodes = []
        self.E = []
        Xpositions = []
        Ypositions = []
        names = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
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
            #print(str(node.calcDegree()) + " : " + node.getName())

    def minDegree(self):
        minD = 100
        for node in self.nodes:
            if node.calcDegree() < minD:
                minD = node.calcDegree()
        return minD

    def maxDegree(self):
        maxD = 0
        for node in self.nodes:
            if node.calcDegree() > maxD:
                maxD = node.calcDegree()
        return maxD
    
    def delete(self):
        for e in self.E:
            e.undraw()
        for n in self.nodes:
            n.undraw()

    def hasCycle(self):
        for n in self.nodes:
            #call traverse graph (recursive function) on each node in the graph
            #if it is every true (cycle found) return true.
            if self.traverseGraph(n, n, []):
                return True
        # if it never returned true, there was never a cycle
        return False
                        
    def traverseGraph(self, current, previous, visited):
        #base case -- dead end
        if len(current.getNeighbors()) <= 1:
            return False

        #see possible neighbors to still visit
        check = []
        for node in current.getNeighbors():
            # return true if one of the neighbors has been previously visited
            if (node in visited) and (node != previous):
                return True
            #otherwise, add unvisited nodes to a list to traverse
            elif node != previous:
                check.append(node)
                
        #update visited nodes  
        visited.append(previous)
        for node in check:
            #recursive call on each new unvisited neighbor
            if self.traverseGraph(node, current, visited):
                return True
        return False
                
        
        
def main():

    win = GraphWin("Graph Example", 800, 600)
    #buttons
    Q = Button(win, Point(20, 530), Point(100, 590), "purple", "QUIT!")
    Gen = Button(win, Point(20, 430), Point(100, 490), "purple", "Generate!")
    AddNode = Button(win, Point(20, 330), Point(100, 390), "purple", "Add Node")
    Degrees = Button(win, Point(20, 230), Point(100, 290), "purple", "Calc Degrees")
    Cycle = Button(win, Point(20, 130), Point(100, 190), "purple", "Has Cycle?")
    Enode = Entry(Point(50, 30), 10)
    Enode.draw(win)
    Eedge = Entry(Point(50, 100), 10)
    Eedge.draw(win)
    Tnode = Text(Point(50, 10), "Number of nodes: ")
    Tnode.draw(win)
    Tedge = Text(Point(50, 80), "Number of edges: ")
    Tedge.draw(win)
    G = Graph(1, 0, win)
    while True:
        m = win.getMouse()
        if Q.isClicked(m):
            break
        if Degrees.isClicked(m):
            print("Minimum Degree: " + str(G.minDegree()))
            print("Maximum Degree: " + str(G.maxDegree()))
        if Cycle.isClicked(m):
            if G.hasCycle():
                print("The graph has a cycle")
            else:
                print("The graph does not have a cycle")
        if Gen.isClicked(m):
            '''print("\n===================================\n")
            G.delete()
            #Graph made with number of nodes and number of edges
            G = Graph(5, 4, win)'''
            G.delete()
            numNode = Enode.getText()
            numEdge = Eedge.getText()
        if numNode != "" and numEdge != "":
            G = Graph(int(numNode), int(numEdge), win)
            
            
            
            
            
    win.close()

if __name__ == "__main__":
    main()

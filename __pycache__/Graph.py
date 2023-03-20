from button import*
import random
import time
import math
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

    def removeNeighbor(self, n):
        self.neighbors.remove(n)

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
        XYpositions = []
        self.names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
        self.colors = ["red", "yellow", "purple", "blue"]
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
                name = self.names.pop(0)
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
            #print(str(node.calcDegree()) + " : " + node.getName(
            
        

        
            
    def addNode(self, win):
        m = win.getMouse()
        x = m.getX()
        y = m.getY()
        name = self.names.pop(0)
        N = Node(x, y, win, name)
        neighbor = random.choice(self.nodes)
        N.addNeighbor(neighbor)
        neighbor.addNeighbor(N)
        self.nodes.append(N)
        L = Line(Point(x, y), neighbor.getCenter())
        L.draw(win)
        self.E.append(L)
        neighbor.undraw()
        neighbor.draw(win)
        N.draw(win)
        N.color("white")

    def removeNode(self, win):
        m = win.getMouse()
        x = m.getX()
        y = m.getY()
        
        for n in self.nodes:
            center = n.getCenter()
            x1 = center.getX()
            y1 = center.getY()
            d = math.sqrt((x - x1)**2 + (y - y1)**2)
            if d <= 30:
                self.nodes.remove(n)
                n.undraw()
                newEdges = []    
                for edge in self.E:
                    if (edge.p1.x == x1 and edge.p1.y == y1) or (edge.p2.x == x1 and edge.p2.y == y1):
                        edge.undraw()
                        print("removed edge " + str(edge))
                    else:
                        newEdges.append(edge)
                self.E = newEdges    
                for nb in n.getNeighbors():
                    print(nb.getName())
                    nb.removeNeighbor(n)
                        
            
       

    def addEdge(self, win):
        prompt = Text(Point(400, 10), "Select first node!")
        prompt.setSize(25)
        prompt.setTextColor("red")
        prompt.undraw()
        prompt.draw(win)
        firstNode = None
        secondNode = None

        m = win.getMouse()
        x = m.getX()
        y = m.getY()
        for n in self.nodes:
            center = n.getCenter()
            x1 = center.getX()
            y1 = center.getY()
            if math.sqrt((x - x1)**2 + (y - y1)**2) <= 30:
                firstNode = n
        
        prompt.undraw()
        prompt = Text(Point(400, 10), "Select second node!")
        prompt.setSize(25)
        prompt.setTextColor("red")
        prompt.draw(win)
        m = win.getMouse()
        x = m.getX()
        y = m.getY()
        for n in self.nodes:
            center = n.getCenter()
            x1 = center.getX()
            y1 = center.getY()
            if math.sqrt((x - x1)**2 + (y - y1)**2) <= 30:
                secondNode = n
    

        if secondNode not in firstNode.getNeighbors() and firstNode not in secondNode.getNeighbors():
            firstNode.addNeighbor(secondNode)
            secondNode.addNeighbor(firstNode)
            L = Line(firstNode.getCenter(), secondNode.getCenter())
            L.draw(win)
            self.E.append(L)
            firstNode.undraw()
            firstNode.draw(win)
            secondNode.undraw()
            secondNode.draw(win)
        
      
  
    def coloringNode(self, colors):

        
        colorMap = {}
        for node in self.nodes:
            # colors of all neighbors
            neighborsColors = []
            for nb in node.getNeighbors():
                # If neigbor already had a color, add it to the list
                if nb in colorMap:
                    neighborsColors.append(colorMap[nb])
            
            for color in self.colors:
                # If a color is not used by any neigbors, use it and exit the loop
                if color not in neighborsColors:
                    node.color(color)
                    colorMap[node] = color
                    break

        
            
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

    win = GraphWin("Graph Example", 800, 700)
    #buttons
    Coloring = Button(win, Point(150, 530), Point(230, 590), "beige", "Coloring")
    AddEdge = Button(win, Point(150, 630), Point(230, 690), "beige", "Add Edge")
    Q = Button(win, Point(20, 630), Point(100, 690), "tomato", "QUIT!")
    Gen = Button(win, Point(20, 530), Point(100, 590), "cyan", "Generate!")
    AddNode = Button(win, Point(20, 430), Point(100, 490), "beige", "Add Node")
    RemoveNode = Button(win, Point(20, 330), Point(100, 390), "beige", "Remove Node")
    Degrees = Button(win, Point(20, 230), Point(100, 290), "beige", "Calc Degrees")
    Cycle = Button(win, Point(20, 130), Point(100, 190), "beige", "Has Cycle?")
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
        if Enode != "" and Eedge != "":
            numNode = Enode.getText()
            numEdge = Eedge.getText()
        if Gen.isClicked(m):
            print("\n===================================\n")
            #Graph made with number of nodes and number of edges
            G.delete()
            G = Graph(int(numNode), int(numEdge), win)
            
        if AddNode.isClicked(m):
            G.addNode(win)

        if RemoveNode.isClicked(m):
            G.removeNode(win)

        if AddEdge.isClicked(m):
            G.addEdge(win)

        if Coloring.isClicked(m):
            G.coloringNode(win)
           
                
                
    win.close()

if __name__ == "__main__":
    main()

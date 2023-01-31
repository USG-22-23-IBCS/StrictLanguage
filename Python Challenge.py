from graphics import *
from button import *
def Mablib(self, noun1, noun2, verb, adjective, exclamation):
    self.noun1 = noun1
    self.noun2 = noun2
    self.verb = verb
    self.adjective = adjective
    self.exclamation = exclamation
def noun1():
    return noun1
def noun2():
    return noun2
def verb():
    return verb
def adjective():
    return adjective
def exclamation():
    return exclamation    




def main():
    win = GraphWin("madlibs", 800, 800)
    N = Entry(Point(200, 100), 20)
    N.draw(win)

    N2 = Entry(Point(200, 200), 20)
    N2.draw(win)

    V = Entry(Point(200, 300), 20)
    V.draw(win)

    A = Entry(Point(200, 400), 20)
    A.draw(win)

    E = Entry(Point(200, 500), 20)
    E.draw(win)
    B = Button(win, Point(400, 450), Point(520, 550), "purple4", "Click")
    
    NT = Text(Point(80, 100), "Enter first noun: ")
    NT.draw(win)
    NT2 = Text(Point(80, 200), "Enter second noun: ")
    NT2.draw(win)
    VT = Text(Point(80, 300), "Enter verb: ")
    VT.draw(win)
    AT = Text(Point(80, 400), "Enter adjective: ")
    AT.draw(win)
    ET = Text(Point(80, 500), "Enter exclamation: ")
    ET.draw(win)
 
    
    while True:
        m = win.getMouse()

        if B.isClicked(m):
            noun = N.getText()
            

            noun2 = N2.getText()
            
     
            verb = V.getText()
            
   
            adj = A.getText()
            
       
            exc = E.getText()
            
            Story = Text(Point(650, 600), "This morning, my " + noun + " woke me up. I woke up, " + verb + ", and ready to go to school. " + noun2 + " was still sleeping. He is so " + adj + " " + exc)
            Story.draw(win)
            B = Button(win, Point(400, 450), Point(520, 550), "purple4", "Click")

        
    
    


if __name__ == "__main__":
    main()

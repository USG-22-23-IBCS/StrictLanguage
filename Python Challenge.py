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




#noun1 = input('enter a noun: ')
#noun2 = input('enter a noun: ')
#verb = input('enter a verb: ')
#adjective = input('enter an adjective: ')
#exclamation = input('enter an exclamtion: ')


def main():
    win = GraphWin("madlibs", 800, 800)
    N = Entry(Point(200, 100), 20)
    N.draw(win)

    N = Entry(Point(200, 200), 20)
    N.draw(win)

    V = Entry(Point(200, 300), 20)
    V.draw(win)

    A = Entry(Point(200, 400), 20)
    A.draw(win)

    E = Entry(Point(200, 500), 20)
    E.draw(win)
    B = Button(win, Point(400, 450), Point(520, 550), "purple4", "Click")
    while True:
        m = win.getMouse()

        if B.isClicked(m):
            noun = N.getText()
            print(noun)

            noun2 = N.getText()
            print(noun2)
     
            verb = V.getText()
            print(verb)
   
            adj = A.getText()
            print(adj)
       
            exc = E.getText()
            print(exc)
            print("This morning, my " + noun + " woke me up. I woke up, " + verb + ", and ready to go to school. " + noun2 + " was still sleeping. He is so " + adj + " " + exc)
    
    


if __name__ == "__main__":
    main()

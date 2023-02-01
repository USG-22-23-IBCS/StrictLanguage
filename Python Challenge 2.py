from graphics import *
from button import *
def main():
    win = GraphWin("Challenge 2", 800, 800)
    C = Circle(Point(400, 50), 30)
    C.draw(win)
    p = C.getCenter()
    y = p.getY()
    x = p.getX()
    while y < 770:
        C.move(0, 10)
        y = C.getCenter().getY()
        if y < 100:
            time.sleep(0.5)
        elif y < 200:
            time.sleep(0.25)
        elif y < 300:
            time.sleep(0.1)
        elif y < 400:
            time.sleep(0.05)
        elif y < 500:
            time.sleep(0.025)
        elif y < 600:
            time.sleep(0.005)
        elif y < 700:
            time.sleep(0.001)
        elif y < 770:
            time.sleep(0.0005)
    if y == 770 and x < 750:
        C.move(10, -200)
        time.sleep(0.1)
        y = C.getCenter().getY()
        x = C.getCenter().getX()
        if y < 750:
            C.move(10, 200)
            time.sleep(0.1)
            y = C.getCenter().getY()
    if y == 770:
        C.move(10, -180)
        time.sleep(0.1)
        y = C.getCenter().getY()
        if y < 750:
            C.move(10, 180)
            time.sleep(0.1)
            y = C.getCenter().getY()
    if y == 770:
        C.move(10, -150)
        time.sleep(0.1)
        y = C.getCenter().getY()
        if y < 750:
            C.move(10, 150)
            time.sleep(0.1)
            y = C.getCenter().getY()
    if y == 770:
        C.move(10, -100)
        time.sleep(0.1)
        y = C.getCenter().getY()
        if y < 700:
            C.move(10, 100)
            time.sleep(0.1)
            y = C.getCenter().getY()
    if y == 770:
        C.move(10, -50)
        time.sleep(0.1)
        y = C.getCenter().getY()
        if y < 750:
            C.move(10, 50)
            time.sleep(0.1)
            y = C.getCenter().getY()
    
    
    
        
        
        
        
    
    
    
        
    
    
        
       
        
   
    





































if __name__ == "__main__":
    main()

import turtleImport

class Artist:

    def __init__(self, t):
        self.t = t
    
    def triangle(self, size = 100):
        self.polygon(3, size)
        
    def square(self, size = 100):
        self.polygon(4, size)
        
            
    def circle(self, size = 100):
        for i in range(360):
            self.t.left(1)
            self.t.forward(1)
        

        
    def polygon(self, sides, size):
        total_angles_degree = (sides - 2)*180
        angle = total_angles_degree/sides
        for i in range(sides):
            self.t.right(180 - angle)
            self.t.forward(size)

            
    def star(self, size):
        for i in range(5):
            self.t.left(72)
            self.t.forward(size)
            self.t.right(144)
            self.t.forward(size)
   
            
    def house(self, size):
        self.polygon(4, size)
        for i in range(2):
           self.t.left(120)
           self.t.forward(size)
        
    def envelope(self, height, width, size = 57):
        for i in range(4):
             self.t.right(90)
             if i % 2  == 0:
                self.t.forward(height)
             else:
                self.t.forward(width)
        self.t.right(150)
        self.t.forward(size)
        self.t.right(59)
        self.t.forward(size)
       
        
     
       
        
        
           
        

        
    def move(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
 

def main():
    
    canvas = turtleImport.Screen()
    canvas.bgcolor("violet")
    canvas.title("Turtle Example")
    t = turtleImport.Turtle()
    t.shape("turtle")
    t.speed(100)

    #create an instance of the artist class
    art = Artist(t)
    art.triangle(80)
    art.move(130, 100)
    art.square(100)
    art.move(-120, 30)
    art.circle(50)
    art.move(-80, -80)
    art.polygon(5,80)
    art.move(100, -100)
    art.star(50)
    art.move(200, 200)
    art.house(60)
    art.move(-200, 200)
    art.envelope(49, 99)
    art.move(-200, 100)
    
 
    


if __name__ == "__main__":
    main()

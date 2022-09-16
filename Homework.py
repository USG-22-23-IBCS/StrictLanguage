class Cat:

    #constructor method has all of the instance variable (values / data)
    def __init__(self, color, size, breed):
        self.numLegs = 4 
        self.color = color
        self.size = size
        self.breed = breed

    def getColor(self):
        return self.color

    def setColor(self, c):
        self.color = c

    def getSize(self):
        return self.size

    def setSize(self, s):
        self.size = s

    def getBreed(self):
        return self.breed

    def getnumLegs(self):
        return self.numLegs



    








def main():
    cat1 = Cat("Yellow", "Small", "Korat")
    cat2 = Cat("Orange", "Big", "British Shorthair")
    print(cat1.getColor())
    print(cat1.getSize())
    print(cat1.getBreed())
    print(cat1.getnumLegs())
    cat1.setColor ("Purple")
    print(cat1.getColor())
    print(cat2.getColor())
    print(cat2.getSize())
    print(cat2.getBreed())
    print(cat2.getnumLegs())
    cat2.setSize ("Medium")
    print(cat2.getSize())
        


if __name__ == "__main__":
    main()

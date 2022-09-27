class Coffeeshop:

    def __init__(self):
        self.coffee = 14
        self.espresso = 20
        self.latte = 27
        self.small = 0
        self.medium = 1
        self.large = 2
        self.menu = "1. Coffee \n2. Espresso \n3. Latte"
        self.sizes = "1. Small (8oz) \n2. Medium (12oz) \n3. Large (16oz)"
        self.option = "1. Order \n2. Learn more about the store\n"
        self.info = "Our coffee shop is the best in Tacoma."

    def getMenu(self):
        return self.menu


    def getOption(self):
        return self.option

    def getInfo(self):
        return self.info


    def getMenuOption(self, selected):
        if selected == "1" or selected == "1. Coffee" or selected == "Coffee":
            return "coffee"
        elif selected == "2" or selected == "2. Espresso" or selected == "Espresso":
            return "espresso"
        elif selected == "3" or selected == "3. Latte" or selected == "Latte":
            return "latte"

    def getPrice(self, drink):
        if drink == "coffee":
            return self.coffee
        elif drink == "espresso":
            return self.espresso
        elif drink == "latte":
            return self.latte
        else:
            return 0.0

    def getSizes(self):
        return self.sizes

    
    def getSizeOption(self, selected):
        if selected == "1" or selected == "1. Small" or selected == "Small":
            return "small"
        elif selected == "2" or selected == "2. Medium" or selected == "Medium":
            return "medium"
        elif selected == "3" or selected == "3. Large" or selected == "Large":
            return "large"

    def getSizeExtra(self, size):
        if size == "small":
            return self.small
        elif size == "medium":
            return self.medium
        elif size == "large":
            return self.large
        else:
            return 0.0
            
       
          
        


def main():

      C = Coffeeshop()
      print("Welcome to our coffee shop! Here's our menu. Please pick an option.\n")
      print(C.getOption())
      selected = input()
      if selected == "1" or selected ==  "1. Order" or selected == "Order":
          print("What would you like to order?\n")
          print(C.getMenu())
          selected = input()
          drink = C.getMenuOption(selected)
          price = C.getPrice(drink)
          print("You selected " + drink + ".That would be $" + str(price))
          print("-------------------------------------------------------")
          print("Please select your size.\n")
          print(C.getSizes())
          selected = input()
          size = C.getSizeOption(selected)
          extraprice = C.getSizeExtra(size)
          print("You selected " + size + ".That would be extra $" + str(extraprice))
          print("-------------------------------------------------------")
          print("Your total would be $" + str(extraprice+price))
    
      
      else:
          print(C.getInfo())





if __name__ == "__main__":
    main()


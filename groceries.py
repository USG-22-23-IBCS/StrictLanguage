class GroceryStore:
    def __init__(self):
        self.grocery = {'orange' : 0.5,
                        'milk' : 4,
                        'cookies' : 3,
                        'rib eye' : 15.5,
                        'shrimp' : 7.5,
                        'king crab' : 40,
                        'egg' : 0.5,
                        'coke' : 1,
                        'instant noodle' : 1.5,
                        'chocolate' : 3}

        self.instock = {'orange' : 2,
                          'milk' : 5,
                          'cookies' : 3,
                          'rib eye' : 1,
                          'shrimp' : 3,
                          'king crab' : 2,
                          'egg' : 12,
                          'coke' : 6,
                          'instant noodle' : 2,
                          'chocolate' : 3}
        self.nameStore = "thisisnotanormalstore"
        self.nameManager = "Jenny"
        self.option = "1. Know what is available \n2. Speak to the manager \n"
        self.option2 = "1. Purchase products \n2. Finish \n "
        self.option3 = "1.Discount \n2. Food restock day \n"

    def getnameStore(self):
        return self.nameStore

    def getnameManager(self):
        return self.nameManager
    def getOption(self):
        return self.option
    def getGrocery(self):
        return self.grocery
    def getOption2(self):
        return self.option2
    def getOption3(self):
        return self.option3

    def purchase(self, shoppingList):
        total = 0.0
        for product in shoppingList:
            total = total + self.grocery[product]
        return total

    def isAvailable(self, product):
        if product in self.grocery:
            return True
        else:
            return False

    def addToCart(self, product):
        self.instock[product] = self.instock[product] - 1

    def isInStock(self, product):
        if self.instock[product] > 0:
            return True
        else:
            return False


def main():

    G = GroceryStore()
    name = G.getnameStore()
    print("Welcome to " + name + "! Please pick an option. \n")
    print(G.getOption())
    selected = input()

    if selected == "1":
        print("These are our available food today. \n")
        print(list(G.getGrocery().keys()))
        shoppingList = []
        while True:
            print("-----------------------------------")
            print("Please pick an option. \n" )
            print(G.getOption2())
            purchaseOrFinish =  input()
            if purchaseOrFinish == "1":
                print("Please type the name of the product you would like to buy. \n" )
                product = input()
                if not G.isAvailable(product):
                    print("Sorry we dont have the product")
                else:
                    if not G.isInStock(product):
                        print("Sorry we are out of stock for the product")
                    else:
                        # when product is both available and isInStock, add to shoppingList
                        shoppingList.append(product)
                        G.addToCart(product)
                        print("Added " + product + " to the cart")
            elif purchaseOrFinish == "2":
                total = G.purchase(shoppingList)
                print("Your shopping total today is " + str(total))
                break
            else:
                print("error")



    elif selected == "2":
        manager = G.getnameManager()
        print("Hi, I am " + manager + ". How can I help you? \n")
        print(G.getOption3())
        selected = input()
        if selected == "1":
            print("Discount is only applicable for customers with diamond member card.")
        elif selected == "2":
            print("Food will be restocked every Saturday.")
        








if __name__ == "__main__":
    main()









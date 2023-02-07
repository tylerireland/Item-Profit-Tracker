#This program will track all auction items and calculate the profit
import pickle
import time as t

my_items = []

class Item:
    def __init__(self,name = '', cost = 0, price = 0, state = 'SELLING', profit = 0):
        self.name = name
        self.cost = cost
        self.price = price
        self.state = state      #SOLD, SELLING, NOT SOLD
        self.profit = profit
        

    def getName(self):
        return self.name

    def setName(self, x):
        self.name = x

    def getCost(self):
        return self.cost

    def setCost(self, x):
        self.cost = x

    def getPrice(self):
        return self.price

    def setPrice(self, x):
        self.price = x

    def isSold(self):
        self.state = 'SOLD'

    def cantSell(self):
        self.state = 'NOT SOLD'

    def getState(self):
        return self.state

    def setProfit(self, x):
        self.profit = x

    def getProfit(self):
        return self.profit

        
def wait():
    t.sleep(1.0)

def LoadObjects():
    with open("MyItems.pickle", "rb") as f:  
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break      
        
def createListing(name, cost):
    with open("MyItems.pickle", "ab") as file:
        obj = Item()
        obj.setName(name)
        obj.setCost(cost)
        my_items.append(obj)
        saveObjects()
        
def saveObjects():
    with open("MyItems.pickle", "ab") as file:
        file.truncate(0)
        for x in my_items:
            pickle.dump(x,file)

def setSold(obj):
    if obj.getState() == 'SELLING':
        obj.isSold()
        price = input("Enter the price sold for: ")
        obj.setPrice(price)
        calcProfit(obj)
        SavetoText(obj)
        saveObjects()
    else:
        print("Item already sold!")
        wait()

def setUnsold(obj):
    if obj.getState() == 'SELLING':
        obj.cantSell()
        obj.setPrice = 0
        calcProfit(obj)
        SavetoText(obj)
        saveObjects()

def calcProfit(obj):
    price = obj.getPrice()
    cost = obj.getCost()
    profit = float(price) - float(cost)
    profit = round(profit, 2)
    obj.setProfit(profit)
    print("You made $" + str(profit) + " from this item!")
    wait()
  
def RemoveItem():
    item_name = input("Enter the item: ")
    for x in my_items:
        if item_name == x.getName():
            certainty = input("Are you sure you want to remove this item? (y/n) \nEnter: ")
            if certainty == 'y':
                my_items.remove(x)
                saveObjects()
            elif certainty == 'n':
                break
        
def calcNetProfit():
    net = 0.00
    for x in my_items:
        net += x.getProfit()
    net = round(net, 2)
    print("You've made $" + str(net) + " from the items sold!")
    wait()

def ListItems():
    if len(my_items) > 0:
        count = 0
        print("\tITEMS")
        for x in my_items:
            count+=1
            if x.getState() == 'SELLING':
                print(str(count) + ". " + x.getName())
            else: 
                print(str(count) + ". " + x.getName() + " **" + x.getState() + "**")

        print("\n")

def ItemCost():
    item_name = input("Enter the item: ")
    for x in my_items:
        if item_name == x.getName():
            print("Price of " + item_name + ": $" + str(x.getCost()) + "\n")
    wait()

def SavetoText(obj):
    with open("ProfitFromAuction.txt", "a") as file:
        
        name = obj.getName()
        cost = obj.getCost()
        price = obj.getPrice()
        profit = obj.getProfit()

        file.write(name + "\n\tCost: $" + str(cost) + "\n\tPrice: $" + str(price) + "\n\tProfit: $" + str(profit) + "\n\n")

try:
    my_items = list(LoadObjects())
    
except:
    print("Unable to load file.")


running = True



while(running):

    ListItems()

    choice = input("1. Add Item\n2. Mark Item as Sold/Unsold\n3. Remove Item \n4. Cost of Item \n5. Show Net Profit\n6. Quit\nEnter: ")

    if choice == '1':

        with open("ProfitFromAuction.txt","a") as file:
                
            adding = True
           
            while(adding):
                
                item_name = input("\nEnter the item name: ")
                item_name = item_name.lower()
                exists = False
                
                if len(my_items) == 0:
                    cost = input("Enter the cost: ")
                    createListing(item_name, cost)
                else:
                    for x in my_items:
                        if x.getName() == item_name:
                            exists = True

                    if exists:
                        print("Item already exists!")
                        wait()
                           
                    else:
                        cost = input("Enter the cost: ")
                        createListing(item_name, cost)
                            
                add_another = ''

                while(add_another != 'y' and add_another != 'n'):
                    add_another = input("Would you like to add another item? (y/n): ")

                    if add_another == 'n':
                        wait()
                        adding = False
                       
   

    elif choice == '2':

        with open("ProfitFromAuction.txt","a") as file:

            count = 0
            valid = True

            if len(my_items) == 0:
                print("No items!")
                wait()

            else:
                
                while valid:

                    item_name = input("Enter the item: ")
                
                    for x in my_items:
                        if x.getName() == item_name:
                            valid = False
                            soldorunsold = input("Do you want to mark iten as sold(1) or unsold(2) ?\nEnter: ")

                            if soldorunsold == '1':
                                setSold(x)  
                            elif soldorunsold == '2':
                                setUnsold(x)

                            wait()
                    if valid:
                        print("There is no item by that name, or it has already been sold!")
                        wait()
                        valid = False

                                        
                 
    elif choice == '3':
        ListItems()
        RemoveItem()
    elif choice == '4':
        ListItems()
        ItemCost()

    elif choice == '5':
        calcNetProfit()

    elif choice == '6':
        running = False

    else:
        print("Invalid Input!")
        wait()


                
            
            


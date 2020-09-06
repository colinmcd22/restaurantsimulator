# Colin McDonnell
# ITP115 Fall 19
# Final Project
# cmmcdonn@usc.edu

from MenuItem import MenuItem #imports the MenuItem class

# This class is the menu class. This class makes use of the MenuItem class to build a menu
# This class has different instance attributes that are lists defined in the constructor, but the constructor
# only takes in one parameter, the fileName("menu.csv")
class Menu(object):
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"] # list of different item types

    #constructor method for menu class
    def __init__(self, fileName):
        self.fileName = "menu.csv"
        self.menuItemDrinkList =[] # drink list
        self.menuItemAppetizerList = [] # appetizer list
        self.menuItemEntreeList = [] # entree list
        self.menuItemDessertList = [] # dessert list

        # this block of code reads through the csv file and adds the items to the proper list
        fileIn = open(self.fileName, "r")
        for line in fileIn:
            line = line.split(',')
            if line[1] == "Drink":
                line = MenuItem(line[0], line[1], line[2], line[3])
                self.menuItemDrinkList.append(line)
            elif line[1] == "Appetizer":
                line = MenuItem(line[0], line[1], line[2], line[3])
                self.menuItemAppetizerList.append(line)
            elif line[1] == "Entree":
                line = MenuItem(line[0], line[1], line[2], line[3])
                self.menuItemEntreeList.append(line)
            elif line[1] == "Dessert":
                line = MenuItem(line[0], line[1], line[2], line[3])
                self.menuItemDessertList.append(line)

        fileIn.close() #close the file



    # Input: the type of item, index of that item
    # Output: returns the proper item list
    # Side effects: none
    # description: allows the user to get the proper menu item that was ordered from the list
    def getMenuItem(self, typeItem, index):
        if typeItem == "Drink":
            return self.menuItemDrinkList[int(index)-1]

        if typeItem == "Appetizer":
            return self.menuItemAppetizerList[int(index)-1]

        if typeItem == "Entree":
            return self.menuItemEntreeList[int(index)-1]

        if typeItem == "Dessert":
            return self.menuItemDessertList[int(index)-1]






    # Input: the type of the item
    # Output: none
    # Side effects: supposed to print the menu
    # description: this method prints the menu as needed, prints each list so the user can choose an item
    def printMenuItemsByType(self, typeItem):
        if typeItem.lower() == "drink":
            print("\n------DRINKS------")
            count = 1
            for x in self.menuItemDrinkList: #loops through the list
                print(str(count) + ": " + str(x))
                count +=1

        if typeItem.lower() == "appetizer":
            print("\n------APPETIZERS------")
            count = 1
            for x in self.menuItemAppetizerList:
                print(str(count) + ": " + str(x))
                count += 1

        if typeItem.lower() == "entree":
            print("\n------ENTREES-----")
            count = 1
            for x in self.menuItemEntreeList:
                print(str(count) + ": " + str(x))
                count += 1

        if typeItem.lower() == "dessert":
            print("\n------DESSERT------")
            count = 1
            for x in self.menuItemDessertList:
                print(str(count) + ": " +  str(x))
                count+=1


    # Input: the type of the item
    # Output: returns the length of the proper list
    # Side effects: none
    # description: picks the correct list and returns the length of it
    def getNumMenuItemsByType(self, typeItem):
        if typeItem.lower() == "drink":
            num = len(self.menuItemDrinkList)
            return num

        if typeItem.lower() == "appetizer":
            num = len(self.menuItemAppetizerList)
            return num

        if typeItem.lower() == "entree":
            num = len(self.menuItemEntreeList)
            return num

        if typeItem.lower() == "dessert":
            num = len(self.menuItemDessertList)
            return num


    





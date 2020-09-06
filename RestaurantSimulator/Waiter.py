# Colin McDonnell
# ITP115 Fall 19
# Final Project
# cmmcdonn@usc.edu

from Menu import Menu # imports the menu class
from Diner import Diner # imports the diner class


# This is the waiter class. This class makes use of the Menu and Diner objects. This class represents the waiter.
# The waiter maintains a list of the diners it is currently taking care of, and progresses them through the different
# stages of the restaurant. The waiter in the simulation will repeat multiple cycles of attending to the diners.
# In each cycle, the waiter will seat a new diner, take any diner's orders, and give diners their bill according to each status
class Waiter(object):
    # constructor method for waiter class with a menu object passed through and a diner list create
    def __init__(self, menuObj):
        self.diners = []
        self.menuObj = menuObj

    # Input: a diner object
    # Output: none
    # Side effects: none
    # description: allows the user to add a diner to the waiters list of diners
    def addDiner(self, dinerObj):
        self.diners.append(dinerObj)

    # Input: none
    # Output: returns an integer that represents the number of diners
    # Side effects: none
    # description: allows the user to get the number of diners the waiter is keeping track of
    def getNumDiners(self):
        return len(self.diners)

    # Input: none
    # Output: none
    # Side effects: supposed to group diners by status and print each diner
    # description: This method created 5 different lists based on status, it then adds a diner to each list
    # The method then loops through each list and prints who is doing what
    def printDinerStatuses(self):
        seated = []
        ordering = []
        eating = []
        paying = []
        leaving = []

        for ppl in self.diners: # appends proper diners to each list
            stat = ppl.getStatus()

            if stat == 0:
                seated.append(ppl)
            elif stat == 1:
                ordering.append(ppl)
            elif stat == 2:
                eating.append(ppl)
            elif stat == 3:
                paying.append(ppl)
            elif stat == 4:
                leaving.append(ppl)


        print("Diners that are seated: ")
        for x in range(len(seated)):
            print("\t" + str(seated[x]))
        print("Diners that are ordering: ")
        for x in range(len(ordering)):
            print("\t" +str(ordering[x]))
        print("Diners that are eating: ")
        for x in range(len(eating)):
            print("\t" + str(eating[x]))
        print("Diners that are paying: ")
        for x in range(len(paying)):
            print("\t" + str(paying[x]))
        print("Diners that are leaving: ")
        for x in range(len(leaving)):
            print("\t" + str(leaving[x]))

    # Input: none
    # Output: none
    # Side effects: supposed to take the order of the diner and add it to their order list
    # description: This method loops through the diner list, checks if they are ordering, and then loops through the item type list
    # to print out the item that the diner is supposed to be order. There is error checking while loops
    # This method then adds the order and prints it
    def takeOrders(self):
        for stat in self.diners: # loop thru diners
            if stat.getStatus() == 1: # check if order
                print("\n" + stat.getName() + ", you are ordering.")
                for itemType in Menu.MENU_ITEM_TYPES: # loop thru the menu item types
                    bools = True # variable to error check with
                    types = Menu("menu.csv").printMenuItemsByType(itemType)
                    order = input(stat.getName() + ", please select a " + str(itemType) + " menu item number.") # input for order
                    while bools:
                        if not order.isalpha():
                            int(order)
                            if int(order) <= int(Menu('menu.csv').getNumMenuItemsByType(itemType)) and int(order) > 0:
                                bools = False
                            else:
                                order = input(stat.getName() + ", please enter a valid response.")
                        else:
                            order = input(stat.getName() + ", please enter a valid response.")
                    item = Menu("menu.csv").getMenuItem(itemType, order) # gets the menu item ordered
                    stat.addToOrder(item) # adds the item to the order list for the diner
                stat.printOrder() # prints their whole order

    # Input: none
    # Output: none
    # Side effects: none
    # description: this method simply uses calculate cost to print out the diners total cost
    def ringUpDiners(self):
        for stat in self.diners:
            if stat.getStatus() == 3:
                cost = stat.calculateMealCost()
                print("\n" + stat.getName() + ",your total cost is " + str(cost))

    # Input: none
    # Output: none
    # Side effects: none
    # description: this method removes the diners that are leaving from the diner list by looping backwards
    def removeDoneDiners(self):
        for stat in range(len(self.diners)-1, -1, -1): # loop backwards
            if self.diners[stat].getStatus() == 4:
                print("\n" + self.diners[stat].getName() + ", thank you for dining with us today!")
                self.diners.remove(self.diners[stat]) # remove the proper diner

    # Input: none
    # Output: none
    # Side effects: none
    # description: this method makes use of all the previous method to advacne the diner, take their order, ring them up,
    # and then remove the finished diner, and finally it updates the status of each diner
    def advanceDiners(self):
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
        for person in self.diners:
            person.updateStatus()






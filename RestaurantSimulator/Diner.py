# Colin McDonnell
# ITP115 Fall 19
# Final Project
# cmmcdonn@usc.edu

from MenuItem import MenuItem # imports menu item class

# This is the diner class. This class represents one of the diners at the restaurant and keeps track of their status and meal
# The constructor in this class defines dinerName, order, and status of the diner
# There are different methods created to manipulate each attribute
class Diner(object):
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"] # list of different stats

    # constructor method for diner, dinerName is passed through and order and status are defined
    def __init__(self,dinerName):
        self.dinerName = dinerName
        self.order = [] # make a list
        self.status = 0 # set it to zero

    # Input: none
    # Output: returns the name of the diner
    # Side effects: none
    # description: allows the user to get the name of the diner in a different class
    def getName(self):
        return self.dinerName

    # Input: a string new diner name
    # Output: none
    # Side effects: none
    # description: allows the user to set the name of the diner in a different class
    def setName(self, newDinerName):
        self.dinerName = newDinerName

    # Input: none
    # Output: returns the order of the diner
    # Side effects: none
    # description: allows the user to get the order of the diner in a different class
    def getOrder(self):
        return self.order

    # Input: a string new order
    # Output: none
    # Side effects: none
    # description: allows the user to set the order of the diner in a different class
    def setOrder(self, newOrder):
        self.order = newOrder

    # Input: none
    # Output: returns the status of the diner
    # Side effects: none
    # description: allows the user to get the status of the diner in a different class
    def getStatus(self):
        return self.status

    # Input: a string new status
    # Output: none
    # Side effects: none
    # description: allows the user to set the status of the diner in a different class
    def setStatus(self, newStatus):
        self.status = newStatus

    # Input: none
    # Output: none
    # Side effects: none
    # description: allows the status to be increased by 1 in a different class
    def updateStatus(self):
        self.status += 1

    # Input: a menu item object
    # Output: none
    # Side effects: none
    # description: allows the user to add to the order of the specific diner in a different class
    def addToOrder(self, menuItem):
        self.order.append(menuItem)


    # Input: none
    # Output: none
    # Side effects: none
    # description: allows the user to print the order of the diner in a different class
    def printOrder(self):
        print("\n" + self.dinerName + " ordered: " )
        for x in range(len(self.order)):
            print(self.order[x])

    # Input: none
    # Output: the total cost of the diners meal
    # Side effects: none
    # description: allows the user to calculate the order cost of the diner in a different class
    def calculateMealCost(self):
        cost = 0
        for var in self.order:
            cost += float(var.getPrice())
        return cost

    # Input: none
    # Output: a str message of their status
    # Side effects: none
    # description: allows the user to get a string descrption of the status of the diner
    def __str__(self):
        msg = self.dinerName + " is currently "
        if self.status == 0:
            msg += "seated"
        elif self.status == 1:
            msg+= "ordering"
        elif self.status == 2:
            msg+= "eating"
        elif self.status == 3:
            msg +="paying"
        elif self.status == 4:
            msg += "leaving"

        return msg




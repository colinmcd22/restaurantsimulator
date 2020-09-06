# Colin McDonnell
# ITP115 Fall 19
# Final Project
# cmmcdonn@usc.edu

# This class is the MenuItem class. This class represents a single item that a diner can
# order from the restaurant's menu. There are 4 instance attributes passed through the constructor
# and each method has a getter and setter method. Finally, there is a str method to print the proper output.

class MenuItem(object):
    def __init__(self,name,typeItem,price,description):
        self.name = str(name) # name of item
        self.typeItem = str(typeItem) # the type of item
        self.price = float(price) # price of the item
        self.description = str(description) # short description of the item

    # Input: none
    # Output: none
    # Side effects: none
    # description: get method for name
    def getName(self):
        return self.name

    # Input: new name
    # Output: none
    # Side effects: none
    # description: allows user to set a new name
    def setName(self,newName):
        if newName.isalpha():
            self.name = newName

    # Input: none
    # Output: none
    # Side effects: none
    # description: get method for type of the item
    def getTypeItem(self):
        return self.typeItem

    # Input: new item type
    # Output: none
    # Side effects: none
    # description: allows user to set a new item type
    def setTypeItem(self,newTypeItem):
        if newTypeItem.isalpha():
            self.typeItem = newTypeItem

    # Input: none
    # Output: none
    # Side effects: none
    # description: get method for price
    def getPrice(self):
        return self.price

    # Input: new price
    # Output: none
    # Side effects: none
    # description: allows user to set a new price
    def setPrice(self,newPrice):
        if newPrice.isalpha():
            self.name = newPrice

    # Input: none
    # Output: none
    # Side effects: none
    # description: get method for description
    def getDescription(self):
        return self.description

    # Input: new description
    # Output: none
    # Side effects: none
    # description: allows user to set a new description
    def setDescription(self, newDescription):
        if newDescription.isalpha():
            self.name = newDescription



    # Input: none
    # Output: returns a string message
    # Side effects: none
    # description: allows user to call this method to print the item features in a nice way
    def __str__(self):
        msg = self.name + " (" + self.typeItem + "): " + str(self.price) + "\n"
        msg += self.description
        return msg




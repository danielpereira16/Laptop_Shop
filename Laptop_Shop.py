#Laptop Shop Bot
import random
from random import randint

#List of random names
names = ["Caleb", "Shawn", "Sean", "Gian", "Jayden", "Ryan", "Daniel", "Danett", "Hannah", "Teresa" ]

# Welcome message with random name
def welcome():
    '''
    Purpose: To generate a random name form the list and print out
    a welcome message
    Parameters: None
    Returns: None
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to Dream Pizza ***")
    print("*** my name is ",name, "***")
    print("*** I will be here to help you order your delicious Dream Pizza ***")

# Menu for Pickup and Delivery
def pickup():
    print ("Do you want your order delivered or are you picking it up")
    print ("For pickup please enter 1") 
    print ("For delivery please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Pickup")
                    break

                elif delivery == 2:
                    print ("Delivery")
                    break
            else:
                print("Number must be 1 or 2")
        except ValueError:
            print ("That was not a valid input")
            print ("Please enter 1 or 2 ")



# Pickup information - Name and Phone




# Delivery information - Name, Address and Phone




# Choose total number of items




# Item List




# Item(s) ordered - from item list - print each ordered item with cost




# Print order out - including if the order is pickup or delivery and names and prices of each item - total cost including any delivery charge




# Ability to cancel or proceed with order




# Option for new order or to exit




# Main Function
def main():
    '''
    Purpose: To run all functions
    A welcome message
    Parameters: None
    Returns: None
    '''
    welcome()
    pickup()


main()
import random
from random import randint

#List of random names
names = ["Caleb", "Shawn", "Sean", "Gian", "Jayden", "Ryan", "Daniel", "Danett", "Hannah", "Teresa" ]

def welcome():
    '''
    Purpose: To generate a random name form the list and print out
    a welcome message
    Parameters: None
    Returns: None
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to my Laptop Shop ***")
    print("*** my name is ",name, "***")
    print("*** I will be here to help you order the right and perfect laptop for you ***")


def main():
    '''
    Purpose: To run all functions
    A welcome message
    Parameters: None
    Returns: None
    '''
    welcome()


main()
# Laptop Shop Bot
# 26.03.22
# Bugs - Phone Number allows letters
#      - Name allows numbers

import random
from random import randint

#List of random names
names = ["Caleb", "Shawn", "Sean", "Gian", "Jayden", "Ryan", "Daniel", "Danett", "Hannah", "Teresa" ]
#List of laptop names
laptop_names = ['Asus 14" Laptop - Intel Celeron 4GB-RAM 128GB','Asus 15.6" Laptop - Intel Core i7 16GB-RAM 512GB-SSD',
'Asus TUF 15.6" Gaming Laptop - Intel Core i5 8GB-RAM 512GB-SSD','Apple MacBook Air 13" with M1 Chip 512GB',
'Apple MacBook Pro 13" with M1 Chip 512GB','HP 15.6" Laptop - Intel Core i5 8GB-RAM 256GB-SSD',
'HP Pavilion 15.6" Laptop - AMD Ryzen5 16GB-RAM 512GB-SSD','HP Spectre x360 13.5" 2-in-1 Laptop - Intel Core i7 16GB-RAM 512GB-SSD',
'HP Envy x360 15.6" 2-in-1 Laptop - AMD Ryzen5 16GB-RAM 512GB-SSD','Acer Swift 3 14" Laptop - Intel Core i5 8GB-RAM 512GB-SSD',
'Acer TravelMate Spin B3 11.6" 2-in-1 Laptop with Pen - Intel Pentium 4GB-RAM 128GB-SSD',
'Acer Aspire 5 15.6" Laptop - AMD Ryzen5 8GB-RAM 256GB-SSD','Microsoft Surface Laptop 4 15" - AMD Ryzen7 8GB-RAM 256GB-SSD',
'Microsoft Surface Laptop 4 13.5" - Intel i5 16GB-RAM 512GB-SSD','Microsoft Surface Laptop Studio 14.4" - Intel i5 16GB-RAM 256GB-SSD',
'Lenovo IdeaPad 3 15.6" Laptop - Intel Pentium Silver 8GB-RAM 128GB-SSD','Lenovo Yoga 7i 14" 2-in-1 Laptop - Intel Core i5 16GB-RAM 512GB-SSD',
'Lenovo IdeaPad Flex 5 14" 2-in-1 Laptop - AMD Ryzen5 16GB-RAM 512GB-SSD']
#List of laptop prices
laptop_prices = [688,1884,1994,2149,2549,1584,1994,3997,3128,1698,836,1298,2499,2549,2699,994,2388,1984]

#list to store ordered laptops
order_list = []
#list to store laptop prices
order_cost = []

# Customer details dictionary
customer_details = {}

# validates inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This cannot be blank")

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
    print("*** Welcome to my Laptop Shop ***")
    print("*** my name is ",name, "***")
    print("*** I will be here to help you order the right and perfect laptop for you ***")

# Menu for Pickup and Delivery
def order_type():
    print ("Is your order for Click and Collect or delivery")
    print ("For Click and Collect please enter 1") 
    print ("For delivery please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Click and Collect")
                    Click_and_Collect_info()
                    break
                elif delivery == 2:
                    print ("Delivery")
                    delivery_info()
                    break
            else:
                print("Number must be 1 or 2")
        except ValueError:
            print ("That was not a valid input")
            print ("Please enter 1 or 2 ")

# Pickup information - Name and Phone
def Click_and_Collect_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question )
    #print(customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    #print(customer_details['phone'])
    print(customer_details)

# Delivery information - Name, Address and Phone
def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question )
    print(customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print(customer_details['phone'])

    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question)
    print(customer_details['house'])

    question = ("Please enter your street name ")
    customer_details['street'] = not_blank(question)
    print(customer_details['street'])

    question = ("Please enter your suburb ")
    customer_details['suburb'] = not_blank(question)
    print(customer_details['suburb'])
    print(customer_details)

# Item List
def list():
    number_laptops = 18

    for count in range (number_laptops):
        print("{} {} ${:.2f}"   .format(count+1,laptop_names[count],laptop_prices[count]))

# Choose total number of items - max 20
# Item(s) ordered - from item list - print each ordered item with cost
def order_laptops():
    # ask for total number of laptops for order
    print("Please note that due to covid, there has been delays in shipping and therefore you can only order a maximum of 20 Laptops per order")
    num_laptops = 0
    while True:
        try:
            num_laptops = int(input("How many Laptops do you want to order? "))
            if num_laptops >= 1 and num_laptops <= 20:
                break
            else:
                print("Your order must between 1 and 20")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter number enter between 1 and 20 ")
    # Choose laptops from the list
    for item in range(num_laptops):
        while num_laptops > 0:
            while True:
                try:
                    laptops_ordered = int(input("Please choose your laptops by entering the number from the list "))
                    if laptops_ordered >= 1 and laptops_ordered <= 18:
                        break
                    else: 
                        print("Your number must be between 1 and 20")
                except ValueError:
                        print ("That is not a valid number")
                        print ("Please enter number enter between 1 and 20 ") 
            laptops_ordered = laptops_ordered -1
            order_list.append(laptop_names[laptops_ordered])
            order_cost.append(laptop_prices[laptops_ordered])    
            print("{} ${:.2f}" .format(laptop_names[laptops_ordered],laptop_prices[laptops_ordered]))
            num_laptops = num_laptops-1

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
    order_type()
    list()
    order_laptops()

main()
# Laptop Shop Bot
# 26.03.22
# Bugs - Phone Number allows letters
#      - Name allows numbers

# Different types of modules being imported into the code
import sys
# Importing the module of sys which is a module
# that provides access to some objects used or
# maintained by the interpreter
import random
# Importing the module of random which is a
# module that is used to generate random things
from random import randint
# From the module of random,
# it imports the module of randint
# which returns an integer number from a
# specified range of numbers


# Constants - Variables that hold a value but will not change
LOW = 1
# Constant used in order type, order confirm or cancel,
# and starting a new order or exiting the program
HIGH = 2
# Constant used in order type, order confirm or cancel,
# and starting a new order or exiting the program
PH_LOW = 7
# Constant used in phone number
PH_HIGH = 10
# Constant used in phone number
HOUSE_LOW = 1
# Constant used in house number
HOUSE_HIGH = 3500
# Constant used in house number


# List of random names used at the beginning of
# the code when starting the program and the welcome message appears
names = ["Caleb", "Shawn", "Sean", "Gian",
         "Jayden", "Ryan", "Daniel", "Danett", "Hannah", "Teresa"
         ]


# List of laptop names.
# These laptop names are the different products that the
# store has to offer for sale
laptop_names = ['Asus 14" Laptop - Intel Celeron 4GB-RAM 128GB-SSD',
                'Asus 15.6" Laptop - Intel Core i7 16GB-RAM 512GB-SSD',
                'Asus 15.6" Laptop - Intel Core i5 8GB-RAM 512GB-SSD',
                'Apple MacBook Air 13" with M1 Chip 512GB-SSD',
                'Apple MacBook Pro 13" with M1 Chip 512GB-SSD',
                'HP 15.6" Laptop - Intel Core i5 8GB-RAM 256GB-SSD',
                'HP Pavilion 15.6" Laptop - AMD Ryzen5 16GB-RAM 512GB-SSD',
                'HP 13.5" 2-in-1 Laptop - Intel Core i7 16GB-RAM 512GB-SSD',
                'HP Envy 15.6" 2-in-1 Laptop - AMD Ryzen5 16GB-RAM 512GB-SSD',
                'Acer 14" Laptop - Intel Core i5 8GB-RAM 512GB-SSD',
                'Acer 11.6" 2-in-1 Laptop - Intel Pentium 4GB-RAM 128GB-SSD',
                'Acer Aspire 5 15.6" Laptop - AMD Ryzen5 8GB-RAM 256GB-SSD',
                'Microsoft Surface Laptop 15" - AMD Ryzen7 8GB-RAM 256GB-SSD',
                'Microsoft Surface Laptop 13.5" - Intel i5 16GB-RAM 512GB-SSD',
                'Microsoft Surface Laptop 14.4" - Intel i5 16GB-RAM 256GB-SSD',
                'Lenovo 15.6" Laptop - Intel Pentium 8GB-RAM 128GB-SSD',
                'Lenovo 14" 2-in-1 Laptop - Intel Core i5 16GB-RAM 512GB-SSD',
                'Lenovo 14" 2-in-1 Laptop - AMD Ryzen5 16GB-RAM 512GB-SSD'
                ]


# List of laptop prices.
# These are the prices for the different laptops
# the store has to offer for sale
laptop_prices = [688, 1884, 1994, 2149, 2549, 1584, 1994,
                 3997, 3128, 1698, 836, 1298, 2499, 2549,
                 2699, 994, 2388, 1984
                 ]


# list to store ordered laptops. When ordering the laptops,
# the program will append all the names of the laptops
# which are ordered
order_list = []


# list to store laptop prices. When ordering the Laptops,
# the program will append all the costs of the laptops
# which are ordered
order_cost = []


# Customer details dictionary - Is a dictionary (a list)
# which can hold customer details and has a variable name.
# It allows the user to take information out more easily
customer_details = {}


# validates string inputs to check if they are a string
# takes question as parameter
# returns response in title class if valid


def check_string(question):
    while True:
        # sets up while true loop
        response = input(question)
        # asks for input(string)
        x = response.isalpha()
        # checks that the input is in alphabetical
        # and sets x to True if alpha
        if x is False:
            # if x is False prints error message
            print("Input must only contain letters.")
        else:
            return response.title()
            # if True returns response in title class


# validates inputs to check if they an integer
# takes low, high and question as parameters
# returns input if the integer is valid


def val_int(low, high, question):
    while True:
        # sets up while loop
        try:
            # the program will print the statement
            # (question) which is asking for an input
            num = int(input(question))
            # asks for input(integer)
            if num >= low and num <= high:
                # if num is inside or equal
                # to the one of the numberic
                # boundaries, it will return num.
                return num
            else:
                # if num is outside of the numeric boundaries
                # an error message
                    print(f"Please enter a number between {low} and {high}.")
        except ValueError:
            # if the input is not an integer it will go to the
            # except code and print an error message followed
            # by an instruction
            print ("That is not a valid number.")
            # Error Print Statement
            print(f"Please enter a number between {low} and {high}.")
            # Instruction print statement


# Validates phone number to check if it is between 7 to 10 digits
# takes low, high and question as parameters
# returns input if the input is an integer and has 7 to 10 digits


def check_phone(question, PH_LOW, PH_HIGH):
    while True:
        # sets up while loop
        try:
            # the program will print the statement
            # (question) which is asking for an input
            num = int(input(question))
            # asks for input(integer)
            test_num = num
            # sets test_number to equal number which
            # allows program to pull apart the number
            # which is inputted to make sure it is a number
            count = 0
            while test_num > 0:
                # starts another while loop where
                # test_num is bigger than 0
                test_num = test_num//10
                # test_num is being divided by 10 to
                # split up the number
                count = count + 1
                # since count is equal to 0,
                # every digit will be
                # counted to check the number of
                # digits that have been entered
            if count >= PH_LOW and count <= PH_HIGH:
                # if count is inside or equal
                # to one of the numeric boundaries,
                # it will return num.
                return num
            else:
                # if num is outside of the numeric
                # boundaries an error message
                print("NZ phone numbers have between 7 and 10 digits")
        except ValueError:
            # if the input is not an integer it will go
            # to the except code and print an error
            # message followed by an instrction
            print ("That is not a valid number.")
            # Error Print Statement
            print("Please enter a number.")
            # Instruction print statement


# Generates message with a random name
# from the list called names and prints it out
# No Parameters
# No Returns


def welcome():
    '''
    Purpose: To generate a random name form the list and print out
    a welcome message
    Parameters: None
    Returns: None
    '''
    num = randint(0, 9)  # setting num to randint which returns
    # an integer number from a specified range
    # of numbers, 0 to 9 in this case
    name = (names[num])
    # setting name to equal the list of names at the index of
    # the random numbers. Each word in a list has an index
    # number with the first one starting with 0 unless specified
    print()  # prints blank space
    print("*** Welcome to my Laptop Shop ***")
    # Print statement welcoming user to online shop with help of bot
    print("*** my name is ", name, "***")
    # Print statement which introduces the person
    # helping including the random name
    print("*** I will be here to help you order the perfect laptop ***")
    # Print statement stating what the program will help you achieve
    print()  # prints blank space


# Creates the option to choose either pickup or delivery
# takes in Low, High and question as parameters when
# sending to the validate integer input function
# returns del_pick information at the end of the function


def order_type():
    del_pick = ""  # Sets del_pick to empty
    question = (f"For Click and Collect please enter {LOW}."
                f"\nFor Delivery please enter {HIGH}."
                f"\nPlease enter the number of your selected choice: ")
#               The question which asks if the user type in 1 or 2
#               depending on if they want delivery or pickup
    print ("Is your order for Click and Collect or delivery.")
    # Print statement which informs customer
    # they are going to have to choose between delivery and pickup
    print ("Please note that a $9.00 delivery fee will be "
           "added if you have chosen less than 5 items.")
    # Print Statement informing customer that if they choose
    # delivery and have less than 5 items in the order they
    # will be charged a $9.00 delivery fee
    delivery = val_int(LOW, HIGH, question)
    # sets delivery to equal validate input which sends
    # input through the function of validate input which
    # checks if the input is an integer and if it fits in
    # the numeric boundaries set by low and high
    if delivery == 1:  # If Delivery is equal to 1
        print()  # prints blank space
        print ("Click and Collect")
        # Prints statement stating Click and collect
        # to show you have chosen click and collect
        del_pick = "Click and Collect"
        # sets del_pick to equal click and collect
        # (will be used in the order print statement function)
        Click_and_Collect_info()
        # Opens and runs the function called click and collect info
    else:  # if delivery is the other option, 2
        print()  # prints blank space
        print ("Delivery")  # Prints statement stating
        # Delivery to show you have chosen Delivery
        del_pick = "Delivery"  # sets del_pick to equal
        # delivery (will be used in the order print statement function)
        delivery_info()  # Opens and runs the function called delivery info
    return del_pick  # returns del_pick information back to del_pick


# Pickup information - Name and Phone
# takes in Low, High and question as parameters when sending
# - to check the string function for name
# - to check the phone function for phone number
# No returns


def Click_and_Collect_info():
    question = ("Please enter your name: ")
    # question asking for name
    customer_details['name'] = check_string(question)
    # customer name will equal to check string which
    # sends input through the function of check string
    print(customer_details['name'])
    # prints the customer name once answer is
    # returned from the check string function

    question = ("Please enter your phone number: ")
    # question asking for phone number
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)
    # customer phone number will equal to check phone
    # which sends input through the function of check phone
    print(customer_details['phone'])
    # prints the customers phone number once the
    # answer is returned from the check phone function
    print(customer_details)
    # prints all information stored in the customer_details library
    print()  # prints blank space


# Delivery information - Name, Address and Phone
# takes in Low, High and question as parameters when sending
# - to check the string function for name, street name,
#   street suffix, and suburb
# - to check the phone function for phone number
# - to validate input function for house number
# No returns


def delivery_info():
    question = ("Please enter your name: ")
    # question asking for name
    customer_details['name'] = check_string(question)
    # customer name will equal to check string which sends
    # input through the function of check string
    print(customer_details['name'])
    # prints the customer name once answer is returned
    # from the check string function

    question = ("Please enter your phone number: ")
    # question asking for phone number
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)
    # customer phone number will equal to check phone which
    # sends input through the function of check phone
    print(customer_details['phone'])
    # prints the customers phone number once the answer
    # is returned from the check phone function

    question = ("Please enter your house number without any"
                "sub-address number or letter, e.g 12 not 12a: "
                )  # question asking house number without any sub-address info
    customer_details['house'] = val_int(HOUSE_LOW, HOUSE_HIGH, question)
    # customer house number number will equal to validate input
    # which sends input through the function of validate input
    print(customer_details['house'])
    # prints the customers house number once the answer
    # is returned from the validate input function

    question = ("Please enter your street name without the street suffix: ")
    # question asking for street name without street suffix
    customer_details['street name'] = check_string(question)
    # customer street name will equal to check string which sends
    # input through the function of check string
    print(customer_details['street name'])
    # prints the customer street name without suffix once
    # answer is returned from the check string function

    question = ("Please enter your street suffix, e.g cresent: ")
    # question asking for street suffix
    customer_details['street suffix'] = check_string(question)
    # customer street suffix will equal to check string which sends
    # input through the function of check string
    print(customer_details['street suffix'])
    # prints the customer street suffix once
    # answer is returned from the check string function

    question = ("Please enter your suburb: ")
    # question asking for suburb
    customer_details['suburb'] = check_string(question)
    # customer street name will equal to check string which sends
    # input through the function of check string
    print(customer_details['suburb'])
    # prints the customer suburb once
    # answer is returned from the check string function
    print()  # prints blank space

    special_instructions()
    # opens and runs the function called special instructions


# creates an input which the customer can use to add
# information they wish to about the delivery such as
# the sub-address etc. This is allowed to be left blank
# no parameters
# Returns answer at a later date in title class


def special_instructions():
    print()  # prints blank space
# question which asks the customer if they wish to
# give an special instructions or information
    question = input(f"Do you have any special instructions we need to know?"
                     f"\nThis could be your sub-address number"
                      "e.g 12a or 1/10."
                     f"\nThis could also be any information we need to "
                      "know when delivering the package such as time or "
                      "location? \n").title()
# will store answer in title class
    customer_details['special'] = question
    # sends the information from the question into
    # the customer details dictionary to be called at a later time
    print()  # prints blank space


# Prints out the list of laptops with their name, price and index number.
# No Parameters
# No Returns


def list():
    number_laptops = 18
    # sets the number of laptops to 18 as their are only 18 laptops for sale
    print("All Laptops are ordered by the brand of the laptop")
    # print statement explaining how the laptops are ordered
    for count in range(number_laptops):
        # the code will count through 18 times until no more numbers are left
        print("{} {} ${:.2f}"   .format(count+1, laptop_names[count],
              laptop_prices[count]))
        # formats the list into 3 columns,
        # - 1 for the index number,
        # - 1 for the names of the pizzas,
        # - 1 for the price formatted with a dollar sign to 2 decimal places
    print()  # prints blank space

# Choose total number of laptops - max 20
# Item(s) ordered - from item list - print each ordered item with cost
# takes num_low, num_high, question as parameters when sending
# - to validate integer for number of laptops the customer wants
# takes list_low, list_high, question as parameters when sending
# - to validate integer for which laptops the customer wants
# No returns


def order_laptops():
    # ask for total number of laptops for order
    print("Please note that due to covid,"
          "there has been delays in shipping and"
          " therefore you can only order a maximum"
          " of 20 Laptops per order")
    # print statement stating the max amount of laptops you can buy
    # in one order
    num_laptops = 0
    # sets number of laptops to equal 0
    NUM_LOW = 1
    # constant used in num_laptops
    NUM_HIGH = 20
    # constant used in num_laptops
    LIST_LOW = 1
    # constant used in laptops_ordered
    LIST_HIGH = 18
    # constant used in laptops_ordered
    print("Please enter the number of laptops you would like to purchase.")
    # print statement asking how many laptops the customer would like to order
    question = (f"The number must be between {NUM_LOW} and {NUM_HIGH}: ")
    # Question which includes the numeric boundaries the
    # number must be in or equal to
    num_laptops = val_int(NUM_LOW, NUM_HIGH, question)
    # sets num_laptops to equal validate input which sends input
    # through the function of validate input which checks if the
    # input is an integer and if it fits in the numeric boundaries
    # set by low and high
    print()  # prints blank space
    # Choose laptops from the list
    for item in range(num_laptops):
        # the code will count through the number of laptops chosen,
        # meaning it will repeat the same code until there
        # are no more numbers left
        while num_laptops > 0:
            # starts another while loop where num_laptops is bigger than 0
                print("Please choose your laptops by entering a number"
                      "from the list above.")
                # print statement informing customer to choose laptop
                # by entering number from the list above
                question = (f"The number must be between {LIST_LOW}"
                             "and {LIST_HIGH}: ")
                # Question which includes the numeric boundaries the
                # number must be in or equal to
                laptops_ordered = val_int(LIST_LOW, LIST_HIGH, question)
                # sets num_laptops to equal validate input which sends input
                # through the function of validate input which checks if the
                # input is an integer and if it fits in the numeric boundaries
                # set by low and high
                laptops_ordered = laptops_ordered - 1
                # sets laptops_ordered equal laptops_ordered - 1 which means
                # that every time a number is inputted, the num_laptops
                # decreases by 1 till it is 0 and the code will stop repeating
                order_list.append(laptop_names[laptops_ordered])
                # appends (sends) the laptops name to the order_list
                # which will store the information
                order_cost.append(laptop_prices[laptops_ordered])
                # appends (sends) the laptops prices to the order_cost
                # which will store the information
                print("{} ${:.2f}" .format(laptop_names[laptops_ordered],
                                           laptop_prices[laptops_ordered]))
# prints the information in two columns
# - one for the name of the laptop
# - one for the price fromatted by a $ sign and 2 decimal places
                num_laptops = num_laptops - 1
                # sets num_laptops equal to num_laptops - 1 which means
                # that every time a number is inputted, the num_laptops
                # decreases by 1 till it is 0 and the code will stop repeating
                print()  # prints blank space


# Print order out - including
# - if the order is pickup or delivery
# - customer details
# - names and prices of each item - total cost including any delivery charge
# Takes del_pick as a parameter
# No returns


def print_order(del_pick):
    print()  # prints blank space
    total_cost = sum(order_cost)
    # sets total cost to equal the sum of all the prices of the laptops ordered
    print("Customer Details")
    # prints statement which tells user that customer details are to follow
    if del_pick == "Click and Collect":
        # if del_pick was to equal Click and Collect from the order_type
        # function it would print the information required
        print("Your order is for Click and Collect.")
        # print statement stating that the order if for click and collect
        print(f"Customer Name: {customer_details['name']}"
              f"\nCustomer Phone: {customer_details['phone']}")
        # prints customers name and phone number formatted as
        # Customer Name: Daniel and then below it Customer Phone: 09049950906
    elif del_pick == "Delivery":
        # if del_pick was to equal delivery from the order_type
        # function it would print the information required
        print("Your order is for Delivery.")
        # print statement stating that the order if for delivery
        print(f"Customer Name: {customer_details['name']}"
              f"\nCustomer Phone: {customer_details['phone']}"
              f"\nCustomer Address: {customer_details['house']}"
              f"{customer_details['street name']}"
              f"{customer_details['street suffix']}"
              f"{customer_details['suburb']}")
        # prints customers name, phone number, house number,
        # street name, street suffix, suburb
        # formatted the same was as the click and collect is
        print("Special instructions: {}".format(customer_details['special']))
        # prints the special information
    print()  # prints blank space
    print("Order Details")
    # prints statement which tells the user the order details are to follow
    count = 0
    # sets the count to equal 0
    for item in order_list:
        # for every laptops that is in the order list
        print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
        # it will print the information in 2 columns
        # - The first will have the laptop names
        # - The second will have the laptops prices
        #   formatted with a $ sign to 2 decimal places
        count = count + 1
        # sets count to equal count + 1 so as every laptop is printed
        # the count will rise till their are no more laptops left
        # in the list, and the laptops should all be printed
    print()  # prints blank space
    if del_pick == "Delivery":
        # if del_pick is equal to Delivery
        if len(order_list) >= 5:
            # if the length of the list is more than 5 index numbers
            # then a print statement will print out stating that the
            # order is delivered for free
            print("Your order will be Delivered to you for free.")
            # print statement which tells the customer the order
            # will be delivered for free
        elif len(order_list) < 5:
            # if the length of the list is less than 5 index numbers
            # then a print statement will print out stating that
            # their will be a $9.00 delivery fee
            print("Just a reminder, due to the fact that you have ordered "
                  "less than 5 items, there is a $9.00 fee for delivery.")
            # print statement which tells the customer that their
            # will be a $9.00 delivery fee
            total_cost = total_cost + 9
            # sets total cost for delivery if the amount of items
            # ordered are less than 5 to equal to the total cost + 9
            # which is the delivery fee
    print("Total Order Cost")
    # print statement telling the customer the total cost is to follow
    print(f"${total_cost:.2f}")
    # print statement which prints the final cost formatted
    # with a $ sign and to 2 decimal places
    print()  # prints blank space


# Ability to cancel or proceed with order
# takes in Low, High and question as parameters
# when sending to the validate integer input function
# no returns


def confirm_cancel():
    question = (f"To Confirm please enter {LOW}."
                f"\nTo Cancel please enter {HIGH}."
                f"\nPlease enter the number of your selected choice: ")
    # The question which asks if the customer type in 1 or 2
    # depending on if they want to confirm or cancel the order
    print ("Please Confirm Your Order")
    # Print statement asking customer to confirm the order

    confirm = val_int(LOW, HIGH, question)
    # sets confirm to equal validate input which sends input through the
    # function of validate input which checks if the input is an integer and
    # if it fits in the numeric boundaries set by low and high
    print()  # prints blank space
    if confirm == 1:
        # if confirm is equal to 1
        print ("Order Confirmed")
        # print statement telling customer order is confirmed
        print ("Your order will be sent to our Store.")
        # print statement telling customer order is being sent to the stor3
        print ("It will be ready soon.")
        # print statement telling customer order will be ready soon
        print()  # prints blank space
        new_exit()
        # opens and runs new exit function

    elif confirm == 2:
        # if confirm is equal to 2
        print ("Order Cancelled")
        # print statement telling customer order is cancelled
        print ("You can restart your order or exit the BOT.")
        # print statement telling customer they can restart the order
        # or exit the bot
        print()  # prints blank space
        new_exit()
        # opens and runs new exit function


# Option for new order or to exit
# takes in Low, High and question as parameters
# when sending to the validate integer input function
# no returns


def new_exit():
    question = (f"To start another order please enter {LOW}."
                f"\nTo exit the bot please enter {HIGH}."
                f"\nPlease enter the number of your selected choice: ")
    # The question which asks if the customer type in 1 or 2
    # depending on if they want to start a new order or exit the program
    confirm = val_int(LOW, HIGH, question)
    # sets confirm to equal validate input which sends input through the
    # function of validate input which checks if the input is an integer and
    # if it fits in the numeric boundaries set by low and high
    print()  # prints blank space
    if confirm == 1:
        # if confirm is equal to 1
        print ("New Order")
        # print statement telling customer that a new order will begin
        print()  # prints blank space
        order_list.clear()
        # uses clear to clean the order list
        order_cost.clear()
        # uses clear to clean the order cost
        customer_details.clear()
        # clears customer details dictionary
        main()
        # opens and runs main function

    elif confirm == 2:
        # if confirm is equal to 2
        print ("Exit")
        # print statment telling customer that the are exiting the bot
        order_list.clear()
        # uses clear to clean the order list
        order_cost.clear()
        # uses clear to clean the order cost
        customer_details.clear()
        # clears customer details dictionary
        sys.exit
        # uses sys to exit the program


# Main Function
# No Parameters
# No Returns


def main():
    '''
    Purpose: To run all functions
    A welcome message
    Parameters: None
    Returns: None
    '''
    welcome()
    # Welcome function
    del_pick = order_type()
    # Order type function
    # - runs delivery or pickup function depending on choice
    list()
    # List function
    order_laptops()
    # Order Laptops function
    print_order(del_pick)
    # Print order function
    confirm_cancel()
    # Confirm or Cancel order function
    # - runs New Order or Exit function

main()
# Main Function, runs the full program

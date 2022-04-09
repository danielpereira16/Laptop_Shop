print ("Please Confirm Your Order")
print ("To Confirm please enter 1") 
print ("To Cancel please enter 2")
while True:
    try:
        confirm = int(input("Please enter a number "))
        if confirm >= 1 and confirm <= 2:
            if confirm == 1:
                print ("Order Confirmed")
                print ("Your order will be sent to our Store")
                print ("It will be ready soon")
                break

            elif confirm == 2:
                print ("Order Cancelled")
                print ("You can restart your order or exit the BOT")
                break
        else:
            print("Number must be 1 or 2")
    except ValueError:
        print ("That was not a valid input")
        print ("Please enter 1 or 2 ")
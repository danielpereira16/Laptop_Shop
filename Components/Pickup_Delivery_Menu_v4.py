# Menu so that user can choose either pickup or delivery

# Bug - need it so that it only accepts 1 or 2

print ("Do you want your order delivered or are you picking it up")

print ("For pickup please enter 1") 
print ("For delivery please enter 2")



low = 1
high = 2

while True:
    try:
        delivery = int(input())

        if delivery == 1:
            print ("Pickup")
            break

        elif delivery == 2:
            print ("Delivery")
            break

    except ValueError:
        print ("That was not a valid input")
        print ("Please enter 1 or 2 ")
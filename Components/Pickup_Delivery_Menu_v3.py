# Menu so that user can choose either pickup or deliver

print ("Do you want your order delivered or are you picking it up")

print ("For pickup please enter 1") 
print ("For delivery please enter 2")

delivery = int(input())

if delivery == 1:
    print ("Pickup")

elif delivery == 2:
    print ("Delivery")

else:
    print ("That was not a valid input")
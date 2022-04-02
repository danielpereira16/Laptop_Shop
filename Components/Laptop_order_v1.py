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



def menu():
    number_laptops = 18

    for count in range (number_laptops):
        print("{} {} ${:.2f}"   .format(count+1,laptop_names[count],laptop_prices[count]))

menu()

# ask for total number of laptops for order
num_laptops = 0

num_laptops = int(input("How many Laptops do you want to order? "))

print(num_laptops)

# Choose laptops from the list
print("Please choose your laptops by entering the number from the menu")
for item in range(num_laptops):
    while num_laptops > 0:
        laptop_ordered = int(input())
        order_list.append(laptop_names[laptop_ordered])
        order_cost.append(laptop_prices[laptop_ordered])    
        num_laptops = num_laptops-1

print(order_list)
print(order_cost)





# Countdown until all laptops are ordered



# print order
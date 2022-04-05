#list to store ordered laptops
order_list = ['Asus 14" Laptop - Intel Celeron 4GB-RAM 128GB','Asus 15.6" Laptop - Intel Core i7 16GB-RAM 512GB-SSD',
'Asus TUF 15.6" Gaming Laptop - Intel Core i5 8GB-RAM 512GB-SSD','Apple MacBook Air 13" with M1 Chip 512GB',
'Apple MacBook Pro 13" with M1 Chip 512GB','HP 15.6" Laptop - Intel Core i5 8GB-RAM 256GB-SSD']
#list to store pizza prices
order_cost = [688, 1884, 1994, 2149, 2549, 1584]


count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
    count = count+1
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

laptop_prices = [688,1884,1994,2149,2549,1584,1994,3997,3128,1698,836,1298,2499,2549,2699,994,2388,1984]

number_laptops = 18

for count in range (number_laptops):
    print("{} {} ${:.2f}"   .format(count+1,laptop_names[count],laptop_prices[count]))
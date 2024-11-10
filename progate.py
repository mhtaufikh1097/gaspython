# ======================================IF ELSE / Kondisional
# pple_price = 2
# money = 10
# input_count = input('Mau berapa apel?: ')
# count = int(input_count)
# total_price = apple_price * count

# print('Anda akan membeli ' + str(count) + ' apel')
# print('Harga total adalah ' + str(total_price) + ' dolar')

# if money > total_price:
#     print('Anda telah membeli ' + str(count) + ' apel')
#     print('Uang Anda tinggal ' + str(money - total_price) + ' dolar')
# elif money == total_price:
#     print('Anda telah membeli ' + str(count) + ' apel')
#     print('Dompet Anda sekarang kosong')
# else:
#     print('Uang Anda tidak mencukupi')
#     print('Anda tidak dapat membeli apel sebanyak itu')
    
    
#=======================================data list,array and loop
# fruits = ['apel', 'pisang', 'jeruk']
# print(fruits)
# # Tambahkan 'anggur' ke 'fruits'
# fruits.append('anggur')

# # Cetak 'fruits'
# print(fruits)

# # Perbarui element index 0
# fruits[0] = 'ceri'

# # Cetak element index 0
# print(fruits)

# ********************************loop
# fruits = ['apel', 'jeruk', 'amer']

# for fruit in fruits:
#     print('saya suka ' + fruit)

# # Tetapkan dictionary ke variable fruits
# fruits = {'apel':'apple','jeruk':'orange'}

# # Cetak nilai dengan kunci 'jeruk'
# print(fruits['jeruk'])

# # Dengan menggunakan dictionary fruits, cetak 'Bahasa Inggris apel adalah ___'
# print('Bahasa Inggris apel adalah' + fruits['apel'])

# x = 10
# # Buat loop while yang diulang selama x lebih besar dari 0
# while x >0:
#     # Cetak variable x  
#     print(x)
#     # Kurangi 1 dari variable x 
#     x -= 1

# x = 100

# while x < 120:
#     print(x)
#     x += 1


# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# for number  in numbers:
#     if number % 3 != 0:
#         continue
#     print(number)

# # # Buat dictionary dengan kunci dan nilai, dan tetapkan ke variable items 
# items = {'apel':2,'pisang':4,'jeruk':6}
# # Buat loop for yang mengambil kunci dari items
# for item_name in items:
#     # Cetak '--------------------------------------------------'
#     print('--------------------------------------------------')
#     # Cetak 'Harga setiap ___ ___ dolar'
#     print('Harga setiap '+item_name + ' '+ '$'+ str(items[item_name]))


# items = {'apel': 2, 'pisang': 4, 'jeruk': 6}
# for item_name in items:
#     print('--------------------------------------------------')
#     print('Harga setiap ' + item_name + ' ' + str(items[item_name]) + ' dolar')
    
#     # Dapatkan nilai menggunakan input(), dan berikan ke variable input_count 
#     input_count = input('Mau berapa'+item_name+'?:')
    
#     # Cetak 'Anda akan membeli ___ ___' menggunakan input_count dan item_name
#     print('Anda akan membeli'+input_count +' '+item_name)

    
#     # Ubah input_count ke integer dan berikan ke variable count 
#     count = int(input_count)
    
#     # Kalikan harga setiap item dan variable count, dan berikan ke variable total_price 
#     total_price = items[item_name] * count
    
#     # Dengan menggunakan total_price dan type conversion, cetak 'Harga total adalah ___ dolar'
#     print('Harga total adalah'+str(total_price)+'dolar')



# is_day = False #boolean mesti tambah is
# is_night = False

# if is_day:
#     print("Selamat siang")
# elif is_night:
#     print("Selamat Malam")
# else:
#     print("selamat pagi")


# print("selamat menikmati liburan")

#============================Operator perbandingan
# grade = 5

# if grade >= 9: 
#     print("Nilai kamu A")
# elif grade >=7:
#     print("Nilai kamu B") 
# elif grade >=6:
#     print("nilai kamu C")
# else:
#     print("Maaf anda gagal")

#============================Operator Logika
# name = "Muhammad Taufik Hidayat"
# by_pass_validation = False

# if len(name) > 3 or by_pass_validation: 
#     print("welcome")
# else:
#     print("nama terlalu pendek")

#============================Perulangan While
# index = 1

# while index <= 5:
#     print("*" * index)
#     index += 1
# print("finish")

#============================Game sederhana tabek angka
# trying = 0
# secret_number = 7
# limit = 3 

# while trying < limit:
#     guess_number = input("masukan angka (1-9) : ")
#     guess_number = int(guess_number)

#     if guess_number == secret_number:
#         print("selamat, Kamu menang")
#         break

#     trying += 1

#============================Kalkulator
# (+ - * / exit)
# command = ""

# while command != "exit":
#    command = input("Perintah : ")

#    if command == "exit":
#       break

#    if command !="+" and command !="-" and command !="*" and command !="/":
#        print("Perintah tidak dikenali")
#        continue

#    a = int(input("Angka pertama : "))
#    b = int(input("Angka kedua : "))
 
#    if command == "+":
#           result = a + b
#    elif command == "-":
#           result = a - b
#    elif command == "*":
#           result = a * b
#    elif command == "/":
#        if b == 0:
#           print("Kesalahan memasukan nilai 0")   
#           continue
#        result = a / b


#    print(f"Hasil : {result}")

# print("terimakasih sudah menggunakan aplikasi kami")


#============================Pengulanan For looping 
# numbers = [1, 2, 3, 4, 5, 6]
# name = "Taufik setiawan"

# for item in range(0, 12, 2): 
#     print(item )


#============================List bisa menampung lebih dari 1 type data
# names = ["taufik", "jonan", "sikabau", "amelda" ]

# for name in names:
#     print(f"Nama : {name} ")


#============================List method
# numbers = [5, 6, 7, 8, 1]
# print(numbers)

# numbers.append(99)
# print(numbers)

# numbers.insert(2, 100)
# print(numbers)

# numbers.pop(5) #menghilangkan index
# print(numbers)

# numbers.remove(5)
# print(numbers)

# numbers.sort()
# print(numbers)

#============================Menjumlahkan list

# numbers = [5, 6, 7, 8, 1]

# init_number = 0
# for number in numbers:
#   init_number = init_number + number

# print(init_number)

#============================Mencari nilai max

# numbers = [5, 6, 7, 8, 1] //mencari dengan fungtion
# numbers.sort()
# max_number = numbers[-1]
# print(max_number)

# max_number = numbers[0] //mencari dengan manual
# for number in numbers:
#   if number > max_number:
#     max_number = number
# print(max_number)

# ============================Tuple
# numbers = [5, 3, 1, 2, 4]
# print(numbers)
# numbers[0] = 10
# print(numbers[2]) 

# ============================Unpack 
# number =  [1, 2, 3]

# # x = number[0]
# # y = number[1]
# # z = number[2]
# x, y, z = number

# print(z)

#=============================Dictionory
#user = {
 #   "name": "Muhammad Taufik Hidayat",
  #  "age" : 30,
   # "is_admin": True
#}

#name = user["username"]
#temp = user.get("username", "taufik")

#print("")
#print(temp)


#============================looping piramida kebalik
# n = 5

# for i in range(n, 0, -1):
#     #mencetak spasi
#     print(" " * (n - i), end="")
#     #mencetak bintang
#     print("*" * (2 * i - 1))
    
#===========================Looping piramida kebwh
# n = 5 

# for i in range(1, n +1):
#     print(" " *(n - i), end="")
    
#     print("*" * (2 * i - 1))

# n = 5
# for i in range(n, 0, -1):
    
#     print(" " * (n-i), end="")
#     print("*" * (2*i-1))



#===========================if else


# nilai = 100

# if nilai >= 90:
#     print("nilai kamu A" ,nilai)
# elif nilai >= 70:
#     print("nilai kamu B")
# else:
#     print("maaf anda gagal")
    

    # grade = 5

# if grade >= 9: 
#     print("Nilai kamu A")
# elif grade >=7:
#     print("Nilai kamu B") 
# elif grade >=6:
#     print("nilai kamu C")
# else:
#     print("Maaf anda gagal")

#  

# int main() {
#     int i, j, k, n;

#     // Meminta pengguna untuk memasukkan jumlah baris
#     printf("Masukkan jumlah baris: ");
#     scanf("%d", &n);

#     // Loop untuk setiap baris
#     for (i = 1; i <= n; i++) {
#         // Loop untuk spasi di awal setiap baris
#         for (j = i; j < n; j++) {
#             printf(" ");
#         }
#         // Loop untuk mencetak bintang
#         for (k = 1; k <= (2 * i - 1); k++) {
#             printf("*");
#         }
#         printf("\n"); // Pindah ke baris berikutnya setelah selesai
#     }

#     return 0;
# }
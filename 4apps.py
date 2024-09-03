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


#============================Pengulanan For
numbers = [1, 2, 3, 4, 5]
name = "Taufik setiawan"

for item in numbers:
    print(item)
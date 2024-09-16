                        #MENERIMA INPUT dari user@@@@@@@@
# name = input("siapa nama kamu? ")
# age = input("berapa umur? ")
# hobby = input("Apa Hobimu? ")
# # sentence = name + " Selamat datang di jawa"
# print("namaku adalah ",name  + " usiaku " ,age + "Tahun " + " hobiku adalah " ,hobby)
print("================Penghasilan Pengemis stopan lampu merah===============")
def jam_ke_menit(jam):
    try:
        jam = float(jam)
        menit = jam * 60
        return menit
    except ValueError:
        return "Input tidak valid. Masukan nilai numerik."

a = int(input("jumlah orang dalam 1 menit =  "))
nilai = int(input("berapa rupiah dari 1 orang = "))
input_jam = int(input("berapa jam anda bekerja dalam 1 hari ?"))

hasil_menit = jam_ke_menit(input_jam)
hasil =  float(a * nilai * hasil_menit)
print("penghasilanku adalah", hasil)





                    #TYPE DATA CONVERSION@@@@@@@@
# year = input("Tahun lahir : ")
# print(type(year))

# year = int(year)
# print(type(year))

# age = 2024 - year

# print("umur kamu : " + str(age))

                    #String @@@@@@@@
# name  = "Taufik Hidayat"
# print(name[-5]) # "-" artinya adalah perhitungan array dari belakang
# print(name[0:6]) #":" artinya untuk memanggil beberapa karakter


                    #Formatted String @@@@@@@@
# first_name = "Muhammad"
# last_name = "Taufik"
# age = 31

# # message = "Muhammad [Taufik]"
# message = f"{first_name} [{last_name}]" #f adalah formated
# message1 = "umur kamu adalah {age}"

# print(message)
# print(age)

#                 #String Method @@@@@@@@
# course = "belajar python"
# length = len(course)
# course.upper 

# print(length)
# print(course.title())
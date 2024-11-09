#variable adalah tempat menyimpan data

#menaru / assignment nilai

# a = 10 
# x = 5 

# panjang = 1000

# print("nilai a = ", a)
# print("nilai x = ", x)
# print("nilai panjang = ", panjang)


#penamaan





#input user

# data = input("Masukan data: ")

# print("data =" , data,", type =",type(data))
 
# #jika kita ingin mengabil int, maka 
# angka  = float(input("masukan angka: "))
# angka  = int(input("masukan angka: "))
# print("data = ", angka,",type =",type(angka))
 
# biner = bool(int(input("masukan nilai bolean: ")))

# print("data = ",biner,",type =", type(biner))



# ==========================latihan komparasi logika==================
#membuat gabungan area rentang dari sebuah angka

#++++++3-------------10++++++++

inputUser = float(input("masukan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10\t:"))

#+++++++++3------------------------------
#Memeriksa angka kurang dari 3 
isKurangDari = (inputUser < 3)
print("kurang dari 3 = ", isKurangDari)

#----------10+++++++++++++++++
# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 = ", isLebihDari)

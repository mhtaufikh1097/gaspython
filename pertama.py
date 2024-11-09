import random

welcome_message = "Welcome To Cuypy Games"
poikpy_position = random.randint(1, 4)



print("****************************")
print(f"** {welcome_message}**")
print("****************************")



nama_user = input("masukan nama anda: ")

print(f'''
Halo {nama_user}! Coba perhatikan goa dibawah ini
|(1)| |(2)| |(3)| |(4)|
''')

pilihan_user = int(input("Menurut kamu di goa no brp POIK berada? [1 / 2 / 3 / 4]: "))


if pilihan_user == poikpy_position:
    print(f"Selamat {nama_user} kamu menang! posisi poikpy ada di {poikpy_position} dan pilihanmu adalah goa nomor {pilihan_user}.")
else:
    print(f"kamu kalah poikpy bukan berada disitu,tapi ada di goa nomor {poikpy_position}. Sedangkan kamu memilih goa nomor {pilihan_user}")


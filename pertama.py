welcome_message = "Welcome To Cuypy Games"

poikpy_position = 2
print("****************************")
print(f"** {welcome_message}**")
print("****************************")



nama_user = input("masukan nama anda: ")

print(f'''
Halo {nama_user}! Coba perhatikan goa dibawah ini
|(1)| |(2)| |(3)| |(4)|
''')

pilihan_user = int(input("Menurut kamu di goa no brp POIK berada? [1 / 2 / 3 / 4]: "))



print(f"pilihan kamu adalah {pilihan_user}")

if pilihan_user == poikpy_position:
    print("Selamat kamu menang Wow!")
else:
    print("kamu kalah poikpy bukan berada disitu")


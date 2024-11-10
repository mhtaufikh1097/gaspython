#================================================Function
# def print_hand(hand,name):
#     print(name+' ' 'memilih ' + hand)
    
# print_hand('batu','poik')
# print_hand('gunting','refani')

# def soba(hand,name='komputer'):
#     print(name+' ' 'Memilih ' + hand)
    
# player_name = input('Masukan nama anda:')
    
# soba('batu',player_name)    

# def print_hand(hand, name='Tamu'):
#     # Tetapkan list hands ke variable hands 
#     hands = ['Batu','Kertas','Gunting']
    
#     # Memperbarui dengan menggunakan element dari variable hands 
#     print(name + ' memilih: ' + hands[hand])

# print('Memulai Permainan Batu Kertas Gunting!')
# #masukan input dalam variable player_name
# player_name = input('Masukan nama anda')
# # Cetak 'Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)'
# print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')

# # Dapatkan input, ubah, dan tetapkan ke variable player_hand 
# player_hand = int(input('Masukkan nomor (0-2): '))

# # Ubah argument pertama ke player_hand
# print_hand(player_hand, player_name)



# ===================game tanpa random komp
# def validate(hand):
#     if hand < 0 or hand > 2:
#         return False
#     return True

# def print_hand(hand, name='Tamu'):
#     hands = ['Batu', 'Kertas', 'Gunting']
#     print(name + ' memilih: ' + hands[hand])

# print('Memulai permainan Batu Kertas Gunting!')
# player_name = input('Masukkan nama Anda: ')

# print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')
# player_hand = int(input('Masukkan nomor (0-2): '))

# if validate(player_hand):
#     # Tetapkan 1 ke variable computer_hand 
#     computer_hand = 1
    
#     print_hand(player_hand, player_name)
#     # Panggil function print_hand dengan computer_hand dan 'Komputer' sebagai argument
#     print_hand(computer_hand, 'Komputer')
    
# else:
#     print('Mohon masukkan nomor yang benar')





# ==========================MEMBUAT FUNCTION MODULE
# Pindahkan ke 3 function dibawah ke utils.py
# import module utilskikie
# import utils

# print('Memulai permainan Batu Kertas Gunting!')
# player_name = input('Masukkan nama Anda: ')

# print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')
# player_hand = int(input('Masukkan nomor (0-2): '))

# # Panggil function validate milik module utils

# if utils.validate(player_hand):
#     computer_hand = 1
    
#     # Panggil function print_hand milik module utils
#     utils.print_hand(player_hand, player_name)
#     utils.print_hand(computer_hand, 'Komputer')
    
#     # Panggil function judge milik module utils
   
#     result = utils.judge(player_hand, computer_hand)
#     print('Hasil: ' + result)
# else:
#     print('Mohon masukkan nomor yang benar')






# ============================Menggunakan function randint
import utils
import random
# import module random


print('Memulai permainan Batu Kertas Gunting!')
player_name = input('Masukkan nama Anda: ')

print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')
player_hand = int(input('Masukkan nomor (0-2): '))

if utils.validate(player_hand):
    # Tetapkan nomor acak antara 0 dan 2 ke computer_hand menggunakan randint
    computer_hand = random.randint(0,2)
    
    utils.print_hand(player_hand, player_name)
    utils.print_hand(computer_hand, 'Komputer')

    result = utils.judge(player_hand, computer_hand)
    print('Hasil: ' + result)
else:
    print('Mohon masukkan nomor yang benar')

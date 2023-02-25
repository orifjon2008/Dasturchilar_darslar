# 1 - vazifa
# Bir so'z kiritadi.
# Shu so'zning ichida nechta harf
# borligi va nechta raqam borligini chiqorsin


# harflar = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
harflarning_soni = 0
sonlar = '1234567890'
sonlarning_soni = 0
spacening_soni = 0
suz = 'Bir nimadur so\'z. 123456. впқва يسلسي'

for i in suz:
    if i.isalpha():
        harflarning_soni += 1
    if i.isnumeric():
        sonlarning_soni += 1
    if i.isspace():
        spacening_soni += 1

# print(harflarning_soni, 'ta harf bor')
# print(sonlarning_soni, 'ta son bor')
# print(spacening_soni, 'ta space bor')

# 2 - vazifa
# foydalanuvchi bir son kiritadi
# kiritilgan sonning karakarasini chiqorib bering
# masalan:
# 7
# 7 * 0 = 0
# 7 * 1 = 7
# 7 * 2 = 14

# son = 6
# for i in range(0, 12 + 1):
#     print(son, '*', i, '=', son * i)

# 3 - vazifa
# 5
# *****
# *****
# *****
# *****
# *****

# son = 6
# belgi = '*'
# for i in range(0, son):
#     print(belgi * son)


# 4 - vazifa
# Sonning faktorialini toping
# n! = 1 * 2 * 3 * 4 * 5 ...... * n
# 5! = 120 = 1 * 2 * 3 * 4 * 5
#
# son = 6
# factarial = 1
# # 2 * 1 = 2,
# for i in range(2, son + 1):
#     factarial *= i
# print(factarial)
#
# import math
# print(math.factorial(son))
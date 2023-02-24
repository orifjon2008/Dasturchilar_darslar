# --------------------------------------------------
# -------------------- For loop --------------------
# --------------------------------------------------



# --------------------------------------------------
# syntax:
# for item in iterable_object :
#     do something with Item (block of code)
# --------------------------------------------------
# 1) yuqorida yozilgan koddagi item bu variable
#    uni loop ichida istalgan vaqtda ishlata olasiz
# 2) item variable bu holatda hozir loop ishora qilib
#    turgan narsaga dalolat qiladi xolos. Loop ikkinchi
#    aynalganida bu item dagi variable ning qiymati o'zgaradi
# 3) itetable_object ==> bu iterable bo'lgan istalgan abyectdir
# --------------------------------------------------

myString = 'SomeString'
#
# for var in 'SomeString': # S
#     print(var)

myString = 'SomeString'
number = 0 # 1 2

# for word in myString:
#     number = number + 1
#     if word == 'g':
#         print('The string has the \'g\' word.')
# print(number)



# range() haqida
# range(0, 10) 0 dan 10 gacha iterable
# object qayratadi
#
# print(type(range(0, 10)))
#




# Bir dastur yarating
# Dastur agar kiritlgan string ichida 'B', yoki 'b harfi bo'lsa
# True deb chiqorsin
# agar unaqa bo'lmasa False deb chiqorsin
#  Diqqat! in ni ishlatmang

# var = 'Abc'
#
# for word in var:
#     if word == 'B' or word == 'b':
#         print(True)
#     else:
#         print(False)

# *
# **
# ***
# ****
# *****
# ******
#
belgi = '*'
son = int(input('Son kiriting.. '))
for i in range(0, son):
    print(belgi)
    belgi = belgi + '*'

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# var = 1
# for i in range(0, 5):
#     print(var, end='')
#     var = var + 1
#     print()


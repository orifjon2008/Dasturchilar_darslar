# --------------------------------------------------
# ------------------- Operators --------------------
# --------------------------------------------------

# Operators:
# - Comparison
# - Logical
# - Arithmatic

# Comparison:

# print(4 == 4)
# print(4 > 5)
# print(4 < 5)
# print(4 >= 5)
# print(4 <= 5)
# print(5 is 5)


# son = int(input('Bir son kiriting: '))
#
# # if (son >= 1 and son <= 2) or son == 12: # 1, 2, 12
# #     print('qish')
#
# if son == 1 or son == 2 or son == 12:
#     print('Qish')
# elif son >= 3 and son <= 5: # 3, 4, 5
#     print('bahor')
# elif son >= 6 and son <= 8: # 6, 7, 8
#     print('yoz')
# elif son >= 9 and son <= 11: # 9, 10, 11
#     print('kuz')
# else:
#     print('siz notogri son kiritdingiz')


print(2 * 2 < 5)

print(2 ** 2 * 2 > 7 and 8 > 10)

# Floating point ==> float, float()

narx = 1900

kurs = 18.80
bank = 100

if narx <= bank * kurs:
    print('Puliz yetadi')
else:
    print('Puliz yetmaydi')


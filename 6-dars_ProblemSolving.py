# user_1
# user_2

# user_1 ==> harf ABCDEFGH
# user_1 ==> son 12345678
# user_2 ==> harf ABCDEFGH
# user_2 ==> son 12345678

# # in
# string = 'abcd'
# print('A' in string)

# user_1_harf = input('Foydalanuvchi 1. Harfni kiriting...') # str
# shaxmat_doskasi_harflari = 'ABCDEFGH'
#
# if user_1_harf in shaxmat_doskasi_harflari:
#     print(True)
# else:
#     print(False)


user_1_word = input('1 - chi Foydalanuvchi Harfni kiriting: ')
user_1_number = int(input('1 - chi Foydalanuvchi Sonni kiriting: '))

shaxmat_harflari = 'ABCDEFGH'

user_2_word = input('2 - chi Foydalanuvchi Harfni kiriting: ')
user_2_number = int(input('2 - chi Foydalanuvchi Sonni kriiting: '))


if user_1_word not in shaxmat_harflari and user_2_word not in shaxmat_harflari:
    print('To`g`ri harf kiriting...')
else:
    if not user_1_number >= 1 and not user_1_number <= 8 and not user_2_number >= 1 and not user_2_number <= 8:
        print('To`g`ri son kiriting...')
    else:
        if user_1_word == user_2_word and user_1_number == user_2_number:
            print(True)
        else:
            print(False)
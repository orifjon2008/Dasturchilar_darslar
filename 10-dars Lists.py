# products = ['Olma', 'Banan', 'Ananas', 8]
# # List is ==> Iterable object
# # List is ==> Mutable object
# # products[1] = 'Anor'
# # print(products)
# # print(products[0][0])
# # print(products[3])
#
#
# # append() ==> listni oxiriga item tiqadi
# products = ['Olma', 'Banan', 'Ananas', 8]
# products.append('Tarvuz')
# print(products)
#
# # clear() ==> listni tozalaydi
# products = ['Olma', 'Banan', 'Ananas', 8]
# products.clear()
# print(products)
#
# # pop(), remove(), del ==> listni ichidagi itemni o'chiradi
# products = ['Olma', 'Banan', 'Ananas', 8]
# products.pop(3) # ==> listni itemini index
# print(products)
#
# products = ['Olma', 'Banan', 'Ananas', 8]
# products.remove('Banan') # itemni o'zini yozsak ochiradi
# print(products)
#
# products = ['Olma', 'Banan', 'Ananas', 8]
# del products[0]
# print(products)
#
# # split() ==> string ni itemlarini alohida qilib listga soladi
# # join() ==> listni stringga aynaltiradi
#
# string = input('Jumla kiriting... ')
# yomon_sozlar = ['Abilax', 'Muttaham']
#
# for soz in yomon_sozlar:
#     if soz in string:
#         string = string.replace(soz, '%*%&^')
# print("Siz kiritgan so'zingiz ==> ", string)

# l = [1, 25, 8, 50, 40]
# jami = 0
# for i in l:
#     jami = jami + i
# print(jami)

l = [1, 25, 8, 50, 40]
jami = 1
for i in l:
    jami = jami * i
print(jami)
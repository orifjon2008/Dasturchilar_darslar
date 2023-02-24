# # --------------------------------------------------
# # --------------------- String ---------------------
# # --------------------------------------------------
# #
# # print('-' * 50)
# # print(' String '.center(50, '-'))
# # print('-' * 50)
# #
# # # 'String', "String", '''String''', """String"""
# #
# # # myString = 'String One'
# # # print(myString)
# # # myString = "String Two"
# # # print(myString)
# # # myString = '''String Three'''
# # # print(myString)
# # # myString = """String Four"""
# # # print(myString)
# #
# # myString = '''String
# # Five
# # new
# # line
# # '''
# # print(myString)
# #
# # myString = """
# # String o' g' hariflarida muommo yo'q
# # """
# # print(myString)
# #
# # myString = '' # ' ni ishlatish
# #
# # myString = " sdgsdg sdfasdf"
# #
#
#
#
# print('-' * 50)
# print(' Escape Sequances characters '.center(50, '-'))
# print('-' * 50)
#
#  #
# #
# #
# #
# # Escape Sequances characters
#
# # \b ==> Back Space
# print('Salom \bJanob')
# print('Salom Janob\b')
#
# # \\ ==> Escape \ its self
# print('Salom \\ Janob')
#
# # \' ==> Escape single quote
# print('G\'ani g\'ildirakni g\'azillatib g\'ildiratdi')
#
# #  \" ==> Escape Double quote
# print("   Men zo\'r \"Inson man\"   ")
#
# # \n ==> New Line
# print('Salom\nJanob')
#
# # \t ==> Horizontal Tap
# print("Salom\tJanob")
#
# #
# #
#
print('-' * 50)
print(' String - indexing & Slicing '.center(50, '-'))
print('-' * 50)
#
#
#
# String - indexing & Slicing
# 1) All data in python is object
# 2) Object Contain Elements
# 3) Every Element Has Own Index
# 4) Python Use Zero Based Indexing
# 5) Use [] to Access Element

# Indexing
myString = 'JanobDasturchi'
# print(myString)
# print(myString[5])
# print(myString[0])
# print(myString[-1])

myString = 'JanobDasturchi'
# Slicing Multiple
# [start:end] # end ni hisobga olmaymiz
# print(myString[0:3])
# print(myString[4:6])
#
# print(myString[:4])
print(myString[4:])
print(myString[0:0])
print(myString[0:0:0])
print(myString[0:0])
print(myString)
#
# # [start:end:steps]
# print(myString[1:6:1])
# print(myString[2:8:2])
# print(myString[::2])
# print(myString[::-1])
#
# myReversedString = myString[::-1]
# print(myReversedString)
#
# # Teskarisini chiqoruvchi dastur.
# soz = input('Bir so\'z kiriting...')
# print(soz[::-1])
# #
# #
# #
# print('-' * 50)
# print(' len() '.center(50, '-'))
# print('-' * 50)
# #
# #
# #
#
# # len() - uzunlikni aytadi, faqat u 1 dan boshlaydi
# #  0 dan mas
#
# print(len(myString))
#
# # birinchi va oxirgi harfni topuvchi dastur
#
# string = input('Biror bir so\'z kiriting... ')
#
# index_of_last_item = len(string) - 1
#
# print('Birinchi harfi:', string[0], 'ekan. Ikkinchi harf esa:', string[index_of_last_item], 'ekan.')
#

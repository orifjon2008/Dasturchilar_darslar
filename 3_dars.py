son_1 = int(input('Birinchi sonni kiriting: '))

son_2 = int(input('Ikkinchi sonni kiriting: '))

belgi = input('Belgi kiriting: ')

if belgi == 'x':
    natija = str(son_1) + ' x ' + str(son_2) + ' = ' + str(son_1 * son_2)

elif belgi == ':':
    natija = str(son_1) + ' : ' + str(son_2) + ' = ' + str(son_1 / son_2)

elif belgi == '+':
    natija = str(son_1) + ' + ' + str(son_2) + ' = ' + str(son_1 + son_2)

elif belgi == '-':
    natija = str(son_1) + ' - ' + str(son_2) + ' = ' + str(son_1 - son_2)

else:
    natija = ''
print(natija)




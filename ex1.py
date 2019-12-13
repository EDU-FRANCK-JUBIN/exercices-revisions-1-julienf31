size = input('Hauteur du sapin :')

space = ' '

for i in range(0,int(size)):
    print((int(size)-i) * space + '^' * ((2*i)+1))
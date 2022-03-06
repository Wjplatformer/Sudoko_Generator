from random import randint as rd
from generator import generate as gd

def make_table(table):#column view
    c=0
    for i in range(9):
        print(table[c+1:c+9:])
        if c==0:
            c+=8
        else:
            c+=9
        
    print(table)
    pass

while True:
    print('Press enter')
    a=input()
    print('Generation in Proccess...')
    if a=='Q':
        break
    make_table(gd())
    

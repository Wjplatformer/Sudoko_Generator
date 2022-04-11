from random import randint as rd
from generator import generate as gd

def make_table(table): #(row view, fixed :D)
    c=0
    for i in range(9):
        print(table[c:c+72:9])
        c+=1
    print('='*20)
    print(table)
    pass

while True:
    print('Press enter')
    a=input()
    print('Generation in Proccess...')
    if a=='Q':
        break
    make_table(gd())
    

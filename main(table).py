from random import randint as rd
from generator import generate as gd

def make_table(table): #(row view, fixed :D)
    for c, _ in enumerate(range(9)):
        print(table[c:c+72:9])
    print('='*20)
    print(table)

while True:
    print('Press enter')
    a=input()
    print('Generation in Proccess...')
    if a=='Q':
        break
    make_table(gd())
    

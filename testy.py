import random
import time

lista={
    'lista50':[],
    'lista10':[]
}

zmiany=[]

for i in range(50):
    lista['lista50'].append(i+1)
for i in range(10):
    lista['lista10'].append(i+1)

print("lista50 wyglada tak {}".format(lista['lista50']))
print("lista10 wyglada tak {}".format(lista['lista10']))

def wczytujemy():
    dowyciecia = []
    wpisane = input('wpisz wynik losowania: ')
    dowycieciastr = wpisane.split(',')
    for i in range(len(dowycieciastr)):
        dowyciecia.append(int(dowycieciastr[i]))
    return dowyciecia

def wycinamy(lista,dowyciecia):
    for i in range(len(dowyciecia)):
        for n in range(len(lista)):
            if dowyciecia[i] == lista[n]:
                lista.pop(n)
                break
    return lista

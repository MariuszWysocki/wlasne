import random
import time

lista=[]
zmiany=[]

liczbazakladow=input('wpisz liczbe zakladow ')
liczbazakladow = int(liczbazakladow)


for i in range(49):
    lista.append(i+1)

print('podstawowa lista {}'.format(lista))
print(len(lista))
print('obcinam skrajne wartosci i wartosci 1-10')

lista=lista[11:-1]
print('podstawowa lista {}'.format(lista))

def wczytujemy():
    dowyciecia = []
    wpisane = input('wpisz wynik poprzedniego losowania: ')
    dowycieciastr = wpisane.split(',')
    for i in range(len(dowycieciastr)):
        dowyciecia.append(int(dowycieciastr[i]))
    return dowyciecia

dowyciecia= wczytujemy()
print('do wyciecia')
print (dowyciecia)

def wycinamy(lista,dowyciecia):
    for i in range(len(dowyciecia)):
        for n in range(len(lista)):
            if dowyciecia[i] == lista[n]:
                lista.pop(n)
                break
    return lista

lista = wycinamy(lista, dowyciecia)
print(lista)

print ('usuwamy wyniki z przed ostatniego losowania')
dowyciecia= wczytujemy()
print ('do wyciecia {}'.format(dowyciecia))
lista = wycinamy(lista, dowyciecia)
print('podstawowa lista {}'.format(lista))

# print ('usuwamy wyniki z przed przed ostatniego losowania')
# dowyciecia= wczytujemy()
# print ('do wyciecia {}'.format(dowyciecia))
# lista = wycinamy(lista, dowyciecia)
# print('podstawowa lista {}'.format(lista))

print('teraz losujemy 6 liczb z {}'.format(len(lista)))

for i in range(liczbazakladow):
    losuje  = random.sample(range(0,len(lista)), 6)
#    print('teraz z listy wycinamy indexy {}'.format(losuje))
#   print('z lista podstawowa {}'.format(lista))
    obstawiamy=[]
    for i in losuje:
        obstawiamy.append(lista[i])
    print('trzeba obstawic {}'.format(obstawiamy))
    time.sleep(2)
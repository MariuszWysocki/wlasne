import random
import time

lista=[]
zmiany=[]

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

liczbazakladow=input('wpisz liczbe zakladow ')
liczbazakladow = int(liczbazakladow)
for i in range(50):
    lista.append(i+1)

print('podstawowa lista {}'.format(lista))
print(len(lista))
print('obcinam skrajne wartości')

lista=lista[1:-1]
print('podstawowa lista {}'.format(lista))



print ('usuwamy wyniki z ostatniego losowania')
dowyciecia= wczytujemy()
print ('do wyciecia {}'.format(dowyciecia))
lista = wycinamy(lista, dowyciecia)
print('podstawowa lista {}'.format(lista))

print ('usuwamy wyniki z przed ostatniego losowania')
dowyciecia= wczytujemy()
print ('do wyciecia {}'.format(dowyciecia))
lista = wycinamy(lista, dowyciecia)
print('podstawowa lista {}'.format(lista))


print ('usuwamy wyniki z przed przed ostatniego losowania')
dowyciecia= wczytujemy()
print ('do wyciecia {}'.format(dowyciecia))
lista = wycinamy(lista, dowyciecia)
print('podstawowa lista {}'.format(lista))



print('teraz losujemy 5 liczb z {}'.format(len(lista)))

for i in range(liczbazakladow):
    losuje  = random.sample(range(0,len(lista)), 5)
#    print('teraz z listy wycinamy indexy {}'.format(losuje))
#   print('z lista podstawowa {}'.format(lista))
    obstawiamy=[]
    for i in losuje:
        obstawiamy.append(lista[i])
    print('trzeba obstawic {}'.format(obstawiamy))
    time.sleep(2)
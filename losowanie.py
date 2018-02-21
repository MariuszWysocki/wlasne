import random
import time

lista=[]
zmiany=[]
opcja = 0

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
##tworzymy liste podstawowa
for i in range(49):
    lista.append(i+1)
print('podstawowa lista {}'.format(lista))
print(len(lista))
## wybieramy opcje losowania
while (opcja != 1):
    a = input('wybierz /a/ dla liczb 1-49 lub /b/ dla losowania 11 - 49')
    if (a=='a'):
        print('wybrales /a/ obcinam skrajne wartosci 1 i 49')
        lista = lista[1:-1]
        print('podstawowa lista {}'.format(lista))

        dowyciecia = wczytujemy()
        print('do wyciecia {}'.format(dowyciecia))
        lista = wycinamy(lista, dowyciecia)
        print('podstawowa lista {}'.format(lista))

        print('usuwamy wyniki z przed ostatniego losowania')
        dowyciecia = wczytujemy()
        print('do wyciecia {}'.format(dowyciecia))
        lista = wycinamy(lista, dowyciecia)
        print('podstawowa lista {}'.format(lista))

        print ('usuwamy wyniki z przed przed ostatniego losowania')
        dowyciecia= wczytujemy()
        print ('do wyciecia {}'.format(dowyciecia))
        lista = wycinamy(lista, dowyciecia)
        print('podstawowa lista {}'.format(lista))

        break
        opcja = 1

    if (a=='b'):
        print('wybrales /b/ obcinam skrajne wartosci i wartosci 1-11')
        lista = lista[10:-1]
        print('podstawowa lista {}'.format(lista))

        dowyciecia = wczytujemy()
        print('do wyciecia {}'.format(dowyciecia))
        lista = wycinamy(lista, dowyciecia)
        print('podstawowa lista {}'.format(lista))

        print('usuwamy wyniki z przed ostatniego losowania')
        dowyciecia = wczytujemy()
        print('do wyciecia {}'.format(dowyciecia))
        lista = wycinamy(lista, dowyciecia)
        print('podstawowa lista {}'.format(lista))

        # print ('usuwamy wyniki z przed przed ostatniego losowania')
        # dowyciecia= wczytujemy()
        # print ('do wyciecia {}'.format(dowyciecia))
        # lista = wycinamy(lista, dowyciecia)
        # print('podstawowa lista {}'.format(lista))

        break
        opcja = 1

print('teraz losujemy 6 liczb z {}'.format(len(lista)))

rnd  = random.SystemRandom()

for i in range(liczbazakladow):
    losuje  = rnd.sample(range(0,len(lista)), 6)
#    print('teraz z listy wycinamy indexy {}'.format(losuje))
#   print('z lista podstawowa {}'.format(lista))
    obstawiamy=[]
    for i in losuje:
        obstawiamy.append(lista[i])
    print('trzeba obstawic {}'.format(obstawiamy))
    time.sleep(2)
import random
import time

def naIntListe(wpisane):
    wpisane = wpisane.split(',')
    zwrot = []
    for i in range(len(wpisane)):
        zwrot.append(int(wpisane[i]))
    return zwrot

def wczytujemy():
    dopociecia = input('wprowadz wynik losowania w formacie 1,2,3,4,5+6,7 ')
    pociete = dopociecia.split('+')
    print('tak wygla pociete wtępnie na dwie listy {}'.format(pociete))

    dopociecia50 = pociete[0];
    dopociecia50 = naIntListe(dopociecia50)

    print('tak wyglada dopociecia50 {}'.format(dopociecia50))

    dopociecia10 = pociete[1];
    dopociecia10 = naIntListe(dopociecia10)
    print('tak wyglada do pociecia10 {}'.format(dopociecia10))

    lista['lista50'] = wycinamy(lista['lista50'], dopociecia50)
    print('po wycieciu lista50 wyglada tak {}'.format(lista['lista50']))

    lista['lista10'] = wycinamy(lista['lista10'],dopociecia10)
    print('po wycieciu lista10 wyglada tak {}'.format(lista['lista10']))



def wycinamy(lista,dowyciecia):
    for i in range(len(dowyciecia)):
        for n in range(len(lista)):
            if dowyciecia[i] == lista[n]:
                lista.pop(n)
                break
    return lista

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
lista['lista50'].remove(1)
lista['lista50'].remove(50)
print("lista50 po usunieciu skrajnych wartosci {}".format(lista['lista50']))
print("lista10 wyglada tak {}".format(lista['lista10']))

wczytujemy()
wczytujemy()
wczytujemy()













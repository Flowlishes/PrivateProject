#!/usr/bin/env python
# coding: utf8

'''
    File name: 1-Main.py
    Date created: 19/11/2017
    Date last modified: 19/11/2017
    Python version: 3.5
'''


import ZimmerbelegunModul

#Liste aller Personen
personenliste = []
#Liste aller Zimmer, Zimmer in Sublisten
zimmerliste = []
#Sublisten der Personen mit ihren Favoriten
like_list = []
#Sublisten der Personen mit ihren No-Go's
hate_list = []
#Anzahl aller eingelesenen Personen
max_personen = 0



def datei_einlesen():
    #Testdateien werden in Listen geladen
    file = open("1-beispiel-4.txt")
    while True:
        #Datei wird Zeile für Zeile eingelesen
        name = file.readline().strip()
        #Zwischenfunktion zum Entfernen der Leerzeichen und +/-
        likes = split_namen(file.readline().strip())
        hates = split_namen(file.readline().strip())

        if not file.readline():
            print(file.readline())
            break
        #HInzufügen der Namen in passende Liste
        eingabe_liste(name, likes, hates)
    file.close()


def eingabe_liste(name, likes, hates):
    #Hinzufügen der eingelesenen Zeilen in passende Liste

    global max_personen

    like_list.append(likes)
    hate_list.append(hates)
    personenliste.append(name)

    max_personen += 1

def split_namen(text):
    #Entfernen der Sonderzeichen am Anfang der Zeile, Leerzeichen
    #und Konvertierung zu einer Liste
    namen = text.split(' ')
    del namen[0]
    #--> Liste wird ausgegeben
    return namen



datei_einlesen()
#print(personenliste)
#print(like_list)
#print(hate_list)

i = 0
plus = True
zimmer = []

#Iteration durch eine sich verändernde Liste (keine for-Schleife möglich --> out of range)
while plus == True:
    #Aktuelle Person hat jemanden in ihrer like_list
    if len(like_list[i]) != 0:
        zimmer.append(personenliste[i])

        del hate_list[i]
        del personenliste[i]
        del like_list[i]

        #print(zimmer)
        #print(personenliste)

        #Sonderfall: falls Ende der Liste, aber Person hat jemanden in ihrer +Liste
        #wird diese entfernt und das Objekt aus der Liste gelöscht, der Iterationsindex ist somit
        #größer als die Anzahl der Listenobjekte-1 und der Zeiger befindet sich außerhalb der Liste
        #folgende if-Abfrage unterbindet einen "out of range"-Fehler
        if i > (len(personenliste)-1):
            plus = False

    #Person hat niemanden in ihrer like_list und das Ende der Personenlite ist erreicht
    elif (len(like_list[i]) == 0) and (i == (len(personenliste)-1)):
        plus = False
    #Keine Personen in like_list und noch kein Ende der Liste --> Erhöhung der
    #Iterationsvariablen um 1
    else:
        i += 1

print(zimmer)
print(personenliste)
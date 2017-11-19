#!/usr/bin/env python
# coding: utf8

'''
    File name: 1-Main.py
    Date created: 19/11/2017
    Date last modified: 19/11/2017
    Python version: 3.5
'''


import ZimmerbelegungModul

#Liste aller Personen
personenliste = []

#Liste aller Zimmer, Zimmer in Sublisten
zimmerliste = []

#Liste aller Negativlisten aller Zimmer
zimmernegativliste = []

#Sublisten der Personen mit ihren Favoriten
like_list = []

#Sublisten der Personen mit ihren No-Go's
hate_list = []

#Anzahl aller eingelesenen Personen
max_personen = 0



def datei_einlesen():
    #Testdateien werden in Listen geladen
    file = open("1-beispiel-1.txt")
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

#----------------------------

def zimmer_negativliste(zimmernegativ, hate_list, index):
    #Iteration durch bereits bestehende Liste, um Doppelnennungen zu vermeiden
    for k in hate_list[index]:
        if k not in zimmernegativ:
            zimmernegativ.append(k)
    return(zimmernegativ)

def person_zimmer(name, personenliste, like_list, hate_list, zimmer, zimmernegativ):
    index = personenliste.index(name)
    #Aktuelle Person wird in das Zimmer eingefügt und aus der Personenliste entfernt
    zimmer.append(personenliste[index])
    del personenliste[index]

    #gemeinsame Negativliste erstellen und aus hate_list entfernen
    zimmernegativ = zimmer_negativliste(zimmernegativ, hate_list, index)
    del hate_list[index]

    #zwischenspeichern der +Liste
    aktuellelike_list = like_list[index]
    del like_list[index]

    #Falls Leute in Wunschliste
    if len(aktuellelike_list) != 0:
        #Druchgehen der Wünsche
        for a in aktuellelike_list:
            name = a
            person_zimmer(name, personenliste, like_list, hate_list, zimmer, zimmernegativ)


datei_einlesen()
print(personenliste)

# i = 0
# plus = True
#
# #Iteration durch eine sich verändernde Liste (keine for-Schleife möglich --> out of range)
# while plus == True:
#     #Aktuelle Person hat jemanden in ihrer like_list
#     if len(like_list[i]) != 0:
#         zimmer = []
#         zimmernegativ = []
#         name = personenliste[i]
#
#         person_zimmer(name, personenliste, like_list, hate_list, zimmer, zimmernegativ)
#
#         #print(zimmer)
#         #print(personenliste)
#         zimmerliste.append(zimmer)
#         zimmernegativliste.append(zimmernegativ)
#
#         #Sonderfall: falls Ende der Liste, aber Person hat jemanden in ihrer +Liste
#         #wird diese entfernt und das Objekt aus der Liste gelöscht, der Iterationsindex ist somit
#         #größer als die Anzahl der Listenobjekte-1 und der Zeiger befindet sich außerhalb der Liste
#         #folgende if-Abfrage unterbindet einen "out of range"-Fehler
#         if i > (len(personenliste)-1):
#             plus = False
#         i = 0
#         #print(personenliste)
#
#     #Person hat niemanden in ihrer like_list und das Ende der Personenlite ist erreicht
#     elif (len(like_list[i]) == 0) and (i == (len(personenliste)-1)):
#         plus = False
#     #Keine Personen in like_list und noch kein Ende der Liste --> Erhöhung der
#     #Iterationsvariablen um 1
#     else:
#         i += 1

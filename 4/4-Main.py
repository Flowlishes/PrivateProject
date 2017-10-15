"""!/usr/bin/python
-*- coding: UTF-8 -*-
"""

'''
    File name: AutoScrabbleMain.py
    Date created: 20/09/2017
    Date last modified: 26/09/2017
    Python version: 3.5
'''


#Modulimport
import AutoScrabbleModul

#Einlesen der Datei mit allen Kürzeln
kuerzel = [line.rstrip('\n') for line in open('4-Kuerzelliste.txt')]

#Eingabe der Wörter
wort = str(input("Worteingabe: "))

lösen = True

#Zuerst Überprüfung auf Ä, da nicht möglich
for c in wort:
    if c == "Ä":
        print("Der Text kann nicht mit mehreren Kennzeichen geschrieben werden, da er ein Ä enthält.")
        lösen = False

#kennzeichenliste = []

if lösen == True:
    #Ansatz1, erstes Kürzel hat einen Buchstaben
    wortrest = wort
    kennzeichenliste = []
    print("\n\nDarstellung mit einem Buchstaben als erstes Kürzel: ")
    AutoScrabbleModul.kuerzelfunktion1(wortrest, kennzeichenliste, kuerzel)

    #Ansatz2, erstes Kürzel hat zwei Buchstaben
    wortrest = wort
    kennzeichenliste = []
    print("\nDarstellung mit zwei Buchstaben als erstes Kürzel: ")
    AutoScrabbleModul.kuerzelfunktion2(wortrest, kennzeichenliste, kuerzel)

    #Ansatz3, erstes Kürzel hat drei Buchstaben
    wortrest = wort
    kennzeichenliste = []
    print("\nDarstellung mit drei Buchstaben als erstes Kürzel: ")
    AutoScrabbleModul.kuerzelfunktion3(wortrest, kennzeichenliste, kuerzel)

    print("""
Falls keine Darstellungsmöglichkeiten ausgegeben werden,
lässt sich das Wort nicht mit mehreren Kennzeichen bilden.
    """)





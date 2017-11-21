#!/usr/bin/env python
# coding: utf8

'''
    File name: 1-Main.py
    Date created: 19/11/2017
    Date last modified: 19/11/2017
    Python version: 3.5
'''

#import ZimmerbelegungModul

#----------------------------
#Initialisierung der Varibalen
#----------------------------

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

#Zwischenspeicher für löschbare Zimmer und Negativliste (spätere Funktion)
index_delete = []

#Übergeordnete Variable, die angibt, ob alle Wünsche erfüllt werden könne
#und das Programm fortfahren soll
loesen = True

#----------------------------
#Einlesefunktionen
#----------------------------

def datei_einlesen():
    #Testdateien werden in Listen geladen
    file = open("1-beispiel-6.txt")
    while True:
        #Datei wird Zeile für Zeile eingelesen
        name = file.readline().strip()
        #Zwischenfunktion zum Entfernen der Leerzeichen und +/-
        likes = split_namen(file.readline().strip())
        hates = split_namen(file.readline().strip())
        if not file.readline():
            #print(file.readline())
            break
        #Hinzufügen der Namen in passende Liste
        eingabe_liste(name, likes, hates)

    file.close()

def eingabe_liste(name, likes, hates):
    #Hinzufügen der eingelesenen Zeilen in passende Liste

    like_list.append(likes)
    hate_list.append(hates)
    personenliste.append(name)

def split_namen(text):
    #Entfernen der Sonderzeichen am Anfang der Zeile, Leerzeichen
    #und Konvertierung zu einer Liste
    namen = text.split(' ')
    del namen[0]
    #--> Liste wird ausgegeben
    return namen


#----------------------------
#Bearbeitungsfunktionen
#----------------------------
def selbst_negativliste(personenliste, hate_list, loesen):
    #Durchgehen aller Personen, um zu überprüfen, ob sich eine Person selbst bei (-) hat
    for x in range(0, len(personenliste)):
        #Druchgehen der jeweiligen Negativlisten
        for k in hate_list[x]:
            if k == personenliste[x]:
                print("Es können nicht alle Wünsche erfüllt werden, da " + str(k) + " nicht mit sich selbst in ein Zimmer möchte.")
                loesen = False
                break
    return(loesen)



def zimmer_negativliste(zimmernegativ, hate_list, index):
    #Iteration durch bereits bestehende Liste, um Doppelnennungen zu vermeiden
    #Namen einer Person zu Negativliste eines Zimmers
    for k in hate_list[index]:
        if k not in zimmernegativ:
            zimmernegativ.append(k)
    return(zimmernegativ)

def negativlisten_zusammenfuehren(zimmernegativliste, x, zimmernegativ):
    #Iteration durch die bereits bestehenden Negativlisten (aktuelles Zimmer, Wunschzimmer)
    #Negativliste eines Zimmers in andere Negativliste übertragen
    for k in zimmernegativliste[x]:
        if k not in zimmernegativ:
            zimmernegativ.append(k)
    #Entfernen der übertragenen Negativliste
    #del zimmernegativliste[x]
    return(zimmernegativ)

def person_zimmer(name, personenliste, like_list, hate_list, zimmer, zimmernegativ, index_delete):
    index = personenliste.index(name)
    #print(name)
    test = name
    #Aktuelle Person wird in das Zimmer eingefügt und aus der Personenliste entfernt
    zimmer.append(personenliste[index])
    del personenliste[index]

    #gemeinsame Negativliste erstellen und aus hate_list entfernen
    zimmernegativ = zimmer_negativliste(zimmernegativ, hate_list, index)
    del hate_list[index]

    #zwischenspeichern der +Liste
    aktuellelike_list = like_list[index]
    del like_list[index]

    #Falls Leute in Wunschliste:
    if len(aktuellelike_list) != 0:
        #print(aktuellelike_list)
        #Durchgehen der Wünsche
        for a in aktuellelike_list:
            #Boolescher Wert für die Personensuche innerhalb der Zimmer nötig
            gefunden = False
            #Name für Funktion vergeben
            name = a
            #Nur hinzufügen, wenn Person noch nicht im gleichen Zimmer ist
            if name not in zimmer:
                index_delete = []
                #Überprüfe, ob Name bereits in anderem Zimmer:
                #Liste aller Zimmer
                for x in range(0, len(zimmerliste)):
                    #Zimmer innerhalb der Liste --> Leute in den Zimmern
                    for s in zimmerliste[x]:
                        if s == name:
                            #Wunschperson bereits in einem anderen Zimmer gefunden
                            #Zimmer werden zusammengeführt
                            zimmer += zimmerliste[x]
                            #print(zimmer)

                            #Zwischenspeichern des Indexes für späteren Löschvorgang (Liste bleibt iterierbar)
                            index_delete.append(x)
                            #print(index_delete)

                            #Gemeinsame Negativliste der beiden Zimmer erstellen
                            zimmernegativ = negativlisten_zusammenfuehren(zimmernegativliste, x, zimmernegativ)
                            #Person über Zimmer gefunden, muss nicht mehr einzeln hinzugefügt werden
                            gefunden = True
                            break
                #Person wird einzeln hinzugefügt, da in keinem Zimmer gefunden
                if gefunden == False:
                    person_zimmer(name, personenliste, like_list, hate_list, zimmer, zimmernegativ, index_delete)
                elif gefunden == True and index_delete:
                    index_delete.sort(reverse=True)
                    #print(index_delete)
                    for j in index_delete:
                        del zimmerliste[int(j)]
                        del zimmernegativliste[int(j)]


#----------------------------
#Einlesen und Vorüberprüfung
#----------------------------

datei_einlesen()
#print(personenliste)

#Überprüfe, ob sich eine Person nicht selbst in ihrer Negativliste genannt hat:
loesen = selbst_negativliste(personenliste, hate_list, loesen)


#----------------------------
#Bearbeitungschritt 1 - Vergabe aller Personen mit Wünschen und ihren Wünschen und der Wünschen, usw.
#----------------------------
if loesen == True:
    i = 0
    plus = True

    #Iteration durch eine sich verändernde Liste (keine for-Schleife möglich --> out of range)
    while plus == True:
        #Aktuelle Person hat jemanden in ihrer like_list
        if len(like_list[i]) != 0:
            zimmer = []
            zimmernegativ = []
            name = personenliste[i]

            #Person aus Wunschliste bereits woanders --> kein neues Zimmer?!

            person_zimmer(name, personenliste, like_list, hate_list, zimmer, zimmernegativ, index_delete)

            #print(zimmer)
            zimmerliste.append(zimmer)
            zimmernegativliste.append(zimmernegativ)

            #Sonderfall: falls Ende der Liste, aber Person hat jemanden in ihrer +Liste
            #wird diese entfernt und das Objekt aus der Liste gelöscht, der Iterationsindex ist somit
            #größer als die Anzahl der Listenobjekte-1 und der Zeiger befindet sich außerhalb der Liste
            #folgende if-Abfrage unterbindet einen "out of range"-Fehler
            if i > (len(personenliste)-1):
                plus = False
            i = 0
            #print(personenliste)

        #Person hat niemanden in ihrer like_list und das Ende der Personenliste ist erreicht
        elif (len(like_list[i]) == 0) and (i == (len(personenliste)-1)):
            plus = False
        #Keine Personen in like_list und noch kein Ende der Liste --> Erhöhung der
        #Iterationsvariablen um 1
        else:
            i += 1



    #----------------------------
    #Bearbeitungschritt 2 - Vergabe aller Personen ohne Wünsche, aber mit Personen in ihrer hate_list
    #----------------------------

    l = 0
    #Suche findet statt
    minus = True
    #Wenn die hate_list keine Leute mehr enthält, kann auch nach nichts gesucht werden
    if not hate_list:
        minus = False

    #Variable, die den Beitrittszustand einer Person in Bezug auf ein Zimmer angibt
    beitritt = False

    #Iteration durch eine sich verändernde Liste (keine for-Schleife möglich --> out of range)
    while minus == True:
        #Aktuelle Person hat jemanden in ihrer like_list
        if len(hate_list[l]) > 0:
            name = personenliste[l]
            zimmer = []
            zimmernegativ = []
            #Durchgehen aller Zimmer
            for x in range(0, len(zimmerliste)):
                #Beitritt bei jedem neuen Zimmer prinzipiell möglich, wird erst durch Abfrage unmöglich
                beitritt = True
                #Druchgehen aller Namen der Zimmernegativliste
                if name in zimmernegativliste[x]:
                    #Name der Person in der Negativliste enthalten, Beitritt von Seiten des
                    #Zimmers unmöglich --> widerspricht dem Wunsch einer der Personen im Zimmer
                    beitritt = False
                #Durchgehen der "Antiwünsche" der Person, wenn eine Person davon im Zimmer
                #--> Beitritt scheitert
                for k in hate_list[l]:
                    #Wenn Name im Zimmer enthalten ist
                    if k in zimmerliste[x]:
                        beitritt = False
                if beitritt == True:
                    #Person kann in aktuelles Zimmer eingefügt werden und aus der Liste entfernt werden
                    #Person ins Zimmer
                    zimmerliste[x].append(name)
                    index = l
                    zimmernegativ = zimmernegativliste[x]
                    zimmernegativliste[x] = zimmer_negativliste(zimmernegativ, hate_list, index)
                    del personenliste[l]
                    del hate_list[l]
                    break #Zimmersuche kann beendet werden
            #Durchlaufen aller Zimmer beendet
            if beitritt == False:
                #kein passendes Zimmer gefunden --> Einzelzimmer
                zimmer = [name]
                zimmernegativ = hate_list[l]
                zimmerliste.append(zimmer)
                zimmernegativliste.append(zimmernegativ)
                del personenliste[l]
                del hate_list[l]

            #Sonderfall: falls Ende der Liste, aber Person hat jemanden in ihrer -Liste
            #wird diese entfernt und das Objekt aus der Liste gelöscht, der Iterationsindex ist somit
            #größer als die Anzahl der Listenobjekte-1 und der Zeiger befindet sich außerhalb der Liste
            #folgende if-Abfrage unterbindet einen "out of range"-Fehler
            if l > (len(personenliste)-1):
                minus = False
            l = 0
            #print(personenliste)

        #Person hat niemanden in ihrer like_list und das Ende der Personenliste ist erreicht
        #print("hello")
        elif ((len(hate_list[l]) == 0) and (l == (len(personenliste)-1))) or ((len(hate_list[l]) == 0) and (l == (len(personenliste)))):
            minus = False
            print("hello")
        #Keine Personen in like_list und noch kein Ende der Liste --> Erhöhung der
        #Iterationsvariablen um 1
        else:
            l += 1

    #----------------------------
    #Bearbeitungschritt 3 - Vergabe aller Personen ohne Wünsche und ohne Leute in ihrer hate_list
    #----------------------------

    #Variable für die Suche nach einem Zimmer in Schritt 3
    gefunden = False

    #solange noch Leute übrig sind
    while len(personenliste) > 0:
        #Durchgehen aller Zimmer, aktuelle Person ist immer die erste der Übrigen aus
        #der Personenliste
        name = personenliste[0]
        zimmer = []
        zimmernegativ = []
        gefunden = False
        for x in range(0, len(zimmerliste)):
            if name not in zimmernegativliste[x]:
                #Name nicht in der Negativliste enthalten --> Person kann in's Zimmer
                zimmerliste[x].append(name)
                #Person aus der Liste entfernen
                del personenliste[0]
                #Löschen ihrer Negativliste
                del hate_list[0]
                #Person hat keine Negativliste, die zum Zimmer hinzugefügt werden muss
                #Boolean auf True, da Zimmer gefunden wurde
                gefunden = True
                break #Zimmersuche für Person beendet
        if gefunden == False:
            #kein passendes Zimmer gefunden, da der Anfangswert von False nicht auf True
            #wechselte --> Einzelzimmer
            zimmer = [name]
            zimmernegativ = []
            zimmerliste.append(zimmer)
            zimmernegativliste.append(zimmernegativ)
            del personenliste[0]
            del hate_list[0]






    print(zimmerliste)
    # print(zimmernegativliste)
#AutoScrabbleModul.py

def mittelteilfunktion1(wortrest, kennzeichenliste, kuerzel):
    umlaute = ["Ä", "Ö", "Ü", "ä", "ö", "ü"]
    #if len(wortrest) >= 1:
    if wortrest[0] not in umlaute:
        if len(wortrest) == 1: #Lösung
            kennzeichenliste = kennzeichenliste + [wortrest[0]] + [" | "]
            #Ausgabe als String
            printneu(kennzeichenliste)
        else:
            kennzeichenliste = kennzeichenliste + [wortrest[0]] + [" | "]
            wortrest = wortrest[1:]  #Wortrest um Glied 1 reduziert
            kuerzelfunktion1(wortrest, kennzeichenliste, kuerzel)
            kuerzelfunktion2(wortrest, kennzeichenliste, kuerzel)
            kuerzelfunktion3(wortrest, kennzeichenliste, kuerzel)

def mittelteilfunktion2(wortrest, kennzeichenliste, kuerzel):
    umlaute = ["Ä", "Ö", "Ü", "ä", "ö", "ü"]
    #Vermeidung von Lesefehlern, beim Aufrufen der Funktion mit len()=1
    if len(wortrest) >= 2:
        if (wortrest[0] not in umlaute) and (wortrest[1] not in umlaute):
            if len(wortrest) == 2: #Lösung
                kennzeichenliste = kennzeichenliste + [wortrest[0]] + [wortrest[1]] + [" | "]
                #Ausgabe als String
                printneu(kennzeichenliste)

            else:
                kennzeichenliste = kennzeichenliste + [wortrest[0]] + [wortrest[1]] + [" | "]
                wortrest = wortrest[2:]  #Wortrest um Glied 1-2 reduziert
                kuerzelfunktion1(wortrest, kennzeichenliste, kuerzel)
                kuerzelfunktion2(wortrest, kennzeichenliste, kuerzel)
                kuerzelfunktion3(wortrest, kennzeichenliste, kuerzel)


def kuerzelfunktion1(wortrest, kennzeichenliste, kuerzel):
    #Wortrest muss mindestens 2 Glieder haben, da noch ein Mittelteil folgen muss
    if len(wortrest) > 1:
        #Suche Kürzel für Länge 1 --> Durchgehen der Liste
        for x in range(0, len(kuerzel)-1):
            if kuerzel[x] == wortrest[0:1]:
                #Kürzel gefunden
                kennzeichenliste = kennzeichenliste + [kuerzel[x]] + ["-"] #Kürzel zur K.liste hinzugefügt
                #print(kennzeichenliste)
                wortrest = wortrest[1:]  #Wortrest um Glied 1 reduziert
                mittelteilfunktion1(wortrest, kennzeichenliste, kuerzel) #Mittelteil mit Länge 1 suchen
                mittelteilfunktion2(wortrest, kennzeichenliste, kuerzel) #Mittelteil mit Länge 2 suchen
                break


def kuerzelfunktion2(wortrest, kennzeichenliste, kuerzel):
    #Wortrest muss mindestens 3 Glieder haben, da noch ein Mittelteil folgen muss
    if len(wortrest) > 2:
        #Suche Kürzel für Länge 2 --> Durchgehen der Liste
        for x in range(0, len(kuerzel)-1):
            if kuerzel[x] == wortrest[0:2]:
                #Kürzel gefunden
                kennzeichenliste = kennzeichenliste + [kuerzel[x]] + ["-"] #Kürzel zur K.liste hinzugefügt
                #print(kennzeichenliste)
                wortrest = wortrest[2:]  #Wortrest um Glied 1-2 reduziert
                mittelteilfunktion1(wortrest, kennzeichenliste, kuerzel) #Mittelteil mit Länge 1 suchen
                mittelteilfunktion2(wortrest, kennzeichenliste, kuerzel) #Mittelteil mit Länge 2 suchen
                break

def kuerzelfunktion3(wortrest, kennzeichenliste, kuerzel):
    #Wortrest muss mindestens 4 Glieder haben, da noch ein Mittelteil folgen muss
    if len(wortrest) > 3:
        #Suche Kürzel für Länge 3 --> Durchgehen der Liste
        for x in range(0, len(kuerzel)-1):
            if kuerzel[x] == wortrest[0:3]:
                #Kürzel gefunden
                kennzeichenliste = kennzeichenliste + [kuerzel[x]] + ["-"] #Kürzel zur K.liste hinzugefügt
                #print(kennzeichenliste)
                wortrest = wortrest[3:]  #Wortrest um Glied 1-3 reduziert
                mittelteilfunktion1(wortrest, kennzeichenliste, kuerzel) #Mittelteil mit Länge 1 suchen
                mittelteilfunktion2(wortrest, kennzeichenliste, kuerzel) #Mittelteil mit Länge 2 suchen
                break


def printneu(kennzeichenliste):
    kennzeichen = ""
    #aus Listenobjekten wird ein großer String
    for x in kennzeichenliste:
        kennzeichen += str(x)
    #Ausgabe des Strings (Lösung)
    print(kennzeichen)
    #raise SystemExit


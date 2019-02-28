def gift_inschrijven(lijst, totaallijst):
    klas = lijst[0]
    bedrag = lijst[1]


    if klas in totaallijst:
        totaallijst[klas] += bedrag

    else:
        totaallijst[klas] = bedrag

    return totaallijst
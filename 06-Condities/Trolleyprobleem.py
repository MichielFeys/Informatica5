antwoord_1 = input('Trek aan de hendel van de wissel? : ')
if antwoord_1 == 'ja':
    antwoord_2 = input('Man van de brug duwen? :  ')
    if antwoord_2 == 'ja':
        doden = 2
    else:
        doden = 1
else:
    antwoord_2 = input('Man van de brug duwen? : ')
    if antwoord_2 == 'ja':
        doden = 1
    else:
        doden = 5
print(doden)

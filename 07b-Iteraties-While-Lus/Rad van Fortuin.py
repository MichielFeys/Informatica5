verborgen_woord = input('verborgen woord: ')
bedrag = int(input('gedraaide geldbedrag: '))
letter = input('letter: ')
som_bedrag = 0
nw = ''
while letter in verborgen_woord and letter not in nw:
    som_bedrag += bedrag
    nw += letter
    letter = str(input('letter: '))

if letter not in verborgen_woord:
    som_bedrag += 0

print(som_bedrag)
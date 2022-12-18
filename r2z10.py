#10. Napravi program koji unosi broj. Neka program ispiše sve parne brojeve sve dok ne dođe do unesenog broja. Neka brojevi budu ispisani jedan do drugog.
n = int(input('Unesi broj: '))
for i in range(2, n+1, 2):
        print (i, end = ' ')

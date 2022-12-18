#2. Napravi program koji unosi rezultat nogometne utakmice za Hrvatsku i Brazil te ispisuje pobjednika.
hrv=int(input('Koliko golova je zabila Hrvatska? '))
bra=int(input('Koliko golova je zabio Brazil? '))
if hrv>bra:
    print ('Hrvatska je pobjednik! :)')
elif bra>hrv:
    print ('Brazil je pobjednik! :( ')
elif bra==hrv:
    print ('Neriješeno je.')
    
        

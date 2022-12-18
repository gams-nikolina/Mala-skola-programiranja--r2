#1. Zadatak za ponavljanje:
#Napravi program u kojem upisuješ svoje ime i broj godina. Program izbacuje rečenicu: "Zovem se ______________ i imam ______________ godina, a da sam duplo stariji/a imao/la bih ____________ godina.
ime=str(input('Unesi svoje ime: '))
godine=int(input('Unesi broj godina: '))

print("Zovem se", ime, "i imam" , godine, "godina, a da sam duplo stariji/a imao/la bih", godine*2, "godina.")

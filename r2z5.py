#4. Napiši program "Python prevoditelj" koji omogućuje unošenje riječi. Nakon unošenja riječi, program prvo slovo te riječi stavlja na zadnje mjesto, a potom na početak riječi stavlja "py" te tako nastaje nova riječ. Program prikazuje i vašu upisanu riječ i novonastalu riječ.
r=input('Upiši riječ: ')
nastavak= 'py'
if len(r) > 0 and r.isalpha():
    r1=r.lower()
    r2=r.lower()
    print('Vaša riječ: ', r1)
    prvo=r1[0]
    drugo=r2[1]
    nova=nastavak+r1+prvo+drugo
    nova=nova[0:]
    print ('Nova riječ: ', nova)
    
  

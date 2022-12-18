#3. Napiši program koji unosi korisničko ime te provjerava je li korisničko ime upisano. Ukoliko je upisano neka ispiše poruku : "Dobro došao, korisničko ime!", a ukoliko nije neka ispiše poruku: "Niste upisali korisničko ime."
ime=input('Upiši korisničko ime:  ')
if ime=='':
    print("Niste upisali korisničko ime.")
else:
    print("Dobro došao/la,",ime,"!")

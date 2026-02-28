def summa(*a):
    n=1
    for son in a:
        n*=son
    return n
print(summa(1,2,3,4,5,6))



def anketa(ism,familya,**malumot):
    """Ma'lumot"""
    malumot['ism']=ism
    malumot['familya']=familya
    return malumot
print(anketa('Komil','Ataxonov',kollej='Urdu',kurs='3',yosh='25',yonalish='iqtisod'))
print(anketa('Dilshod','Matnazarov',kollej='Urdu',kurs='3',yosh='25',yonalish='iqtisod'))
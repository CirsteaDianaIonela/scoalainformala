# Creati o clasa care sa calculeze si sa returneze operatia matematica de mai jos pentru
# 4 numere: [a(b+3)/c]*d.
# Clasa trebuie sa aiba 2 metode: prima metoda este metoda speciala init.
# Iar cea dea doua metoda este metoda speciala str.
# Va rog sa aplicati cel putin doua exemple (doua obiecte).
# Metoda init trebuie sa foloseasca parametrii default a=1,b=2,c=3,d=4 si trebuie sa suprime
# orice eroare.

# class Operatie:
#     def __init__(self, a=1, b=2, c=3, d=4):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
#     def verificare(self):
#         self.e = f'Informatiile introduse nu sunt cifre'
#         if str(self.a).isnumeric() and str(self.b).isnumeric() and str(self.c).isnumeric() and str(self.d).isnumeric():
#             self.e = (self.a * (self.b + 3) / self.c) * self.d
#         return self.e
#
#     def __str__(self):
#         return f'Rezultatul este: {self.verificare()}'


# La aparitia unei erori trebuie sa afiseze textul: <>
# Folositi clasa in trei exemple:
# • cu patru parametrii numerici diferiti de cei default
# • cu 3 parametrii non-numerici
# • cu 2 parametrii numerici

# ob1 = Operatie()
# print(ob1)
# ob2 = Operatie(5, 5, 5, 5)
# print(ob2)
# ob3 = Operatie('a', 'b', 'c', 7)
# print(ob3)
# ob4 = Operatie('a', 'b', 2, 7)
# print(ob4)


# . Creati o clasa care se numeste lista_CD_DVD.
# La crearea unui obiect ala cestei clase va solicita doua argumente reprezentand titlu si
# continut cu care va crea doua atribute.
# Fiecare obiect creat va fi adaugat intr-o lista din namespace-ul global
# Clasa are o metoda care cauta si gaseste pe baza textului dat ca argument un obiect, afisiand titlu
# si continutul. Se va folosi lista de obiecte pentru a cauta.
# La afisarea obiectului returnati utilizand metoda __str__ titlul obiectului.


class Lista_CD_DVD:

    lista = []
    def __init__(self, titlu, continut):
        self.titlu = titlu
        self.continut = continut
        caracteristici = [self.titlu, self.continut]
        self.lista.append(caracteristici)

    @staticmethod
    def cautare(argument):
        mesaj = f"Obiectul nu a fost gasit"
        for i in Lista_CD_DVD.lista:
            if argument in i[0] or argument in i[1]:
                mesaj = f'Obiectul cautat este Titlu: {i[0]} si continutul este: {i[1]}'
        return mesaj

    def __str__(self):
        return f'Titlul este {self.titlu}'

# Aplicati clasa pentru 3 exemple apoi folositi cautarea pe un caz pozitiv si unul
# negativ. Printati cele 3 obiecte.

ob1 = Lista_CD_DVD('GTA', 'game')
ob2 = Lista_CD_DVD('Prajiturim', 'invatat')
ob3 = Lista_CD_DVD('Despre animale', 'descopera')
print(Lista_CD_DVD.lista)
print(Lista_CD_DVD.cautare('game'))
print(Lista_CD_DVD.cautare('viata'))

# Creati un program ce are o clasa numita util. Clasa are o variabila a clasei de tip lista
# populata automat in constructor(__init__) cu obiectul.
# Creati a doua clasa numita izatori care primeste in constructor doua argumente numite
# user si passw, formand cu ajutorul acestora doua atribute cu acelasi nume.
# Creati a treia clasa numita utilizatori care sa mosteneasca clasele util și izatori fără a
# pierde din functionalitatea claselor mostenite.
# De asemenea, aceasta clasa are o metoda privata numita parole care sa returneze un
# set cu toate parolele și o metoda privata numita useri care sa returneze un set cu toți
# userii. Se va folosi variabila clasei de tip lista care are toate obiectele pentru căutare.
# Interpretorul trebuie sa ridice o eroare setata de voi în cazul în care este apelat
# obiectul prin len(). Setati 3 obiecte și testați functionalitatea.


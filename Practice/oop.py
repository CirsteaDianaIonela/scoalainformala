class A:
    counter = 0
    zi_nastere = 12
    def __init__(self, nume):
        self.name = nume
        A.counter +=1

    def __str__(self):
        return f"Numele este {self.name}"


class B(A):
    def __init__(self, nume,adresa):
        super().__init__(nume)
        self.__adress = adresa

    def schimbare_nume(self, nume):
        self.name = nume
        return nume

    def __str__(self):
        return f"Numele este {self.name} si adresa este {self.__adress}"

class C(B)
    pass


# om1 = B("Diana","Zori de zi")
# print(om1)
# om1.schimbare_nume("Anca") #accesare metoda
# print(om1)
# print(A.zi_nastere) #accesare atribut de clasa
# om2 = A("George")
# print(om2)
# om3 = B("Cosmin", "Ciprian Porumbescu")
# print(om3)
# print(A.counter)
# print(om1.adress)
# print(om1.__dict__)
# print(om1._B__adress) #accesare atribut privat
# print(hasattr(om1, 'name'))
# print(hasattr(om1, 'nr_ochi'))
# print(hasattr(om1, 'adress'))
# om4 = A("Ionela")
# om4.varsta = 27
# print(om4.__dict__)
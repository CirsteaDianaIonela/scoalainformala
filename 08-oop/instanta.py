class Rata:

    ochi = 2 #atribut de clasa

    def __init__(self, inaltime, greutate, gen):
        self.inaltime = inaltime
        self.greutate = greutate
        self.gen = gen

    def merge(self): #metoda, actiune pe care o poate face rata
        pass

    def macane(self): #metoda, actiune pe care o poate face rata
        return "Mac-mac"

rata_1 = Rata(inaltime=10, greutate=3.4, gen =" femeiesc")
rata_2 = Rata(inaltime=20, greutate=5, gen =" barbatesc")

print(Rata.ochi) #accesam atributul de clasa

print(rata_1.macane()) #acesare valoare din metoda, apelare metoda
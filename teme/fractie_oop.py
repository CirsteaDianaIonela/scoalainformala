# Să se scrie o clasă Fractie(numarator, numitor) care sa implementeze următoarele metode:
# ○ __init__ : instanțiem numărător și numitor
# ○ __str__ : afisam "numărător/numitor"
# ○ __add__ : returnam o noua fractie care reprezinta adunarea
# ○ __sub__: returnam o nouă fracție care reprezinta scădearea
# ○ inverse: returnează o nouă fracție (inversa fracției)

class Fractie:
    def __init__(self, numarator, numitor):  #instantierea
        self.numarator = numarator
        self.numitor = numitor

    def __add__(self):  #adunarea
        return self.numarator + self.numitor

    def __sub__(self):  #scaderea
        return self.numarator - self.numitor

    def rezultat_functie(self):  #impartirea
        return self.numarator/self.numitor

    def inversul_fractiei(self):  #inversa
        try:
            return self.numitor / self.numarator
        except ZeroDivisionError:
            return f"Nu se poate imparti la 0"

    def __str__(self):  #afisarea
        self.rezultat = self.numarator/self.numitor
        return f"Rezultatul adunarii este: {self.__add__()}\n " \
               f"Rezultatul scaderii este: {self.__sub__()}\n"\
               f"Rezultatul fractiei este: {self.rezultat_functie()}\n"\
               f"Inversa factiei este: {self.inversul_fractiei()}"


fractie1 = Fractie(9, 3)
print(fractie1)

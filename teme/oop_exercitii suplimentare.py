# Creati 3 clase ce vor reprezenta un catalog auto:
# • Clasa1 • La initializare trebuie sa oferim doi parametrii de intrare marca si tip • Are o
# metoda ce accepta parametrul de intrare culoare. De asemenea o metoda numita
# AfisareCuloare pentru afisarea culorii. Folositi metoda pentru afisare.


class Clasa1():
    def __init__(self, marca, tip):
        self.marca = marca
        self.tip = tip

    def culoare_masina(self, culoare):
        self.culoare = culoare

    def __str__(self):
        return self.culoare

    # def __str__(self):
    #     return f'{self.marca, self.tip}'
# • Clasa2 : • Mosteneste Clasa1 si avem o metoda care adauga argumentul scaune_incalzite
# ca parametru de intrare

class Clasa2(Clasa1):
    def __init__(self,marca, tip, scaune_incalzite):
        super().__init__(marca, tip)
        self.scaune_incalzite = scaune_incalzite

    def __str__(self):
        return f'{self.marca, self.tip, self.scaune_incalzite}'

# • Clasa3 : • Mosteneste Clasa1 si avem o metoda care adauga argumentul
# Blocuri_Optice_LED ca parametru de intrare

class Clasa3(Clasa1):
    def __init__(self,marca, tip, LED):
        super().__init__(marca, tip)
        self.LED = LED

    def __str__(self):
        return f'{self.marca, self.tip, self.LED}'

# • Creati un obiect al Clasei 2 (marca = ARO,Tip = M461) si folositi metoda de creare argum
# DA. scaune_incalzite cu valoarea Nu;

masina1 = Clasa2('ARO', 'M461','Nu')
print(masina1)
# Creati argumentul culoare cu valoarea rosu

masina1.culoare_masina('rosu')
print(masina1.culoare)

# • Creati un obiect al Clasei 3 (marca = Dacia, Tip = 1310) si folositi metoda de creare argum.
# Blocuri_Optice_LED cu valoarea Nu;
#
masina2 = Clasa3('Dacia', '1310', 'Nu')
print(masina2)

# Creati argumentul culoare cu valoarea negru
masina2.culoare_masina('negru')
print(masina2.culoare)

# • Afisati pe rand argumentele culoare, Blocuri_Optice_LED, scaune_incalzite marca si tip a
# obiectelor create

print(masina1.culoare)
print(masina2.culoare)
print(masina1.scaune_incalzite)
print(masina2.LED)
print(masina1.tip)
print(masina2.tip)
print(masina1.marca)
print(masina2.marca)








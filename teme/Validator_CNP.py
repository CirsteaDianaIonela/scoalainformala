import datetime
CNP = input("Introdu CNP-ul: ")
CNP_introdus = list(CNP)
data = slice(1, 7, 1)
judet = slice(7, 9, 1)
data_nasterii = CNP[data]
msg = " "


def lungime():
    if len(CNP_introdus) == 13:
        return True


def S():
    if CNP_introdus[0] != "0":
        return True


def AA_LL_ZZ():
    data = slice(1, 7, 1)
    data = data_nasterii
    try:
        datetime.datetime.strptime(data, "%y%m%d")
        return True
    except ValueError:
        return False


def JJ():
    jud = ['01', 'Alba', '02', 'Arad', '03', 'Arges', '04', 'Bacau', '05', 'Bihor', '06', 'Bistrita-Nasaud', '07',
           'Botosani', '08', 'Brasov', '09', 'Braila', '10', 'Buzau', '11', 'Caras-Severin', '12', 'Cluj', '13',
           'Constanta', '14', 'Covasna', '15', 'Dambovita', '16', 'Dolj', '17', 'Galati', '18', 'Gorj', '19',
           'Harghita', '20', 'Hunedoara', '21', 'Ialomita', '22', 'Iasi', '23', 'Ilfov', '24', 'Maramures', '25',
           'Mehedinti', '26', 'Mures', '27', 'Neamt', '28', 'Olt', '29', 'Prahova', '30', 'Satu-Mare', '31', 'Salaj',
           '32', 'Sibiu', '33', 'Suceava', '34', 'Teleorman', '35', 'Timis', '36', 'Tulcea', '37', 'Vaslui', '38',
           'Valcea', '39', 'Vrancea', '40', 'Bucuresti', '41', 'Bucuresti-S1', '42', 'Bucuresti-S2', '43',
           'Bucuresti-S3', '44', 'Bucuresti-S4', '45', 'Bucuresti-S5', '46', 'Bucuresti-S6', '51', 'Calarasi', '52',
           'Giurgiu']

    judet = slice(7, 9, 1)
    judet_n = CNP[judet]
    while judet_n in jud:
        return True

def NNN():
    nnn=slice(10,13,1)
    if CNP[nnn] in range(1,1000):
        return True

def cifra_de_control():
    nr_control = (2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9)
    val = sum(a * int(b) for a, b in zip(nr_control, CNP_introdus)) % 11
    return '1' if val == 10 else str(val)


def caractere_cnp():
    if CNP.isdigit():
        return True

if lungime() and S() and AA_LL_ZZ() and JJ() and caractere_cnp() and NNN() and cifra_de_control() == CNP_introdus[12]:
    msg = "CNP valid"
    print(msg)
else:
    msg = "CNP invalid"
    print(msg)

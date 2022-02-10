#● Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg, altfel returnează valoarea 0.

def functie():
    msg = " "
    nr_introdus=input("Spune-mi o valoare: ")
    value=nr_introdus
    if value.isnumeric():
        msg = value
    else:
        msg = ("0")
    return msg
msg = functie()
print(msg)





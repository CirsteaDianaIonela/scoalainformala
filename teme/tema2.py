#● Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg, altfel returnează valoarea 0.
#
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


# Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care reprezintă numere întregi sau reale.
# ○ your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
#
# ○ your_function() va returna 0.
#
# ○ your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4)
#
# def functie_2 (1, 5, -3, ‘abc’, [12, 56, ‘cad’]):


def your_function(*lista):
    if len(list(lista)) == 0:
        print("0")
    else:
        print(sum([d for d in lista if isinstance(d, int)]))

your_function()
your_function(1, 5, -3, "abc", [12, 56, "ca"])
your_function(2, 4, "ab", "param_1 = 2")






# 2 variable
# 1 operator
# 1 rezultat

def suma (a:int,b:int) -> int:
    return f"{a} + {b} = {a+b}"


def diferenta (a:int,b:int) -> int:
    return f"{a} - {b} = {a-b}"


def inmultire (a:int,b:int) -> int:
    return f"{a} * {b} = {a*b}"


def impartire (a:int,b:int) -> float:
    if b==0:
        while b==0:
            b = int(input("Aloca o noua valoare pentru b:"))
    return f"{a} / {b} = {a/b}"


def operator() -> str:
    op = input("Alege operatorul:")
    if op not in ["*","/","+","-"]:
        while op not in ["*","/","+","-"]:
            op = input("Alege operatorul:")
    return op

def conversie(mesaj_input: str):
    nr = input(f"{mesaj_input}")
    while nr.isdigit() is False:
        nr = input(f"{mesaj_input}")
    return int(nr)

def calculator():
    nr1 = conversie("Primul numar:")
    nr2 = conversie("Al doilea numar:")
    op = operator()
    if op == "+":
        rezultat = suma(nr1,nr2)
    elif op == "-":
        rezultat = diferenta(nr1, nr2)
    elif op == "*":
        rezultat = inmultire(nr1, nr2)
    else:
        rezultat = impartire(nr1, nr2)
    return rezultat
    # return f"{nr1} {op} {nr2} = ", eval (f"{nr1} {op} {nr2}")
print(calculator())



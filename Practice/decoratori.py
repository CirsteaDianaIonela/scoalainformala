# def decorator (paramentru):
#     return paramentru
#
# @decorator
# def text(sir):
#     return sir.upper()
#
# print(text("salut"))

def decorator(functie):
    def decoreaza (var):
        return f'{functie(var)}'
    return decoreaza

@decorator
def text(sir):
    return sir.upper()

print(text("Buna"))
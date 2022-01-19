print("Numele meu este Alexandra")
print(1,type(1)) # tipul int
print(1.1, type(1.1)) #type float
print(1j, type(1j)) #tupe complex
print(int(1.1))
print(1+1) #adunare
print(1-1) #scadere
print(1*0) #inmultire
print(5/2) #impartire
print (5//2) #catul
print(5%2) #restul
print(5**2) #ridicare la putere

print(5==2) #operator de egalitate boolean true sau false
print(5!=2) #operator sde inegalitate/diferite boolean
print(5>2)
print(5<2)
print(5>=2)
print(5<=2)

print(5>2 and 3>1) #operator logic si
print(5>2 or 3>1) #operator logic sau
print(not(5>2 and 3>1)) #operator logic de negare

#my_var, my_var_1 = 0,1   #declarare variabila
my_var = 3
#my_var = my_var +1 #asignare prin alocare / incrementare
my_var *=2
print(my_var)

print("Ana are mere")

variabila = "Ana 'are' mere"
print(variabila)
nume = "Cirstea"
prenume = "Diana"
varsta = 20
inaltime = 1.65
#prezentare = "Numele meu este {} si prenumele este {}".format(nume, prenume)
#prezentare =f"Numele meu este {nume} si prenumele meu este {prenume}"

prezentare = "Numele meu este " + nume + " si prenumele este " + prenume + " si varsta mea este " +str(varsta)
print(prezentare)

#calcul = inaltime + varsta
calcul = nume + prenume
print(calcul)




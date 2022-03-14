class ClasaMea:

    gamma = 0 #atribut/variabila de clasa

    def __init__(self): #constrctorul, initializeaza valorile dintr-un obiect
        self.alpha = 1 # varibila de instance / proprietate
        self.__delta = 3 #variabila de instanta privata


obj = ClasaMea() #instantierea clasei
obj.beta = 2 #aceasta variabila este de instanta care exista doar in interiorul obj-ului/obiectului
print(obj.__dict__) #returneaza intr-un dictionar obiectele clase
print(obj.alpha)#accesare alpha din obictul obj
print(obj.gamma) #/sau print(ClasaMea.gamma) #accesare gama
print(obj._ClasaMea__delta) #accesare variabila PRIVATA
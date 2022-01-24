# tema structuri de date
mylist = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(mylist)  #declarare lista

mylist_ascending = sorted(mylist)  #lista ascendent
print(mylist_ascending)

mylist_descending = sorted(mylist, reverse=True) #lista descendent
print(mylist_descending)

print(mylist_ascending[1::2]) #lista cu numere pare

print(mylist_ascending[::2]) #lista cu numere impare

print(mylist_ascending[2::3]) # multipli ai nr 3



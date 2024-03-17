





#Ex_1 - În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
'''o adresa de meorie unde se salveaza date. datelese pot modifica pe parcursul rularii codului (suprascriere)'''


#Ex_2 - Declară și inițializează câte o variabilă din fiecare din următoarele tipuri:int, string, float, boolean
elev = "Pavel Ion" #string
varsta = 18 #integer
media_la_bac = 8.75  #float
promovat = True  #boolean
print(type(elev))
print(type(varsta))
print(type(media_la_bac))
print(type(promovat))
print(f'Variabilele noastre sunt de urmatoarele tipuri: {type(elev)}, {type(varsta)}, {type(media_la_bac)}, {type(promovat)}')
print(f'Variabilele noastre sunt de urmatoarele tipuri: {type(elev), type(varsta), type(media_la_bac), type(promovat)}')
print(type(elev), (varsta))


#Ex_3 - Utilizează funcția type pentru a verifica dacă variabilele declarate mai sus au tipul de date așteptat.
print(type(elev), (varsta))


#Ex_4 - Rotunjește variabila ‘float’ folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere), apoi verifică din nou tipul de date al acesteia.
print(round(media_la_bac,1))   #varianta scurta, rotunjire la o singura decimala
media_la_bac = round(media_la_bac)  #rotunjire la numar intreg
print(media_la_bac)

#Ex_5 - Incearca sa convertesti variabila string la int folosind type casting si observa rezultatele
''' Type Casting poate fi folosit in convertirea din string in integer, dar si din integer in string'''
#exemplul 1
var1 = "2"
print(type(var1))
var1 = int(var1)
print(type(var1))
#exemplul 2
var2 = 3
print(type(var2))
var2 = str(var2)
print(type(var2))
#print(int(elev))
#Ex_6 - Incearca sa convertesti variabila boolean la int folosind type casting si observa rezultatele
promovat= False
print(int(promovat))

#Ex_7 - Schimba valoarea variabilei boolean (din true in false sau din false in true) si repeta exercitiul anterior
promovat= True
print(int(promovat))

print("----------------------------------------")

nume= "Pavel Ion" # string
varsta=18 # int
media_la_bac= 8.75 # float
promovat= True # boolean
 # Ex 1: Folosește funcția print() și printează în consola 4 propoziții folosind cele 4 variabile.
# # Rezolvă nepotrivirile de tip pe rand prin toate modalitatile cunoscute
#print("numele elevului este" +nume +", are varsta de "+ varsta+", a luat nota"+ media_la_bac+" a promovat"+promovat)
#print("numele elevului este" +nume +", are varsta de "+ str(varsta)+", a luat nota"+ media_la_bac+" a promovat"+promovat))
#print("numele elevului este" +nume +", are varsta de "+ str(varsta)+", a luat nota"+ str(media_la_bac)+" a promovat"+promovat))
print("numele elevului este " +nume +", are varsta de "+ str(varsta)+", a luat nota "+ str(media_la_bac) +" si a promovat "+str(promovat))
# varianta formatata:
print(f"numele elevului este {nume}, are varsta de {varsta}, a luat nota {media_la_bac} si a promovat {promovat}")

#Ex_2 - Citește de la tastatură numele și prenumele unei persoane și salveaza-le in cate o variabila.
# Afișează pe ecran următoarea propoziție: 'Numele complet are x caractere'.
nume= "Pavelescu"
prenume="Raluca"
"""
cal = 1   "000 110 001"
          " c   a   l "
Cal = 1   "010 110 001"
          " C   a   l"
          declarare si initializare de variabile diferite, adrese de memorie diferite, nu este suprascriere
"""
lungime_nume= len(nume)   # functia len() aduce un rezultat de tip integer
print(lungime_nume)
lungime_prenume= len(prenume)
print(lungime_prenume)
a=lungime_nume+lungime_prenume
print(len(nume)+len(prenume))
#print(a)
#print(f"Numele complet are {a} caractere")
print(f"Numele complet are {len(nume+prenume)} caractere'")

print("-----------------------------------------------")

#Ex_3 - Citește de la tastatură lungimea și lățimea unui dreptunghi și salveaza-le in cate o variabila.
# Afișează pe ecran următoarea propoziție: 'Aria dreptunghiului este x'.
lungime= 12
latime=4
print(f"Aria dreptunghiului este {lungime*latime}")
# sau fac o alta variabila:
aria= lungime*latime
print(f"Aria dreptunghiului este {aria}")
print("---------------------------------------------")

#Ex_4 - Având stringul: 'Coral is either the stupidest animal or the smartest rock' afișează de câte ori apare
# cuvântul 'the' în acest string
propozitie="Coral is either the stupidest animal or the smartest rock"
x= "the"
print(propozitie.count(x))

#EX_5 Folosindu-te de string-ul de la exercițiul 4, inlocuieste “the” cu “THE” peste tot (inclusiv in cuvantul “either”)
# si afișează pe ecran rezultatul
print(propozitie.replace(x,x.upper()))

#Ex_6 Folosindu-te de string-ul de la exercițiul 4 foloseste un assert ca să verifici dacă acest string conține doar numere.
assert propozitie.isnumeric() == False, "Stringul nu contine doar numere"
#assert propozitie.isnumeric() == True, "Stringul nu contine doar numere"
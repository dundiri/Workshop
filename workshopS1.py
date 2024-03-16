





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
#var2 = 3
# print(type(var2))
# var2 = str(var2)
# print(type(var2))
# print(int(elev))
#Ex_6 - Incearca sa convertesti variabila boolean la int folosind type casting si observa rezultatele

#Ex_7 - Schimba valoarea variabilei boolean (din true in false sau din false in true) si repeta exercitiul anterior

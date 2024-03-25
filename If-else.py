# Ex_1 Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
'''
Structura if else, putem sa o consideram ca pe o intersectie.
Daca conditia este adevarata mergem la dreapta si executam codul
Daca condita este falsa mergem la stanga si executam codul/ skip
'''

# Ex_2 Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural daca este numar intreg mai mare ca 0)
x = 7
if x >= 0 and type(x) == int:
    print(f'{x} este numar natural')
else:
    print(f'Numarul {x} nu este numar natural')

# Ex_3 Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

if int(x) > 0:
    print("numar pozitiv")
elif int(x) < 0:
    print("numar negativ")
else:
    print("neutru")

    # Ex_4 Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).

if x >= -2 and x <= 13:
    print("numarul este inclus in intervalul -2 13")
else:
    print("nu este inclus in interval -2 13")

    # Ex_5 Verifica daca x NU este intre 5 si 27, excluzand capetele de interval. (a se folosi ‘not’)
    # x = 7

    # if not (x > 5 and x < 27):  # if not(x>5)  and not(x<27)
    # print("numarul nu este in interval")
    # else:
    # print("numarul este in interval")

    # if not x > 5 and not x < 27:       # expresia contine o dubla negatie - Not >5 si not < 27 || si Not < 27
    #     print("nu este in interval")
    # else:
    #     print("este in interval")

    # Ex_6 Declara o noua variabila y de tip int si apoi verifica si afiseaza daca a si b sunt egale, daca nu, afiseaza care din ele este mai mare
a = 8
b = 8
if a > b:
    print(f'{a} este mai mare ca {b}')
elif b > a:
    print(f'{b} este mai mare ca {a}')
else:
    print("numerele sunt egale")
        # Ex_7 Presupunand ca x, y, z (toate de tip int) reprezinta laturile unui triunghi, afiseaza daca triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau oarecare (nicio latura nu e egala).
x = 3
y = 6
z = 9
if x == y and x == z and y == z:
    print("triunghi echilateral")
elif x == y or x == z or y == z:
     print("triunghi isoscel")
else:
    print("triunghi oarecare")

#Ex_8 Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie! Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.
litera = "E"  #input(str("introduceti litera = "))
if litera.upper() == "A" or litera.upper() == "E" or litera.upper() == "I" or litera.upper() == "O" or litera.upper() == "U":
    print("litera este vocala")
elif litera.isdigit():
    print("caracterul introdus nu este litera")
else:
    print("litera este consoana")

lita_vocale = ["A", "E", "I", "O", "U"]
if litera.upper() in lita_vocale:
    print("litera este vocala")
else:
    print("litera este consoana")


'''
Calculare pret discount

Dacă un client are peste 65 de ani, atunci i se va oferi o reducere de 15%.
În caz contrar, dacă clientul nu are peste 65 de ani, dacă persoana călătorește cu cel puțin un copil va avea o reducere de 10%
Atat pentru seniori cat si pentru non- seniori se va aplica o reducere suplimentara de 10% daca vor calatori in timpul iernii.
De asemenea, atât pentru seniori, cât și pentru non seniori se va aplica o taxă de lux de 3% dacă vor călători în clasa I (în orice sezon) sau 1% taxă de gestiune în caz contrar.
'''
varsta_client = 66
discount = 0
copii = False
sezon = "iarna"
clasa = "2"
pret = 100
if varsta_client > 65:
    discount = 0.15
elif copii == True:
    discount = 0.1
if sezon == "iarna":
    discount += 0.1  # discount = discount + 0.1
if clasa == "1":
    tax = 0.03
else:
    tax = 0.01
pret_calatorie = pret - (pret*discount) + (pret*tax)
print(f'Pretul excursiei este: {pret_calatorie}')
'''
Calculare discount seller

Compania X vinde mărfuri la punctele de vânzare cu ridicata și cu amănuntul. 
Clienții angro primesc o reducere de două procente la toate comenzile. 
De asemenea, compania încurajează atât clienții angro, cât și clienții cu amănuntul
să plătească ramburs la livrare, oferind o reducere de două procente pentru această 
metodă de plată. Încă o reducere de două procente este acordată pentru comenzile de 
50 sau mai multe unități. 

'''
client_angro = True  #False
reducere = 0
cantitate = 50
ramburs = True  #False
pret = 100
if client_angro:
    reducere = 0.02
if ramburs:
    reducere += 0.02
if cantitate >= 50:
    reducere += 0.02
pret_final = pret - (pret*reducere)
print(f'Pretul total al comenzii este {pret_final}')

'''
Introduceti un nume de film de la tastatura si evaluati daca numele acelui film este 
numele filmului vostru preferat. Daca da, atunci printati pe ecran: 
“Acesta este filmul meu preferat”. In caz contrar printati pe ecran: 
“Din pacate nu este filmul meu preferat”
'''
film = "Terminator"   #input("Introduceti filmul: ")
film_preferat = "Titanic"
if film == film_preferat:
    print("Acesta este filmul meu preferat")
else:
    print("Din pacate nu este filmul meu preferat")


"""
Aveti la dispozitie urmatorul database url:
jdbc:mysql://mysql.db.server:3306/my_database?useSSL=false&serverTimezone=UTC
host = jdbc:mysql://
baza_de_date = mysql.db.server
:3306 = portul de access
/my_database?useSSL=false&serverTimezone=UTC = 

SELECT "cereneala" FROM "nume tabel"
WHERE filter and filter
ORDER by ASC sau DESC
Extrageti din acest text numele bazei de date: mysql.db.server
Folositi un if statement pentru a evalua daca numele bazei de date 
este cel corect (presupunand ca extrageti url-ul dintr-un sistem extern si 
nu stiti care este acesta)
"""
data_base_link = "jdbc:mysql://mysql.db.server:3306/my_database?useSSL=false&serverTimezone=UTC"
expected_data_base_name = "mysql.db.server"
link_without_host = data_base_link[data_base_link.index("/")+2: len(data_base_link)]
data_base_name = link_without_host[0:link_without_host.index(":")]
if data_base_name == expected_data_base_name:
    print("baza de date este corecta")
else:
    print("baza de date nu este corecta")
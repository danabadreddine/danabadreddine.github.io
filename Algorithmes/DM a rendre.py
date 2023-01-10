#PROJET PRG
AJOTIUER LES TRUCS QUIL AIME

#Ex1

def arrondi_decime(x:float) -> float :
    """Arrondi a la decime pres un nombre a virgule"""
#c'est une fonction qui prend en entree un nombre a virgule
#et donne en sortie un nombre toujours a virgule mais arrondi a la decime pres

    if x==int(x):

        return x

    else:

        return int(x*10+1)/10
#c'esr une premiere hypothese que je pose, mais je pense que le calcul ne sera pas vraiment bon


#Sinon, on peut utiliser la fonction arr qui va arrondir ; 
[inserer arr]


#Ex2

#prixkm(d:int)->float

def prixkm(d:int) -> float:
    """Calcule le prix d’un trajet en TER, en seconde classe, sur une distance donnee"""

    #la fonction prend en etree la distance d qui en l'espece represente des entiers, 
    #et affiche en sortie un nombre a virgule 

    assert d>0,"Il faut que d soit plus grand que zero" 

#le programme ne fonctionnera que si d est plus grand que 0, une distance ne peut aps etre negative

    a = 0.7781

    b = 0.1944

#on introduit les valeurs qui sont affectees a a et b pour debuter. 
#ces valeurs changent en fonction de la distance

    if d>=17 and d<=32:a = 0.2503;b = 0.2165

    elif d<=64:a = 2.0706;b = 0.1597

    elif d<=109:a = 2.8891;b = 0.1489

    elif d<=149:a = 4.0864;b = 0.1425

    elif d<=199:a = 8.0871;b = 0.1193

    elif d<=300:a = 7.7577;b = 0.1209

    elif d<=499:a = 13.6514;b = 0.1030

    elif d<=799:a = 18.4449;b = 0.0921

    else:a = 32.2041;b = 0.0755

#avec la boucle conditionnelle if et elif, on met en avant le tableau de l'enoncee qui fait correspondre a chaque distance une valeur a et une valeur b

    return a + d*b

#lorsque l'on rentre dans la boucle qui correspond a nos valeurs, on return a + d * b, soit le prix calcule suivant le bareme kilometrique


#Ex3

def prixkm1ere(p:float)->float:
    """Calcule le tarif première classe a partir du tarif de seconde classe""".

    prix= prixkm(d)
#je vais affecter a prix la valeur prixkm(d) correspondant au tarif de seconde classe

    prix= prix *1.5
#je multiplie par 1.5 le prix de second classe et j'affecte cette valeur a prix, mon prix de premiere classe

    assert p>0,"Il faut que p soit plus grand que zero" 

    return prix

#Ex4

#HYPOTHESE 1: 
def prix_speciaux_max(p:float)->float:
    """Calcule le maximum autorise pour les TGV, Intercités de nuit et Intercités à réservation obligatoire"""

    
    prix= prixkm(d)
#je vais affecter a prix la valeur prixkm(d) correspondant au tarif de seconde classe

    maximum = prix 

#HYPOTHESE 2:
REMLIR LE DEBUT 
    return p*2.1
assert p>0,"Il faut que p est plus grand que zero"


#Ex5
def distance(gare1:str,gare2:str)->float:
    """Affiche, selon les cas, un message d’erreur, noms des gares, la distance entre les deux gares et les différents prix possibles, -1 s’il y a une erreur"""

    assert gare1 != "" and gare2 != "" ,"Il faut que les noms gares ne soie pas null"

    a = open("distances.csv","r")

    d = -1

    while :

        l = a.readline()
    #a.readline lit une ligne du fichier et va l'asssigner a la variable l

        if not l:
            break

    #si la variable l est vide, on est arrive a la fin du fichier, on arrete

        t = l.split(",")
    #dans le fichier, on a le nom de la premiere gare, le nom de la deuxieme gare separes par une virgule
    #avec splir(","), on va separer ces deux gares
    #chacune va se mettre dans une case dans un tableau, d'ou la variable t representant ce tableau a 3 cases (gare 1, gare 2, et la distance entre les deux)

        if t[0]==gare1 and t[1]==gare2:
#si je trouve la ligne que je veux, 
#La variable d (troisiene case dans mon tableau)
            d = float(t[2])

            d = arrondi_decime(d/1000)

            print("De",gare1,"A",gare2,":",d,"KM")
#apres avoir cnverti de m en km, d prend la distance entre gare 1 et gare 2
#on affiche les noms des gares et la distance en km
            s = prixkm(d)

            print("Prix en seconde classe:",s,"Euro")
#on affiche le prix en seconde classe en euro
            p = prixkm1ere(s)

            print("Prix en premiere classe:",p,"Euro")
#on affiche le prix en 


    if d == -1:

        print("Erreur, l'une des gares n'existe pas")
#on affiche erreur si l'une des deux gares n'existe pas
    a.close()

    return d
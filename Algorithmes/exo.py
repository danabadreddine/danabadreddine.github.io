#foncgion fusion qui prend en etree un tableau, dont on suppose que la premiere moitie est triee, et la deuxieme moitie est triee
#et qui deplace tout dans un meme tableau et le trier. 

def pasdecopie(liste:list[int]) -> list[int]
	"""Prends en entree un tableau dont la premiere et la deuxieme partie sont triees, et qui deplacera tout dans ce meme tableau en le triant"""

#Donc dans ce cas on a deja les deux demis tableaux tries, donc c'est une fonction fusion simple

	debut=0
	milieu=len(liste)//2

	while debut < milieu and milieu <len(liste):
	#milieu represente le pointeur, je veux que debut soit plus petit que la longuer /2 meme si milieu bouge

		if liste[debut] < liste[milieu]
			debut = debut + 1
		else:
			tmp = liste[debut]
			liste[debut] = liste[milieu]
			liste[milieu] = tmp
			debut=debut+1
		if debut ==milieu
			milieu=milieu+1

	return liste

	


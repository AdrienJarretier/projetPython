from random import shuffle

'''
1)PermutationAleatoire
2)MatricePermutation
3)PermutationAssociee
6)ProduitPermutG
'''


'''
PermutationAleatoire

Entree :
	n : un entier

Sortie :
	Une liste qui represente une matrice de permutation aleatoire de taille n*n (n-uplet)
'''
def PermutationAleatoire(n) :

	nUpletPermut = []

	for i in range(n):
		nUpletPermut.append(i+1)

	shuffle(nUpletPermut)

	return nUpletPermut


'''
MatricePermutation

Entree :
	nUpletPermutation : liste representant une matrice de permutation

Sortie :
	Matrice de permutation associee à nUpletPermutation
'''




'''
PermutationAssociee

Entree :
	mPerm : matrice de permutation

Sortie :
	liste representant mPerm (n-uplet associe)
'''




'''
ProduitPermutG

n-uplet : n-uplet associe a P

l'ordre des Lignes change, dans chaque ligne i de ( P * M ) on a la ligne de M de la position de i dans n-uplet

Entree :
	P : matrice de permutation
	M : matrice quelconque

Sortie :
	matrice produit de P et M ( P * M )
'''
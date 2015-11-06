from random import shuffle
from simplesMatricesFonctions import *

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
def PermutationAleatoire( n ) :

	nUpletPermut = []

	for i in range( n ):
		nUpletPermut.append( i + 1 )

	shuffle( nUpletPermut )

	return nUpletPermut


'''
MatricePermutation

Entree :
	nUpletPermutation : liste representant une matrice de permutation

Sortie :
	Liste de listes correspondant à la Matrice de permutation associee a nUpletPermutation
'''
def MatricePermutation( nUpletPermutation ) :

	n = len( nUpletPermutation )
	matricePerm = MatNulle( n, n )

	# start DEBUG
	# afficherMat( matricePerm )
	# print( "" )
	# end DEBUG

	for col in range( n ) :
		lig = nUpletPermutation[ col ] - 1
		# on ajoute un " 1 " a la ligne specifiee par nUpletPermutation, sinon un " 0 "
		matricePerm[ lig ][ col ] = 1

	return matricePerm



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

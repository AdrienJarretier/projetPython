from simplesMatricesFonctions import *
from copy import deepcopy


##MatriceTransvection
##
##On notera une transvection : t(i,a,j)
##
##Matrice identite + a * Matrice Eij
##
##Entree :
##    i : entier : indice de la ligne/colonne à remplacer : 1 <= i
##    a : reel : coefficient de multiplication de la ligne/colonne j
##    j : entier : indice de la ligne/colonne de remplacement : 1 <= j ET j != i
##Sortie :
##    Liste de listes : Matrice de transvection
##
def MatriceTransvection( i, a, j ) :
    Id = MatId( max( i, j ) )
    Id[ i - 1 ][ j - 1 ] = a
    return Id



'''
ProduitTransvectionD

	Cj <- Cj + a * Ci

Entree :
	M : Liste de listes : Matrice(n, p)
	T : Liste de listes : Matrice de transvection(p, x)

Sortie :
	Liste de listes : matrice produit ( M * T )
'''
def ProduitTransvectionD( M, T ) :
	MProduct = deepcopy( M )

	n = len( M )
	p = len( M[ 0 ] )

	nT = len( T )
	pT = len( T[ 0 ] )

	if p != pT :

		raise Exception("le nombre de colonnes de M et de lignes de T est different")

	else :

		Ci = 0
		alpha = 0

		for i in range( nT ) :
			for j in range( pT ) :
				if i != j and T[ i ][ j ] != 0 :
					Ci = i
					alpha = T[ i ][ j ]

		for i in range( n ) :
			MProduct[ i ][ Ci ] += alpha * M[ i ][ Ci ]

	return MProduct



'''
Entree :
	T : Liste de listes : matrice de transvection

Sortie :
	composants de la transvection (i, a, j) :
		i : entier : indice de la ligne/colonne à remplacer : 1 <= i
		a : reel : coefficient de multiplication de la ligne/colonne j
		j : entier : indice de la ligne/colonne de remplacement : 1 <= j ET j!=i

'''
def TransvectionAssociee( T ) :

	AfficherMat( T )
	print("")

	nT = len( T )
	pT = len( T[ 0 ] )

	for i in range( nT ) :
		for j in range( pT ) :
			if i != j and T[ i ][ j ] != 0 :
				return i+1, T[ i ][ j ], j+1

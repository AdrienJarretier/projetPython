from simplesMatricesFonctions import *
from copy import deepcopy


##MatriceTransvection
##
##On notera une transvection : t(i,a,j)
##
##Matrice identite + a * Matrice Eij
##
##Entree :
##    n : taille des matrices
##    i : entier : indice de la ligne/colonne à remplacer : 1 <= i <=n
##    a : reel : coefficient de multiplication de la ligne/colonne j
##    j : entier : indice de la ligne/colonne de remplacement : 1 <= n ET j!=i
##Sortie :
##    Liste de listes : Matrice de transvection
##
def MatriceTransvection( n, i, a, j ) :
    Id = MatId( n )
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





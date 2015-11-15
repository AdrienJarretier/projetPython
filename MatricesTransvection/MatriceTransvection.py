from simplesMatricesFonctions import *
from copy import deepcopy
from MatricesTransvection.EstTransvection import *


##MatriceTransvection
##
##On notera une transvection : t(i,a,j)
##
##Matrice identite + a * Matrice Eij
##
##Entree :
##    i : entier : indice de la ligne/colonne à remplacer : 1 <= i
##    a : reel : coefficient de multiplication de la ligne/colonne j : a != 0
##    j : entier : indice de la ligne/colonne de remplacement : 1 <= j ET j != i
##Sortie :
##    Liste de listes : Matrice de transvection
##
def MatriceTransvection( i, a, j ) :

	if i == j or i < 1 or j < 1 :
		raise Exception( "'i' et 'j' doivent etre differents et superieurs a 0" )
	elif a == 0 :
		raise Exception( "'a' doit etre different de 0" )
	else :
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

	# print( "DEBUG : ", TransvectionAssociee( T ) )

	Ci, alpha, Cj = TransvectionAssociee( T )

	n = len( M )
	p = len( M[ 0 ] ) # nombre de colonnes

	if p < Ci or p < Cj :

		raise Exception("le nombre de colonnes de M est inferieur aux colonnes donnees dans la matrice de transvection")

	else :

		for i in range( n ) :
			MProduct[ i ][ Cj - 1 ] += alpha * M[ i ][ Ci - 1 ]

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

	# AfficherMat( T )
	# print("")

	if( EstTransvection( T ) ) :

		nT = len( T )
		pT = len( T[ 0 ] )

		for i in range( nT ) :
			for j in range( pT ) :
				if i != j and T[ i ][ j ] != 0 :

					# print( "DEBUG : i+1 : ", i + 1 )
					# print( "DEBUG : j+1 : ", j + 1 )
					# print( "DEBUG : a : ", T[ i ][ j ] )

					return i+1, T[ i ][ j ], j+1

	else :
		raise Exception("ce n'est pas une matrice de transvection valide")


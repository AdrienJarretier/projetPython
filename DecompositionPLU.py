from simplesMatricesFonctions import *

from MatricesPermutation.MatricesPermutation import *
from MatricesTransvection.MatricesTransvection import *

'''
DecompositionPLU

Decomposition en 3 matrices P, L et U
de la matrice carree donnee en entree

A peut se décomposer
sous la forme du produit de 3 matrices
sous la forme : A = PLU

Entree :
	A : liste de listes : Matrice carree

Sortie :
	P : liste de listes : Matrice de permutation
	L : liste de listes : Matrice triangulaire inferieure
	U : liste de listes : Matrice triangulaire superieure

'''
def DecompositionPLU( A ) :
	lig = 0 # indice de la ligne courante
	col = 0 # indice de la colonne courante

	n = len( A )

	P = MatId( n )
	L = MatId( n )

	while lig < n and col < n :

		lp = 0 # ligne du pivot

		pivotTrouve = False
		# booleen : False si on a trouve aucun pivot dans la colonne

		for i in range( lig, n ) :

			if A[ i ][ col ] != 0 :
				lp = i
				pivotTrouve = True
				break


		if not pivotTrouve :
			col += 1

		else :
			permut = list( range( 1, n+1 ) )
			permut[ lig ] = i + 1
			permut[ i ] = lig + 1

			Paux = MatricePermutation( permut )

			A = ProduitPermutG( Paux, A )
			P = ProduitPermutG( Paux, P )
			L = ProduitPermutG( MatricePermutationInverse( Paux ), L )

			pivot = A[ lig ][ col ]

			for i in range( lig+1, n ) :

				T = MatriceTransvection( i+1, - float( A[ i ][ col ] ) / pivot , lig+1 )
				A = ProduitTransvectionG( T, A )

				L = ProduitTransvectionG( MatriceTransvectionInverse( T ), L )

			lig += 1
			col += 1

	U = A

	return P, L, U

A = [
		[ 4, -9, 2 ],
		[ 2, -4, 4 ],
		[ -1, 2, 2 ]
	]

AfficherMat( DecompositionPLU( A ) )

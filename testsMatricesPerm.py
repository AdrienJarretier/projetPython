from MatricesPermutation import *

def afficherMat( m ) :
	# m : n'importe quelle matrice representee comme une liste de listes

	# pas de retour
	for i in range( len( m ) ) :
		print( m[ i ] )



for i in range( 5 ) :

	for j in range( 3 ) :

		nUplet = PermutationAleatoire( i + 1 )

		print("")
		print( "PermutationAleatoire", i + 1 , " : ", nUplet )

		print( " MatricePermutation( ", nUplet , " ) : " )

		afficherMat( MatricePermutation( nUplet ) )
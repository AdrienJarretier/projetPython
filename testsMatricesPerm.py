from MatricesPermutation import *
from simplesMatricesFonctions import *




for i in range( 5 ) :

	for j in range( 3 ) :

		nUplet = PermutationAleatoire( i + 1 )

		print("")
		print( "PermutationAleatoire", i + 1 , " : ", nUplet )

		print( " MatricePermutation( ", nUplet , " ) : " )

		afficherMat( MatricePermutation( nUplet ) )
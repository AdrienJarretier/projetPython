from MatricesPermutation import *

for i in range( 5 ) :

	for j in range( 3 ) :

		nUplet = PermutationAleatoire( i + 1 )

		print( "PermutationAleatoire", i + 1 , " : ", nUplet )

		print( " MatricePermutation( ", nUplet , " ) : " )

		print( MatricePermutation( nUplet ) )
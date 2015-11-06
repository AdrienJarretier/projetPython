from MatricesPermutation import *
from simplesMatricesFonctions import *




for i in range( 4 ) :

	for j in range( 3 ) :

		nUplet = PermutationAleatoire( i + 1 )

		print("")
		print( "PermutationAleatoire(", i + 1 , ") : ", nUplet )

		print( "MatricePermutation( ", nUplet , " ) : " )

		m = MatricePermutation( nUplet );

		AfficherMat( m )

		print( "PermutationAssociee : ", PermutationAssociee( m ) )
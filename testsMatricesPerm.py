from MatricesPermutation import *
from simplesMatricesFonctions import *


A = [   [ 1, 1 ],
		[ 2, 2 ],
		[ 3, 3 ],
		[ 4, 4 ],
	]


for i in range( 3, 4 ) :

	for j in range( 3 ) :

		nUplet = PermutationAleatoire( i + 1 )

		print("")
		print( "PermutationAleatoire(", i + 1 , ") : ", nUplet )

		# print( "MatricePermutation( ", nUplet , " ) : " )

		m = MatricePermutation( nUplet );

		#AfficherMat( m )
		AfficherMat( A )

		# print( "PermutationAssociee : ", PermutationAssociee( m ) )

		print("")
		print( "ProduitPermutG : " )
		AfficherMat( ProduitPermutG( m, A ) )

from simplesMatricesFonctions import *
from Decomposition import *

def testDecompositionPLU() :
	mTests = [
				[
					[ 4, -9, 2 ],
					[ 2, -4, 4 ],
					[ -1, 2, 2 ]
				],

				[
					[ 2, 4, 2, 0 ],
					[ 1, 2, 1, 0 ],
					[ 1, 2, 1, 3 ],
					[ 1, 2, 2, 1 ]
				]

			 ]

	for A in mTests :
		print("decomposition PLU de : ")

		AfficherMat( A )

		PLU = DecompositionPLU( A )

		matName = [ "P", "L", "U" ]

		for i in range( 3 ) :
			print("")
			print( matName[ i ], ":")
			AfficherMat( PLU[ i ] )

		print("")
		print("produit P * L * U")
		print("( lourd, pour tester si on retrouve la matrice de depart ) :")
		AfficherMat( produit( produit( PLU[0], PLU[1] ), PLU[2] ) )

		print("")

if __name__ == "__main__":
	testDecompositionPLU()

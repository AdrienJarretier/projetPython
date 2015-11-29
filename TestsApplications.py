from simplesMatricesFonctions import *
from Applications import *

def testDeterminantPLU() :
	print(" Determinant PLU :")

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
			],

			[
				[ 0, 3, 1 ],
				[ 4, 1, 1 ],
				[ 2, 2, 4 ]
			],

			[
				[ -6, 6 ],
				[ -2, -4 ]
			],

			[
				[ 1, 1 ],
				[ 2, -2 ]
			]

		 ]

	for A in mTests :
		print("#"*50)

		AfficherMat( A )

		detA = DeterminantPLU( A )

		print("")
		print( "determinant :", detA)




def TestResolutionTriSupCramer () :
	print("Resolution de la matrice triangulaire supérieure par la méthode de Cramer :")
	A1Tests = [
			[
				[ 1, 1, 1 ],
				[ 0, 1, 1 ],
				[ 0, 0, 1 ]
			],

			[
				[ 2, 2, 2, 2 ],
				[ 0, 2, 2, 2 ],
				[ 0, 0, 2, 2 ],
				[ 0, 0, 0, 2 ]
			],

			[
				[ 3, 3 ],
				[ 0, 3 ]

			],
			[
				[ 1, 2, 3 ],
				[ 0, 4, 5 ],
				[ 0, 0, 6 ]
			]


		  ]


	B1Tests = [
			[ 1, 1, 1 ],
			[ 0, 2, 1, 3 ],
			[ 1, 2 ],
			[ 6, 6, 6 ]
		  ]

	SolAttendues1 = [
				[ 0, 0, 1 ],
				[ -1, 0.5, -1, 1.5 ],
				[ -1/3, 2/3 ],
				[ 2.5, 0.25, 1 ]
			]

	for i in range ( len( A1Tests ) ):
		print("Systeme a resoudre :")
		print(" Matrice A :")
		AfficherMat( A1Tests[ i ] )
		print( " " )
		print( " Second membre " )
		AfficherMat( B1Tests[ i ] )
		print(" ")
		print(" Solution du systeme A * X = B attendue :")
		print(SolAttendues1[ i ])
		print(" ")
		print("Solutions du systeme A * X = B trouvée :")
		print(ResolutionTriSupCramer( A1Tests[ i ], B1Tests[ i ] ) )
		print(" ")
		print("-" * 50)



def TestResolutionTriInfCramer () :
	print("Resolution d'une matrice triangulaire inferieure par la méthode de Cramer :")

	A2Tests = [
			[
				[ 1, 0, 0 ],
				[ 1, 1, 0 ],
				[ 1, 1, 1 ]
			],

			[
				[ 2, 0, 0, 0 ],
				[ 2, 2, 0, 0 ],
				[ 2, 2, 2, 0 ],
				[ 2, 2, 2, 2 ]
			],

			[
				[ 1, 0 ],
				[ 2, 3 ]

			],
			[
				[ 1, 0, 0 ],
				[ 2, 3, 0 ],
				[ 4, 5, 6 ]

			]
		  ]

	B2Tests = [
			[ 1, 1, 1 ],
			[ 0, 2, 1, 3 ],
			[ 1, 2 ],
			[ 6, 6, 6 ]
		  ]

	SolAttendues2 = [
				[ 1, 0, 0 ],
				[ 0, 1, -0.5, 1 ],
				[ 1, 0 ],
				[ 6, -2, -4/3 ]
			]

	for i in range ( len( A2Tests ) ):
		print("Systeme a resoudre :")
		print(" Matrice A :")
		AfficherMat( A2Tests[ i ] )
		print( " " )
		print( " Second membre " )
		AfficherMat( B2Tests[ i ] )
		print(" ")
		print(" Solution du systeme A * X = B attendue :")
		print(SolAttendues2[ i ])
		print(" ")
		print("Solutions du systeme A * X = B trouvée :")
		print(ResolutionTriInfCramer( A2Tests[ i ], B2Tests[ i ] ) )
		print(" ")
		print("-" * 50)

if __name__ == "__main__":

	testDeterminantPLU()
	TestResolutionTriSupCramer ()
	TestResolutionTriInfCramer ()

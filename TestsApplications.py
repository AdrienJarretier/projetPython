from simplesMatricesFonctions import *
from Applications import *

def testDeterminantPLU() :
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

if __name__ == "__main__":
	testDeterminantPLU()

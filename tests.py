from TestsTransvections import *
from TriangulaireSup import *
from TriangulaireInf import *
from TestsDecomposition import *
from TestsApplications import *

def testTriangulaireSup() :
	M=[
	    [1,2,2],
	    [0,1,2],
	    [0,0,1]
	    ]
	AfficherMat(M)
	print(TriangulaireSup(M))

	print(" ")

	P=[
	    [1,2,3,4],
	    [0,0,2,5],
	    [4,5,6,9],
	    [5,8,6,8]
	    ]
	AfficherMat(P)
	print(TriangulaireSup(P))
	print(" ")

	T=[
	    [1,2,3,4],
	    [0,1,2,5],
	    [0,0,1,9],
	    ]
	AfficherMat(T)
	print(TriangulaireSup(T))




def testTriangulaireInf() :
	M=[
	    [1,0,0],
	    [1,1,0],
	    [1,1,1]
	    ]

	AfficherMat(M)
	print(TriangulaireInf(M))

	P=[
	    [1,0,4],
	    [1,1,0],
	    [1,1,1]
	    ]
	AfficherMat(P)
	print(TriangulaireInf(P))

	T=[
	    [1,0,0],
	    [1,1,1],
	    [1,1,1]
	    ]
	AfficherMat(T)
	print(TriangulaireInf(T))




tests = [
			[ "MatriceTransvection" , testMatriceTransvection ],
			[ "EstTransvection" , testEstTransvection ],
			[ "MatriceTransvectionInverse" , testMatriceTransvectionInverse ],
			[ "ProduitTransvectionG" , testProduitTransvectionG ],
			[ "ProduitTransvectionD" , testProduitTransvectionD ],
			[ "TransvectionAssociee" , testTransvectionAssociee ],
			[ "TriangulaireSup" , testTriangulaireSup ],
			[ "TriangulaireInf" , testTriangulaireInf ],
			[ "DecompositionPLU" , testDecompositionPLU ],
			[ "DeterminantPLU" , testDeterminantPLU ]
		]

testsTaille = len( tests );

continuerTests = True;

while continuerTests :

	print("")

	for i in range( testsTaille ) :

		print( i + 1 , "-" , tests[ i ][ 0 ] )

	print("")

	testNum = input("choix( 1-" + str(testsTaille) + ", 'q' pour quitter ) : ")

	testNum = testNum.lower()

	if testNum == "q" or testNum == "quit" or testNum == "exit" :

		continuerTests = False

	elif( testNum.isnumeric() and 0 < int( testNum ) and int( testNum ) <= len( tests ) ) :

		print("")
		tests[ int( testNum ) - 1 ][ 1 ]()


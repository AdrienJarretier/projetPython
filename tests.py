from TestsPermutations import *
from TestsTransvections import *

from TestsDecomposition import *
from TestsApplications import *




tests = [
			[ "PermutationAleatoire" , testPermutationAleatoire ],
			[ "MatricePermutation" , testMatricePermutation ],
			[ "PermutationAssociee" , testPermutationAssociee ],
			[ "EstPermutation" , testEstPermutation ],
			[ "MatricePermutationInverse" , testMatricePermutationInverse ],
			[ "ProduitPermutG" , testProduitPermutG ],
			[ "ProduitPermutD" , testProduitPermutD ],

			[ "MatriceTransvection" , testMatriceTransvection ],
			[ "EstTransvection" , testEstTransvection ],
			[ "MatriceTransvectionInverse" , testMatriceTransvectionInverse ],
			[ "ProduitTransvectionG" , testProduitTransvectionG ],
			[ "ProduitTransvectionD" , testProduitTransvectionD ],
			[ "TransvectionAssociee" , testTransvectionAssociee ],

			[ "TriangulaireSup" , testTriangulaireSup ],
			[ "TriangulaireInf" , testTriangulaireInf ],
			[ "DecompositionPLU" , testDecompositionPLU ],

			[ "DeterminantPLU" , testDeterminantPLU ],
			[ "ResolutionTriSupCramer" , TestResolutionTriSupCramer ],
			[ "ResolutionTriInfCramer" , TestResolutionTriInfCramer ],
			[ "ResolutionCramer" , TestResolutionCramer ]
		]

testsTaille = len( tests );

continuerTests = True;

while continuerTests :

	print("")

	for i in range( testsTaille ) :

		print( i + 1 , "-" , tests[ i ][ 0 ] )
		if i == 6 :
			print("")
		if i == 6 + 6 :
			print("")
		if i == 6 + 6 + 3 :
			print("")

	print("")

	testNum = input("choix( 1-" + str(testsTaille) + ", 'q' pour quitter ) : ")

	testNum = testNum.lower()

	if testNum == "q" or testNum == "quit" or testNum == "exit" :

		continuerTests = False

	elif( testNum.isnumeric() and 0 < int( testNum ) and int( testNum ) <= len( tests ) ) :

		print("")
		tests[ int( testNum ) - 1 ][ 1 ]()


from MatricesTransvection.testsTransvections import *

tests = [
			[ "MatriceTransvection" , testMatriceTransvection ],
			[ "EstTransvection" , testEstTransvection ],
			[ "MatriceTransvectionInverse" , testMatriceTransvectionInverse ],
			[ "ProduitTransvectionG" , testProduitTransvectionG ],
			[ "ProduitTransvectionD" , testProduitTransvectionD ],
			[ "TransvectionAssociee" , testTransvectionAssociee ]
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

		tests[ int( testNum ) - 1 ][ 1 ]()


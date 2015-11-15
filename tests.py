# from MatricesPermutation.testsMatricesPerm import *
# from MatricesTransvection.testEstTransvection import *
# from MatricesTransvection.testMatriceTransvectionInverse import *
# from MatricesTransvection.testMatriceTransvection import *
# from MatricesTransvection.testProduitTransvectionD import *
# from MatricesTransvection.testTransvectionAssociee import *

tests = [
		"testsMatricesPerm",
		"testEstTransvection"
		]

testsTaille = len( tests );

continuerTests = True;

while continuerTests :

	for i in range( testsTaille ) :

		print( i + 1 , "-" , tests[ i ] )

	testNum = input("choix( 1-" + str(testsTaille) + ", 'q' pour quitter ) : ")

	# print( "*",testNum,"*" )

	testNum = testNum.lower()

	if testNum == "q" or testNum == "quit" or testNum == "exit" :
		continuerTests = False

	if testNum == "1" :
		# from MatricesPermutation.testsMatricesPerm import *
		import MatricesPermutation.testsMatricesPerm
	if testNum == "2" :
		# from MatricesTransvection.testEstTransvection import *
		import MatricesTransvection.testEstTransvection


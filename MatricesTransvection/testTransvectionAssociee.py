from MatricesTransvection.MatriceTransvection import TransvectionAssociee
from MatricesTransvection.MatriceTransvection import MatriceTransvection
from simplesMatricesFonctions import *

def testTransvectionAssociee( t ) :

	i = t[ 0 ]
	a = t[ 1 ]
	j = t[ 2 ]

	try :
		Mt = MatriceTransvection( i, a, j )
		print( "Mt : " )
		AfficherMat( Mt )

		print( "Attendu :", (i, a, j) )
		print( "resultat de la fonction TransvectionAssociee a Mt :" )
		print( TransvectionAssociee( Mt ) )
		print("")

	except Exception as inst :
		print( inst )

tests = [
			( 1, 2, 2 ),
			( 4, 2, 2 ),
			( 1, 0, 2 ),
			( 20, 10, 20 )
		]

for t in tests :
	print("-"*30, "testTransvectionAssociee", t, "-"*30 )
	testTransvectionAssociee( t )
	print("")

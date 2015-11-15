from MatricesTransvection.MatriceTransvection import *
from simplesMatricesFonctions import *

from Matrice_inverse_cofacteurs import produit

def testProduitTransvectionD( M, i, a, j ) :

	T = MatriceTransvection( i, a, j )

	print("matrice de transvection : ")
	AfficherMat( T )
	print("")
	print("matrice sur laquelle appliquer la trasnvection :")
	AfficherMat( A )
	print("")
	print("resultat attendu : ")
	print("C"+str(j),"<= C"+str(j),"+",a,"* C"+str(i), "=", A[0][j-1]+a*A[0][i-1] )
	print("")
	print("resultat de la fonction ProduitTransvectionD :")
	AfficherMat( ProduitTransvectionD( A, T ) )
	print("")
	print("produit en utilisant la methode classique et lourde pour comparer : ")
	try :
		AfficherMat( produit( A, T ) )
	except Exception as inst:
		print("")
		print( inst )
		print("")
	print("")



A = [
	[ 1, 2, 3, 4, 5 ],
	[ 1, 2, 3, 4, 5 ],
	[ 1, 2, 3, 4, 5 ]
]

tests = [
		( A, 4, 0, 5 ),
		( A, 4, 3, 5 ),
		( A, 2, 1, 1 ),
		( A, 1, 10, 2 ),
		( A, 1, 10, 3 )
		]

print( "A : " )
AfficherMat( A )

for t in tests :
	try :
		print("-"*30, "testProduitTransvectionD( A," , t[1], ",", t[2], ",", t[3], ")", "-"*30 )
		testProduitTransvectionD( t[0], t[1], t[2], t[3] )
		print("")
	except Exception as inst:
		print("")
		print( "(", t[1], ",", t[2], ",", t[3],") :",inst )
		print("")

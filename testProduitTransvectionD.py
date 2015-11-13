from MatriceTransvection import *
from simplesMatricesFonctions import *

import Matrice_inverse_cofacteurs

def TransvectionAssociee( T ) :

	nT = len( T )
	pT = len( T[ 0 ] )

	Ci = 0
	Cj = 0
	alpha = 0

	for i in range( nT ) :
		for j in range( pT ) :
			if i != j and T[ i ][ j ] != 0 :
				Ci = i
				Cj = j
				alpha = T[ i ][ j ]

	return Ci, alpha, Cj

# def testProduitTransvectionD( M, T ) :

# 	a = 2
# 	i = 1
# 	j = 3
# 	t = MatriceTransvection(3,i,a,j)

# 	AfficherMat( t )
# 	print("")
# 	AfficherMat( A )
# 	print("")
# 	print("C"+str(j),"<= C"+str(j),"+",a,"* C"+str(i), "=", A[0][j-1]+a*A[0][i-1] )
# 	print("")
# 	AfficherMat( ProduitTransvectionD( A, t ) )
# 	print("")
# 	AfficherMat( Matrice_inverse_cofacteurs.produit( A, t ) )
# 	print("")

# A = [
# 	[ 1, 2, 3 ],
# 	[ 1, 2, 3 ],
# 	[ 1, 2, 3 ]
# ]

a = 2
i = 1
j = 3
print( TransvectionAssociee( MatriceTransvection(3,i,a,j) ) )
print( TransvectionAssociee( MatriceTransvection(5,i,a,j) ) )
print( TransvectionAssociee( MatriceTransvection(4,i,a,j) ) )

from MatriceTransvection import *
from simplesMatricesFonctions import *

import Matrice_inverse_cofacteurs

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

i = 1
a = 2
j = 2
print( TransvectionAssociee( MatriceTransvection(i,a,j) ) )
print("")
print( TransvectionAssociee( MatriceTransvection(i,a,j) ) )
print("")
i = 4
a = 2
j = 2
print( TransvectionAssociee( MatriceTransvection(i,a,j) ) )

from MatricesPermutation import *
from MatriceTransvection import *

from simplesMatricesFonctions import *

def testMatriceTransvection( t ) :
    print("")
    print( "MatriceTransvection", t, " : " )
    print( "matrice (", t[0], ",", t[0], ")" )
    print( "coefficient :", t[2], ", ligne :",t[1], ", colonne :" ,t[3] )
    AfficherMat( MatriceTransvection( t[0], t[1], t[2], t[3] ) )


# A = [   [ 1, 1 ],
# 		[ 2, 2 ],
# 		[ 3, 3 ],
# 		[ 4, 4 ],
# 	]


# for i in range( 3, 4 ) :

# 	for j in range( 3 ) :

# 		nUplet = PermutationAleatoire( i + 1 )

# 		print("")
# 		print( "PermutationAleatoire(", i + 1 , ") : ", nUplet )

# 		# print( "MatricePermutation( ", nUplet , " ) : " )

# 		m = MatricePermutation( nUplet );

# 		#AfficherMat( m )
# 		AfficherMat( A )

# 		# print( "PermutationAssociee : ", PermutationAssociee( m ) )

# 		print("")
# 		print( "ProduitPermutG : " )
# 		AfficherMat( ProduitPermutG( m, A ) )

# -------------------------------------- EstPermutation --------------------------------------

# M=[
#     [1,0,0,0],
#     [0,0,0,1],
#     [0,1,0,0],
#     [0,0,1,1]
#     ]

# print(EstPermutation(M))


# P=[
#     [1,0,0,0],
#     [0,0,0,0],
#     [0,1,0,0],
#     [0,0,1,0]
#     ]
# print(EstPermutation(P))


# T=[
#     [1,0,0,0],
#     [0,0,0,1],
#     [0,1,0,0],
#     [0,0,0,1]
#     ]
# print(EstPermutation(T))

# R=[
#     [1,0,0,0],
#     [0,0,0,1],
#     [0,1,0,0],
#     ]
# print(EstPermutation(R))

# # -------------------------------------- ProduitPermutD --------------------------------------

# M=[
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
#     ]

# P=[
#     [0,0,1,0],
#     [0,1,0,0],
#     [0,0,0,1],
#     [1,0,0,0]
#     ]

# AfficherMat(ProduitPermutD(M,P))

# t = ( 3, 1, 3, 3 )
# testMatriceTransvection( t )

# t = ( 5, 3, 12, 5 )
# testMatriceTransvection( t )

# t = ( 4, 3, 2, 1 )
# testMatriceTransvection( t )

A = [ [ 1, 2, 3 ],
      [ 1, 2, 3 ],
      [ 1, 2, 3 ],
      [ 1, 2, 3 ]
    ]

AfficherMat( ProduitTransvectionD( A, MatriceTransvection( 3, 2, 1, 1 ) ) )
print("")
AfficherMat( ProduitTransvectionD( A, MatriceTransvection( 3, 1, 10, 1 ) ) )
print("")
AfficherMat( ProduitTransvectionD( A, MatriceTransvection( 3, 1, 10, 2 ) ) )
print("")
AfficherMat( ProduitTransvectionD( A, MatriceTransvection( 3, 1, 10, 3 ) ) )

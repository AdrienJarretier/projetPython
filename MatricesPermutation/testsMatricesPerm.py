from MatricesPermutation import *
from MatriceTransvection import *

from simplesMatricesFonctions import *
from EstTransvection import *
from MatriceTransvectionInverse import *

from Matrice_inverse_cofacteurs import inverse


def testMatriceTransvection( t ) :
    print("")
    print( "MatriceTransvection", t, " : " )
    print( "matrice (", t[0], ",", t[0], ")" )
    print( "coefficient :", t[2], ", ligne :",t[1], ", colonne :" ,t[3] )
    Mt = MatriceTransvection( t[0], t[1], t[2], t[3] )
    AfficherMat( Mt )



def testMatriceTransvectionInverse(M,i,j,a):
    print("")
    print("Matrice :")
    AfficherMat(M)
    print( "inverse en calculant les cofacteurs ( lourd, ici pour test et comparer ) : " )
    AfficherMat( inverse( M ) )
    print("")
    print("Inverse de la matrice de transvection :")
    print("Ici la diagonale formee de 1 ne doit pas changer alors que le",a," de la colonne ",j," et de la ligne ",i," doit etre remplace par " ,-a)
    AfficherMat(MatriceTransvectionInverse(M))
    print(" ")



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


# print("Fonction EstPermutation :")

# M=[
#     [1,0,0,0],
#     [0,0,0,1],
#     [0,1,0,0],
#     [0,0,1,1]
#     ]
# print(EstPermutation(M))
# print(" ")

# P=[
#     [1,0,0,0],
#     [0,0,0,0],
#     [0,1,0,0],
#     [0,0,1,0]
#     ]
# print(EstPermutation(P))
# print(" ")

# T=[
#     [1,0,0,0],
#     [0,0,0,1],
#     [0,1,0,0],
#     [0,0,0,1]
#     ]
# print(EstPermutation(T))
# print(" ")

# R=[
#     [1,0,0,0],
#     [0,0,0,1],
#     [0,1,0,0],
#     ]
# print(EstPermutation(R))
# print(" ")

# # -------------------------------------- ProduitPermutD --------------------------------------

# -------------------------------------- ProduitPermutD --------------------------------------

# print("Fonction ProduitPermutD :")

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

# AfficherMat( ProduitPermutD( M, P ) )

# print(" ")

# # -------------------------------------- MatriceTransvection --------------------------------------

# t = ( 3, 1, 3, 3 )
# testMatriceTransvection( t )

# t = ( 5, 3, 12, 5 )
# testMatriceTransvection( t )

# t = ( 4, 3, 2, 1 )
# testMatriceTransvection( t )

# A = [ [ 1, 2, 3 ],
#       [ 1, 2, 3 ],
#       [ 1, 2, 3 ],
#       [ 1, 2, 3 ]
#     ]



# # -------------------------------------- ProduitTransvectionD --------------------------------------


# AfficherMat( ProduitTransvectionD( A, MatriceTransvection( 3, 2, 1, 1 ) ) )

# print("")
# AfficherMat( ProduitTransvectionD( A, MatriceTransvection( 3, 1, 10, 1 ) ) )

# print("")
# AfficherMat( ProduitTransvectionD( A, MatriceTransvection( 3, 1, 10, 2 ) ) )

# print("")
# AfficherMat( ProduitTransvectionD( A, MatriceTransvection( 3, 1, 10, 3 ) ) )



# # ---------------------------------- EstTransvection ------------------------

# print("Fonction EstTransvection :")

# M=[
#     [1,0,0],
#     [0,1,0],
#     [1,0,1]
#     ]
# print(EstTransvection(M))

# P=[
#     [1,0,0],
#     [1,1,1],
#     [0,0,1]
#     ]
# print(EstTransvection(P))

# T=[
#     [1,0,0,0,0],
#     [2,2,0,0,0],
#     [0,0,1,0,0],
#     [3,2,1,1,0],
#     [4,0,0,0,1]
#     ]
# print(EstTransvection(T))

# print(" ")





# --------------------------- MatriceTransvectionInverse ------------
print("Matrice de transvection Inverse :")




M=[
    [1,0,0],
    [0,1,1],
    [0,0,1]
    ]
testMatriceTransvectionInverse(M,2,3,1)

P=[
    [1,0,0,0],
    [0,1,0,0],
    [3,0,1,0],
    [0,0,0,1]
    ]
testMatriceTransvectionInverse(P,3,1,3)

T=[
    [1,0,0,0,0,0],
    [0,1,0,0,0,5],
    [0,0,1,0,0,0],
    [0,0,0,1,0,0],
    [0,0,0,0,1,0],
    [0,0,0,0,0,1]
    ]
testMatriceTransvectionInverse(T,2,6,5)

R=[
    [1,0],
    [2,1],
    ]
testMatriceTransvectionInverse(R,2,2,2)





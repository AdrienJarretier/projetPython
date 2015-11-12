from MatricesPermutation import *
from simplesMatricesFonctions import *
from EstTransvection import*
from MatriceTransvectionInverse import*

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
print("Fonction EstPermutation :")
M=[
    [1,0,0,0],
    [0,0,0,1],
    [0,1,0,0],
    [0,0,1,1]
    ]
print(EstPermutation(M))
print(" ")

P=[
    [1,0,0,0],
    [0,0,0,0],
    [0,1,0,0],
    [0,0,1,0]
    ]
print(EstPermutation(P))
print(" ")

T=[
    [1,0,0,0],
    [0,0,0,1],
    [0,1,0,0],
    [0,0,0,1]
    ]
print(EstPermutation(T))
print(" ")

R=[
    [1,0,0,0],
    [0,0,0,1],
    [0,1,0,0],
    ]
print(EstPermutation(R))
print(" ")

# -------------------------------------- ProduitPermutD --------------------------------------
print("Fonction ProduitPermutD :")
M=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]

P=[
    [0,0,1,0],
    [0,1,0,0],
    [0,0,0,1],
    [1,0,0,0]
    ]

AfficherMat(ProduitPermutD(M,P))
print(" ")

# ---------------------------------- EstTransvection ------------------------
print("Fonction EstTransvection :")
M=[
    [1,0,0],
    [0,1,0],
    [1,0,1]
    ]
print(EstTransvection(M))
print(" ")

P=[
    [1,0,0],
    [1,1,1],
    [0,0,1]
    ]
print(EstTransvection(P))
print(" ")
      
T=[
    [1,0,0,0,0],
    [2,2,0,0,0],
    [0,0,1,0,0],
    [3,2,1,1,0],
    [4,0,0,0,1]
    ]
print(EstTransvection(T))
print(" ")

# --------------------------- MatriceTransvectionInverse ------------
print("Matrice de transvection Inverse :")

def testMatriceTransvectionInverse(M,i,j,a):
    print("Matrice :")
    AfficherMat(M)
    print("Inverse de la matrice de transvection :")
    print("Ici la diagonale formee de 1 ne doit pas changer alors que le",a," de la colonne ",j," et de la ligne ",i," doit etre remplace par " ,-a)
    AfficherMat(MatriceTransvectionInverse(M))
    print(" ")




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





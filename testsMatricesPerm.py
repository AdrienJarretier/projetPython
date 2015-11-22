from MatricesPermutation.MatricesPermutation import *

from simplesMatricesFonctions import *




A = [   [ 1, 1 ],
		[ 2, 2 ],
		[ 3, 3 ],
		[ 4, 4 ],
	]


for i in range( 3, 4 ) :

	for j in range( 3 ) :

		nUplet = PermutationAleatoire( i + 1 )

		print("")
		print( "PermutationAleatoire(", i + 1 , ") : ", nUplet )

		print( "MatricePermutation( ", nUplet , " ) : " )

		m = MatricePermutation( nUplet );

		AfficherMat( m )
		AfficherMat( A )

		print( "PermutationAssociee : ", PermutationAssociee( m ) )

		print("")
		print( "ProduitPermutG : " )
		AfficherMat( ProduitPermutG( m, A ) )

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

AfficherMat( ProduitPermutD( M, P ) )

print(" ")






from Permutations import *

from simplesMatricesFonctions import *




A = [           [ 1, 1 ],
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
		print("-" * 50)

# -------------------------------------- EstPermutation --------------------------------------

print("#" * 50)
print(" ")

print("Fonction EstPermutation :")

M=[[
        [ 1, 0, 0, 0 ],
        [ 0, 0, 0, 1 ],
        [ 0, 1, 0, 0 ],
        [ 0, 0, 1, 1 ]
    ],
    [
        [ 1, 0, 0, 0 ],
        [ 0, 0, 0, 1 ],
        [ 0, 1, 0, 0 ],
        [ 0, 0, 1, 0 ]
    ],
    [
        [ 1, 0, 0, 0 ],
        [ 0, 0, 0, 0 ],
        [ 0, 1, 0, 0 ],
        [ 0, 0, 0, 1 ]
    ],
    [
        [ 1, 0, 0, 0 ],
        [ 0, 0, 0, 1 ],
        [ 0, 1, 0, 0 ],
    ],
    [
        [ 1, 2, 0 ],
        [ 0, 0, 1 ],
        [ 0, 1, 0 ],
     ]
    ]

for i in range (len(M)) :
        AfficherMat( M[i] )
        print(" ")
        print("Une matrice de permutation doit :")
        print(" - etre carre,")
        print(" - contenir que des 1 et des 0,")
        print(" - avoir qu'un seul 1 par ligne et par colonne")
        print("Cette matrice est elle une matrice de permutation ?", EstPermutation( M[ i ] ))   
        print("-" * 50)
        print(" ")

# ------------------------------------- MatricePermutationInverse ----------------------------
print("#" * 50)
print("Fontion MatricePermutationInverse :")
MP = [
        [
                [ 1, 0, 0 ],
                [ 0, 0, 1 ],
                [ 0, 1, 0 ]
        ],
        [
                [ 0, 0, 0, 1 ],
                [ 1, 0, 0, 0 ],
                [ 0, 1, 0, 0 ],
                [ 0, 0, 1, 0 ]
        ],
        [
                [ 1, 0 ],
                [ 0, 1 ]
        ]
     ]

for i in range ( len( MP ) ):
        print("Matrice de permutation :")
        AfficherMat( MP[ i ] )
        print(" ")
        print("L'inverse d'une matrice de permutation est egale a la transposee de la dite matrice")
        print("Inverse de la matrice de permutation :")
        AfficherMat( MatricePermutationInverse( MP[ i ] ))
        print(" ")
        print("-" * 50)
                     

# -------------------------------------- ProduitPermutD --------------------------------------

print("#" * 50)
print(" ")
print("Fonction ProduitPermutD :")

M=[
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ],

P=[
        [0,0,1,0],
        [0,1,0,0],
        [0,0,0,1],
        [1,0,0,0]
    ]

AfficherMat( ProduitPermutD( M, P ) )

print(" ")






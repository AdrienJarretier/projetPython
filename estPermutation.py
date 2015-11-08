from simplesMatricesFonctions import*
from MatricesPermutation import*

##Enree :
##	M : matrice à tester de taille n*p
##Sortie :
##	Vrai si la matrice M est une matrice de permutation valide


def EstPermutation( M ) :
    n = len( M )
    p = len( M[0] )
    L = []
    if n != p :
        return False
    for i in range( n ) :
        cptLigne = 0
        for j in range( n ) :
            if M[i][j] != 0 and M[i][j] != 1 :
                return False
            if M[i][j] == 1 :
                cptLigne += 1
                L.append(i)
                if i in L :
                    return False
        if cptLigne != 1 :
            return False
        
            
    
    return True

M=[
    [1,0,0,0],
    [0,0,0,1],
    [0,1,0,0],
    [0,0,1,1]
    ]

print(EstPermutation(M))


P=[
    [1,0,0,0],
    [0,0,0,0],
    [0,1,0,0],
    [0,0,1,0]
    ]
print(EstPermutation(P))


T=[
    [1,0,0,0],
    [0,0,0,1],
    [0,1,0,0],
    [0,0,0,1]
    ]
print(EstPermutation(T))

R=[
    [1,0,0,0],
    [0,0,0,1],
    [0,1,0,0],
    ]
print(EstPermutation(R))


# ------------------------------------------------------------------
##MatricePermutationInverse
##
##L'inverse d'une matrice de permutation est egale a la transposee de la dite matrice
##
##Utilisation d'une fonction Transposee()
##
##Entree :
##	mPerm : matrice de permutation
##
##Sortie :
##	matrice inverse de mPerm


def MatricePermutationInverse( mPerm ):
    return Transposee( mPerm)


# ---------------------------------------------------------------------
##ProduitPermutD
##
##n-uplet : n-uplet associe a P
##
##l'ordre des Colonnes change,
##dans chaque colonne j de ( M * P ) on a la colonne n-uplet[j] de M
##
##Entree :
##	P : matrice de permutation
##	M : matrice quelconque
##
##Sortie :
##	matrice produit de M et P ( M * P )



def ProduitPermutD( M,P ):
    L = PermutationAssociee( P )
    n=len ( M )
    p=len ( M[0] )
    A=MatNulle(n,p)
    for j in range( p ):
        for i in range( n ):
            A[i][j]=M[i][L[j]-1]
    return A

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































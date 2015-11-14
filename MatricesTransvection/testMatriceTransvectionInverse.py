from MatricesTransvection.MatriceTransvectionInverse import *

from Matrice_inverse_cofacteurs import inverse

from simplesMatricesFonctions import *

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

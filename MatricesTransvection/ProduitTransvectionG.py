from copy import deepcopy
from MatriceTransvection import *
from simplesMatricesFonctions import *
from testProduitTransvectionD import *

## ProduitTransvectionG
##
## Entree :
##	T : Liste de listes : Matrice de transvection(n, p)
##	M : Liste de listes : Matrice(p, x)
##
## Sortie :
##	Liste de listes : matrice produit ( T * M )

def ProduitTransvectionG(T,M):
    P=deepcopy(M)
    i,a,j=TransvectionAssociee(T)
    for k in range(len(P[0])):
        P[i][k]+=a*P[j][k]
    return P

M=[
    [1,1,1],
    [2,2,2],
    [3,3,3],
    [4,4,4]
    ]



a = 2
i = 1
j = 3
t = MatriceTransvection(3,i,a,j)

AfficherMat(ProduitTransvectionG(t,M))


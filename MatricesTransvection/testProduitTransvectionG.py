from MatricesTransvection import *
from simplesMatricesFonctions import *

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


from MatriceTransvection import *
from simplesMatricesFonctions import *

A = [
	[ 1, 2, 3 ],
	[ 1, 2, 3 ],
	[ 1, 2, 3 ]
]

t = MatriceTransvection(3,1,2,3)

AfficherMat( t )
AfficherMat( ProduitTransvectionD( A, t ) )

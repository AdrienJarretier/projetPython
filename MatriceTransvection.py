from simplesMatricesFonctions import *



##MatriceTransvection
##
##On notera une transvection : t(i,a,j)
##
##Matrice identite + a * Matrice Eij
##
##Entree :
##    n : taille des matrices
##    i : entier : indice de la ligne à remplacer : 1 <= i <=n
##    a : reel : coefficient de multiplication de la ligne j
##    j : entier : indice de la ligne de remplacement : 1 <= n ET j!=i
##Sortie :
##    Liste de listes : Matrice de transvection

def MatriceTransvection( n, i, a, j ) :
    Id = MatId( n )
    Id[ i - 1 ][ j - 1 ] = a
    return Id



'''
ProduitTransvectionD

Entree :
	M : Liste de listes : Matrice(n, p)
	T : Liste de listes : Matrice de transvection(p, x)

Sortie :
	Liste de listes : matrice produit ( M * T )
'''
# def ProduitTransvectionD( M, T ) :

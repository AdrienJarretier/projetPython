## ProduitTransvectionG
##
## Entree :
##	T : Liste de listes : Matrice de transvection(n, p)
##	M : Liste de listes : Matrice(p, x)
##
## Sortie :
##	Liste de listes : matrice produit ( T * M )
    
def ProduitTransvectionG(T,M):
    for k in range(len(M)):
        M[j][k]=a*M[j][k]
    M[i]=M[j]
    return M

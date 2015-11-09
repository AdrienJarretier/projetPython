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

def MatriceTransvection (i,a,j):
    Id=MatId(n)
    return Id[i][j]=a


    
    

##EstTransvection
##
##uniquement des 1 dans la diagnonale
##et des 0 partout sauf un et un seul element
##
##Entree :
##	M : Liste de listes : Matrice
##
##Sortie :
##	Booleen : vrai si M est une matrice de transvection

def EstTransvection(M):
    n=len(M)
    c=0
    cpt=0
    for i in range (n):
        if M[i][i]==1:
            c+=1
        else :
            return False
        for j in range(n):
            if M[i][j]!=0:
                cpt+=1
    if cpt!=c+1:
        return False
    return True





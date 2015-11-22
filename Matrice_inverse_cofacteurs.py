#calcul de l'inverse d'une matrice


def mineure (m,lig,col):
    #suppression de la ligne d'indice lig
    aux=m[0:lig]+m[lig+1:]
    #suppression de l'élément d'indice col
    aux2=[]
    for ligne in aux:
        aux2.append(ligne[0:col]+ligne[col+1:])
    return aux2

#developpement du determinant systématique selon la première colonne
def det(m):
    if len(m)==1:
        return m[0][0]
    else:
        s=0
        signe=1
        for lig in range (0, len (m)):
            maux=mineure(m,lig,0)
            signe=-1*signe
            s=s+signe*m[lig][0]*det(maux)
        return s

#affiche matrice
def affiche(m):
    for lig in m:
        print(lig)

#transposée d'une matrice carrée
def transpose(m):
    n=len(m)
    for i in range(0,n):
        for j in range(0,i):
            aux=m[i][j]
            m[i][j]=m[j][i]
            m[j][i]=aux
    return m

#E: m matrice carrée inversible
#calcul de l'inverse : transposée de la matrice des cofacteurs
#S: renvoie la matrice inverse
def inverse(m):
    d=det(m)
    aux=[]
    for lig in range(0,len(m)):
        ligne=[]
        if (lig % 2==0):
            signe=-1
        else:
            signe=1
        for col in range(0, len(m[0])):
            ligne.append(signe*det(mineure(m,lig,col))/d)
            signe=(-1)*signe
        aux.append(ligne)
    return transpose(aux)

#...............................................................................
#E: M1 est une matrice n*m
#   M2 est une matrice m*p
#calcul du produit de 2 matrices
#S: M1*M2
def produit (M1,M2):
    n=len(M1)
    m=len(M2)
    p=len(M2[0])
    if len(M1[0])==m:
        #calcul du produit
        R=[]
        for i in range(0,n):
            ligne=[]
            for j in range(0,p):
                som=0
                for k in range(0,m):
                     som= som + M1[i][k] * M2[k][j]
                ligne.append(som)
            R.append(ligne)
        return R
    else:
        raise Exception("Produit impossible.")


###########################################################################
# m=[[1.,2.,3.],[2.,4.,16.],[7.,8.,19.]]
# m1=[[2.,0.],[0.,2.]]
# print(m)
# affiche(m)
# print("transposee de m:")
# tm=transpose(m)
# affiche(tm)

# affiche(m)
# print("mineure")
# aux=mineure(m1,1,1)
# affiche(aux)
# print("m1=")
# affiche(m1)
# print("det(m1)=",det(m1))

# print("")
# print("m=")
# affiche(m)
# print("det(m)=",det(m))
# print("inverse de m:")
# mi=inverse(m)
# affiche(mi)
# print("produit m*inverse(m):")
# affiche(produit(mi,m))


# print("")
# m=[[1.,-1.,2.,4.],[0,3.,2.,1.],[-5.,2.,-3.,-2.],[5,-4,3,-2]]
# print("m=")
# affiche(m)
# print("det(m)=",det(m))
# print("inverse de m:")
# mi=inverse(m)
# affiche(mi)
# print("produit m*inverse(m)==Id ?:")
# affiche(produit(mi,m))
# print("inverse de l'inverse de m==m ?:")
# affiche(inverse(mi))



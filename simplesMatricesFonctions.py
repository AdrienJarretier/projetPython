def AfficherMat( m ) :
	# m : n'importe quelle matrice representee comme une liste de listes

	# pas de retour
	for i in range( len( m ) ) :
		print( m[ i ] )


'''
MatNulle

Entree :
	n : un entier
	p : un entier

Sortie :
	Matrice nulle de taille (n, p) représentée par une liste de listes
'''
def MatNulle(n, p) :
	m = []
	for i in range(n) :
		L = []
		for j in range(p):
			L.append(0)

		m.append(L)

	return m


'''
Transposee

Entree :
	m : matrice quelconque (n, p) , liste de listes

Sortie :
	Matrice (p, n) transposee de m, liste de listes
'''
def Transposee( m ) :
	transposed = MatNulle(len(m[0]), len(m))

	for i in range(len(m)) :
		for j in range(len(m[i])):
			transposed[j][i] = m[i][j]

	return transposed

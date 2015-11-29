︠bff41b37-c0dd-4e50-90d5-f5c96f59b976s︠
print("Applications :")
A = matrix(QQ,[[5,8,9,10,8],[4,5,6,4,6],[7,8,10,5,9],[11,8,4,9,2],[9,4,12,3,1]])

B = matrix(QQ,[[1,4,5,7,8]]).transpose()

P, L, U = A.LU(pivot='partial')

show("La matrice A est :")
show(A)
print(" ")

show("Le second membre est :")
show(B)
print(" ")

show("On a la decomposition PLU :")
print(" ")

show("Matrice P :")
show(P)
print(" ")

show("Matrice L :")
show(L)
print(" ")

show("Matrice U :")
show(U)
print(" ")

show("Les solutions du système sont :")
show(A.solve_right(B))


︡e9a228fa-0e3f-42f6-9a69-2ab01d63ccab︡︡{"stdout":"Applications :\n","done":false}︡{"html":"<div align='center'>La matrice A est :</div>","done":false}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrrrr}\n5 &amp; 8 &amp; 9 &amp; 10 &amp; 8 \\\\\n4 &amp; 5 &amp; 6 &amp; 4 &amp; 6 \\\\\n7 &amp; 8 &amp; 10 &amp; 5 &amp; 9 \\\\\n11 &amp; 8 &amp; 4 &amp; 9 &amp; 2 \\\\\n9 &amp; 4 &amp; 12 &amp; 3 &amp; 1\n\\end{array}\\right)$</div>","done":false}︡{"stdout":" \n","done":false}︡{"html":"<div align='center'>Le second membre est :</div>","done":false}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{r}\n1 \\\\\n4 \\\\\n5 \\\\\n7 \\\\\n8\n\\end{array}\\right)$</div>","done":false}︡{"stdout":" \n","done":false}︡{"html":"<div align='center'>On a la decomposition PLU :</div>","done":false}︡{"stdout":" \n","done":false}︡{"html":"<div align='center'>Matrice P :</div>","done":false}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrrrr}\n0 &amp; 1 &amp; 0 &amp; 0 &amp; 0 \\\\\n0 &amp; 0 &amp; 0 &amp; 0 &amp; 1 \\\\\n0 &amp; 0 &amp; 0 &amp; 1 &amp; 0 \\\\\n1 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\\\\n0 &amp; 0 &amp; 1 &amp; 0 &amp; 0\n\\end{array}\\right)$</div>","done":false}︡{"stdout":" \n","done":false}︡{"html":"<div align='center'>Matrice L :</div>","done":false}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrrrr}\n1 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\\\\n\\frac{5}{11} &amp; 1 &amp; 0 &amp; 0 &amp; 0 \\\\\n\\frac{9}{11} &amp; -\\frac{7}{12} &amp; 1 &amp; 0 &amp; 0 \\\\\n\\frac{7}{11} &amp; \\frac{2}{3} &amp; \\frac{32}{155} &amp; 1 &amp; 0 \\\\\n\\frac{4}{11} &amp; \\frac{23}{48} &amp; \\frac{53}{620} &amp; \\frac{157}{347} &amp; 1\n\\end{array}\\right)$</div>","done":false}︡{"stdout":" \n","done":false}︡{"html":"<div align='center'>Matrice U :</div>","done":false}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrrrr}\n11 &amp; 8 &amp; 4 &amp; 9 &amp; 2 \\\\\n0 &amp; \\frac{48}{11} &amp; \\frac{79}{11} &amp; \\frac{65}{11} &amp; \\frac{78}{11} \\\\\n0 &amp; 0 &amp; \\frac{155}{12} &amp; -\\frac{11}{12} &amp; \\frac{7}{2} \\\\\n0 &amp; 0 &amp; 0 &amp; -\\frac{694}{155} &amp; \\frac{353}{155} \\\\\n0 &amp; 0 &amp; 0 &amp; 0 &amp; \\frac{757}{1388}\n\\end{array}\\right)$</div>","done":false}︡{"stdout":" \n","done":false}︡{"html":"<div align='center'>Les solutions du système sont :</div>","done":false}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{r}\n\\frac{5431}{1514} \\\\\n-\\frac{4317}{757} \\\\\n-\\frac{971}{1514} \\\\\n\\frac{1657}{1514} \\\\\n\\frac{2225}{757}\n\\end{array}\\right)$</div>","done":false}︡{"done":true}
︠a5745760-2425-4267-9732-e61864d69478s︠
︡ad39b844-050d-4d17-bbc9-b5a0345f00f0︡︡{"done":true}
︠c573878b-088c-4754-bd2a-f1961dce469ds︠
︡fddaa45a-44d4-4f43-b92d-c92d0e57edf9︡︡{"done":true}
︠7b73dbb2-b181-465f-8f7e-e7ffed288cb8︠
︠679d3303-6da9-4522-b0bb-12e81198afa6︠










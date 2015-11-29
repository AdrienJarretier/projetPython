︠5034a64d-2d92-4990-82e5-68e04bf438f8s︠
def testDeterminantPLU() :
    mTests = [
                [
                    [ 4, -9, 2 ],
                    [ 2, -4, 4 ],
                    [ -1, 2, 2 ]
                ],

                [
                    [ 2, 4, 2, 0 ],
                    [ 1, 2, 1, 0 ],
                    [ 1, 2, 1, 3 ],
                    [ 1, 2, 2, 1 ]
                ],

                [
                    [ 0, 3, 1 ],
                    [ 4, 1, 1 ],
                    [ 2, 2, 4 ]
                ],

                [
                    [ -6, 6 ],
                    [ -2, -4 ]
                ],

                [
                    [ 1, 1 ],
                    [ 2, -2 ]
                ]

             ]

    for m in mTests :
        print("#"*50)

        A = matrix(QQ, m)

        show( A )

        detA = A.determinant()

        print("")
        print( "determinant :", detA)

        print("")

testDeterminantPLU()

︡8f3535d0-e435-49fc-a4ce-b3995e4987b6︡︡{"stdout":"##################################################\n","done":false}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrr}\n4 &amp; -9 &amp; 2 \\\\\n2 &amp; -4 &amp; 4 \\\\\n-1 &amp; 2 &amp; 2\n\\end{array}\\right)$</div>","done":false}︡{"stdout":"\n('determinant :', 8)\n\n##################################################\n","done":false}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrrr}\n2 &amp; 4 &amp; 2 &amp; 0 \\\\\n1 &amp; 2 &amp; 1 &amp; 0 \\\\\n1 &amp; 2 &amp; 1 &amp; 3 \\\\\n1 &amp; 2 &amp; 2 &amp; 1\n\\end{array}\\right)$</div>","done":false}︡{"stdout":"\n('determinant :', 0)\n\n##################################################\n","done":false}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrr}\n0 &amp; 3 &amp; 1 \\\\\n4 &amp; 1 &amp; 1 \\\\\n2 &amp; 2 &amp; 4\n\\end{array}\\right)$</div>","done":false}︡{"stdout":"\n('determinant :', -36)\n\n##################################################\n","done":false}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rr}\n-6 &amp; 6 \\\\\n-2 &amp; -4\n\\end{array}\\right)$</div>","done":false}︡{"stdout":"\n('determinant :', 36)\n\n##################################################\n","done":false}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rr}\n1 &amp; 1 \\\\\n2 &amp; -2\n\\end{array}\\right)$</div>","done":false}︡{"stdout":"\n('determinant :', -4)\n\n","done":false}︡{"done":true}
︠367ab8cd-72fc-45f3-9aa2-629298934671︠










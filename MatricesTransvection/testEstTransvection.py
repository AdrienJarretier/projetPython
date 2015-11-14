from MatricesTransvection.EstTransvection import *

print("Fonction EstTransvection :")

M=[
    [1,0,0],
    [0,1,0],
    [1,0,1]
    ]
print(EstTransvection(M))

P=[
    [1,0,0],
    [1,1,1],
    [0,0,1]
    ]
print(EstTransvection(P))

T=[
    [1,0,0,0,0],
    [2,2,0,0,0],
    [0,0,1,0,0],
    [3,2,1,1,0],
    [4,0,0,0,1]
    ]
print(EstTransvection(T))

print(" ")

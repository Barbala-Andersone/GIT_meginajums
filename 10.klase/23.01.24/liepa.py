"""Sastādīt programmu, kas lietotājam jautā 
ievadīt divus skaitļus un izvada to dalījumu.
Piezīme. Dalīt ar nulli nedrīkst!
"""

A=int(input("Ievadi pirmo skaitli:"))
B=int(input("Ievadi otro skaitli:"))
if B==0:
    print("Dalīt ar nulli nedrīkst!")
else:
    if A%B==0:
        print(f"{A} dalot ar {B} iegūst {int(A/B)}")
    else:
        print(f"{A} dalot ar {B} iegūst {A/B}")
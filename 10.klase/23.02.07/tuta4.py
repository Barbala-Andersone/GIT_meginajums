"""
# Kāda būs x vērtība pēc koda izpildes
for l in "olgola": #ir vēl joprojām apgabalā 
    if l == "o":
        print("hhs")
        pass 
    print(l, end=", ")

for num in range(2,-5,-1):
    print(num,end=", ")

""
num   izdrukā
 2     2, 
 1     1, 
 0     0, 
-1    -1, 
-2    -2, 
-3    -3, 
-4    -4, 
""


for num in range(10,14):
    for i in range(2,num):
        if num%i == 1:
            print(num)
            break

""
num   i   izdrukā
10    2    ------
      3    10
      4    ------
      ...
      9
11    2    1
      3
      4
      5
      ...
12
13
14
""
"""
"""
var   10                             11      12                 13    14                15     16               17     18             19     20          21
i         0                      1       2                  3      4                 5      6                7      8              9     10
j            2 3 4 5 6 7 8 9 10                  2 ... 10                  2 ... 10                 1 ...10                1...10                1...10 
"""
"""
i        j        var
0        2        10
0        3        10
0        4        10
0        5        10
0        6        10
0        ...      10
0        9        11
1        9        12

2        2        12
2        ...      12
2        9        12

2        9        13
3        9        14

4        2        14
4        ...      14
4        9        14
4        9        15
5        9        16

6        2
var:
16
i:
6
j:
3
var:
16
i:
6
j:
4
var:
16
i:
6
j:
5
var:
16
i:
6
j:
6
var:
16
i:
6
j:
7
var:
16
i:
6
j:
8
var: 
16
i:
6
j:
9
var:
16
i:
6
j:
9
var:
17
i:
7
j:
9
var:
18
i:
8
j:
2
var:
18
i:
8
j:
3
var:
18
i:
8
j:
4
var:
18
i:
8
        j: 5
                var: 18
i: 8
        j: 6
                var: 18
i: 8
        j: 7
                var: 18
i: 8
        j: 8
                var: 18
i: 8
        j: 9
                var: 18
i: 8
        j: 9
                var: 19
i: 9
        j: 9
                var: 20
i: 9
        j: 9
                var: 21
"""

var=10
for i in range(10):
    for j in range(2,10,1):
        if var % 2 == 0:
             continue
             var+=1
    var+=1
else:
    var+=1
print(var)

"""
var  i  j 
10   
     0  
        2  
11 
        3
12
     1
        2
13
        3
14
     2  
        2
15
        3
16
     3
        2
17
        3
18
     4
        2
19
        3
20
     5
        2
21

        3
     3
20
        2
21
        3
     3
"""
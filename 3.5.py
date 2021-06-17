x=[0,34,245,0,542]
y=[42,41,0,52,2425]
for i in x:
    for j in y:
        # print(f"{i} is x and {j} is y") 
        print(f"{i} < 1/3 < {j}",i<1/3<j)

"""
output
0 < 1/3 < 42 True
0 < 1/3 < 41 True
0 < 1/3 < 0 False
0 < 1/3 < 52 True
0 < 1/3 < 2425 True
34 < 1/3 < 42 False
34 < 1/3 < 41 False
34 < 1/3 < 0 False
34 < 1/3 < 52 False
34 < 1/3 < 2425 False
245 < 1/3 < 42 False
245 < 1/3 < 41 False
245 < 1/3 < 0 False
245 < 1/3 < 52 False
245 < 1/3 < 2425 False
0 < 1/3 < 42 True
0 < 1/3 < 41 True
0 < 1/3 < 0 False
0 < 1/3 < 52 True
0 < 1/3 < 2425 True
542 < 1/3 < 42 False
542 < 1/3 < 41 False
542 < 1/3 < 0 False
542 < 1/3 < 52 False
542 < 1/3 < 2425 False
"""
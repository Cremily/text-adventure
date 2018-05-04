from itertools import product
values = []
for p in product((True,False),repeat=3):
    values.append(p)
def implies(a,b):
    if b == False and a == True:
        return False
    else:
        return True
for x in values:
    a = x[0]
    b = x[1]
    c = x[2]
    table = (a,b,c)
    a_imp_b = implies(a,b)
    na_imp_c = implies(not a,c)
    table = (a_imp_b,na_imp_c)
    P = a_imp_b and na_imp_c 
    Q = a_imp_b or na_imp_c
    R = implies(a_imp_b,na_imp_c)
    print(table,R)

"""
send a function calculate the time
"""


from py_ecc.bn128 import G1, G2, pairing, add, multiply, eq,neg,curve_order
import random
import functools
from ecpy.curves import Curve
import libnum
import numpy as np 
import timeit
import math

"""
A = multiply(G2, 5)
B = multiply(G1, 6)
print(pairing(A, B))

"""

"""
crs 
"""


def get_crs_G2(tau):
    crs = []
    for i in range(30):
        x = (tau**(i))    
        e_point = multiply(G2,x)
        crs.append(e_point)
    return(crs)


def get_crs_G1(tau):
    crs = []
    for i in range(30):
        x = (tau**(i))    
        e_point = multiply(G1,x)
        crs.append(e_point)
    return(crs)


"""
commit polynomial
"""


def poly_commit_G1(poly,crs):
    coef = list(poly.coef)
    coef.reverse()
    commit = multiply(G1,int(coef[0]) % curve_order)
    for i in range(len(coef)):
        if i>0:
            commit = add(commit,multiply(crs[i],int(coef[i]) % curve_order))
    return(commit)


def poly_commit_G2(poly,crs):
    coef = list(poly.coef)
    coef.reverse()
    commit = multiply(G2,int(coef[0]) % curve_order)
    for i in range(len(coef)):
        if i>0:
            commit = add(commit,multiply(crs[i],int(coef[i]) % curve_order))
    return(commit)



def eval_proof_g2(poly_1,a,crs_g2):
    y = poly_1(a)
    poly_2 = poly_1 - y
    poly_3 = np.poly1d([1,-a])
    poly_41 = np.polydiv(poly_2,poly_3)
    poly_4 = poly_41[0]
    eval_commit = poly_commit_G2(poly_4,crs_g2)
    return(eval_commit)


def eval_proof_g1(poly_1,a,crs_g1):
    y = poly_1(a)
    poly_2 = poly_1 - y
    poly_3 = np.poly1d([1,-a])
    poly_41 = np.polydiv(poly_2,poly_3)
    poly_4 = poly_41[0]
    eval_commit = poly_commit_G1(poly_4,crs_g1)
    return(eval_commit)



def execute_zkp(poly_1):

    tau = 12
    crs_g2 = get_crs_G2(tau)
    crs_g1 = get_crs_G1(tau)
    a = 2
    y = poly_1(a)

    polycommit = poly_commit_G2(poly_1,crs_g2)
    evalcommit = eval_proof_g2(poly_1,a,crs_g2)

    polyB = np.poly1d([1,-a])

    B = add(crs_g1[1],neg( multiply(G1,a)))

    #polyBcommit = poly_commit_G1(polyB,crs_g1)

    C = add(polycommit,neg( multiply(crs_g2[0],y)))

    ret = 'xxx'
    if(pairing(evalcommit,B) == pairing(C,G1)):
        ret = 'aaa'
    else:
        ret = 'bbb'
    return(ret)



def get_poly(a1,a2,n):
    coef = [0]*(2*n)
    for i in range(n):
        x = (-1)**i
        y = math.factorial(2*i)
        id = 2*i
        coef[id] = a1*(x/y)
    coef.reverse()
    cos_poly = np.poly1d(coef)

    coef = [0]*(2*n)
    for i in range(n):
        x = (-1)**i
        y = math.factorial(2*i+1)
        id = 2*i+1
        coef[id] = a2*(x/y)
    coef.reverse()
    sin_poly = np.poly1d(coef)
    return(cos_poly+sin_poly)


a1 = 2
#poly_x = np.poly1d([1,2,3,4])

def get_zkp_time(polys):
    t = []
    for i in range(len(polys)):
        poly_x = polys[i]
        start = timeit.default_timer()
        ret = execute_zkp(poly_x)
        print(ret)
        stop = timeit.default_timer()
        t.append(stop - start)

    return(t)














#!/usr/bin/python3
# -*- coding: utf-8 -*-

#------------------------------------------
# Newton
#------------------------------------------

from math import *
# La fonction sigma
def sigma(x):
    return 1/(1+exp(-x))

a = 68
b = -1
c = -44



# Exemple 1
print("--- Exemple ---")
t,p = 1.77,79
f = a*t+b*p+c
s = sigma(f)
print("taille t =",t)
print("poids p =",p)
print("onction affine f =",f)
print("sortie  =",s)


# Exemple 2
print("--- Exemple ---")
t,p = 1.65,67
f = a*t+b*p+c
s = sigma(f)
print("taille t =",t)
print("poids p =",p)
print("onction affine f =",f)
print("sortie  =",s)
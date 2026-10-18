#se importan en un inicio las librerias necesarias para el funcionamiento del programa
import numpy as np
import time

class calc :
    def __init__ ( z) :
        z . d ={}
    def p (z ,n , vals ) :
        if n <=0: return 0.0
        if n ==1: return vals [0]
        if n in z . d : return z. d [ n ]
        r = min ( z . p (n -1 , vals ) + vals [n -1] , z . p (n -2 , vals ) + vals [n -1]*0.8)
        z . d [ n ]= r ; return r

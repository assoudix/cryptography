#!/usr/bin/python3

import numpy
import sys

val1='0011'

def encode(m, g):
  """codage: message (m)*matrice_g(g)"""
  en = numpy.dot(m, g)%2
  return en

def decode(m, h):
  """décodage: matrice_h(h)*message(m)"""
  dec = numpy.dot(h, m)%2
  return dec

def flipbit(enc,bitpos):

  if (enc[bitpos]==1):
    enc[bitpos]=0
  else:
    enc[bitpos]=1
  return enc

def hamming(inp):
  g =  numpy.array([[1, 0, 0, 0, 1, 1, 1],[0, 1, 0, 0, 0, 1, 1],[ 0, 0 ,1 ,0 ,1 ,0 ,1],[0, 0, 0, 1, 1, 1, 0]])
  h = numpy.array([[ 1, 0, 1, 1, 1, 0, 0],[1 ,1 ,0 ,1 ,0 ,1 ,0],[ 1 ,1, 1, 0, 0, 0, 1],])

  inp = inp[:4]

  enc = encode(inp, g)

  dec = decode(enc, h)
  print ("Input  \t\tCoded (1 error)  \tError Position")
  print (inp,"\t",enc,"\t",dec)

  print ("----------------------")
  print ("Single Errors:")
  print ("Input  \t\tCoded (1 error)  \tError Position")
  for i in range (0,7):
    enc = encode(inp, g)
    enc1=flipbit(enc,i)
    dec = decode(enc1, h)
    print (inp,"\t",enc1,"\t",dec)

inp = numpy.array(list(map(int, val1)))


hamming(inp)
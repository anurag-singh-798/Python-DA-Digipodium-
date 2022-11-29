# Wap to calculate SI & Amount

from msilib.text import tables
from re import T


p = float(input("Enter PA : "))
r = float(input("Enter Rate of interest : "))
t = float(input("Enter time : ")) 

SI = p*r*t / 100
print("Simple interest :", SI)

amount = p + SI
print("Amount : ", amount)
from lib.class_patients import Patients
from lib.euclidean import euclidean
from lib.pearson import pearson
from lib.scaledown import scaledown
from math import *
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
from numpy import *
import pylab

print "Activitat: 4"
print

# llegir dades fitxer
patients = Patients("echocardiogram.csv")

num_variables = 7
d, myClass = patients.convertToProcessData(num_variables)

# separar dades segons la classe per a l'MDS
print "Separant les dades en dos sectors segons la classe..."
n = len(myClass)
num_elements_group_A_myClass = sum(myClass)
num_elements_group_B_myClass = n - num_elements_group_A_myClass

d_separacio_grups = zeros(shape(d), float)
posi = 0
for i in range(shape(d)[0]):
    if myClass[i] == 1:
        for j in range(shape(d)[1]):
            d_separacio_grups[posi][j] = d[i][j]
        posi += 1
posi = num_elements_group_A_myClass
for i in range(shape(d)[0]):
    if myClass[i] == 0:
        for j in range(shape(d)[1]):
            d_separacio_grups[posi][j] = d[i][j]
        posi += 1

# calcular MDS amb Pearson Score
print "MDS amb Pearson Score..."
mds = scaledown(d_separacio_grups, pearson)

# plotejar MDS amb Pearson Score
print "Plotejant MDS segons la classe..."
fig1 = pylab.figure()
for i in range(0, num_elements_group_A_myClass, 1):
    pylab.scatter(mds[i][0], mds[i][1], marker='o', c='b')
for i in range(num_elements_group_A_myClass, n, 1):
    pylab.scatter(mds[i][0], mds[i][1], marker='x', c='r')
fig1.suptitle('Metrica: Pearson Score')
pylab.show()

print
# calcular MDS amb Euclidean Distance
print "MDS amb Euclidean Distance..."
mds = scaledown(d_separacio_grups, euclidean)

# plotejar MDS amb Euclidean Score
print "Plotejant MDS segons la classe..."
fig1 = pylab.figure()
for i in range(0, num_elements_group_A_myClass, 1):
    pylab.scatter(mds[i][0], mds[i][1], marker='o', c='b')
for i in range(num_elements_group_A_myClass, n, 1):
    pylab.scatter(mds[i][0], mds[i][1], marker='x', c='r')
fig1.suptitle('Metrica: Euclidean Distance')
pylab.show()

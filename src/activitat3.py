from lib.class_patients import Patients
from math import *
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
from numpy import *
import pylab

def analisi_Multivariable(d):
    centroides = d.mean(0) # centroides = mitja_Aritmetica(d)
    A = d - centroides
    matriu_autocorrelacio = dot(A.T, A)
    return A, centroides, matriu_autocorrelacio

def descomposicio_Valors_Singulars(matcov):
    return linalg.eig(matcov)

print "Activitat: 3"
print

# llegir dades fitxers
patients = Patients("echocardiogram.csv")

num_variables = 6
d, myClass = patients.convertToProcessData(num_variables)
A, centroides, matriu_autocorrelacio = analisi_Multivariable(d)

# Obtenir els valors singulars
valors_Propis, vectors_Propis = descomposicio_Valors_Singulars(matriu_autocorrelacio)

# Obtenir els valors propis ordenats per ordre decreixent
indexs_creixent = argsort(valors_Propis)  # orden creciente 
indexs_decreixent = indexs_creixent[::-1] # orden decreciente 
valors_Propis_OrdreDecreixent = valors_Propis[indexs_decreixent] # valores propios en orden decreciente
vectors_Propis_OrdreDecreixent = vectors_Propis[:,indexs_decreixent] # valores propios en orden decreciente

# determinar el % de varianca amb 3 components
valors_Propis_suma = sum(valors_Propis)
numero_components = 3
print "Percentatge de varianca amb", numero_components, "components", 100.0 * (sum(valors_Propis_OrdreDecreixent[:numero_components]) / valors_Propis_suma), "%"

print "PCA amb",numero_components,"components: amb els",numero_components,"VEPS amb mes VAP..."
d_PCA = zeros((d.shape[0], numero_components), float)
for i in range(d_PCA.shape[0]):
    for j in range(d_PCA.shape[1]):
        d_PCA[i, j] = dot(A[i, :], vectors_Propis_OrdreDecreixent[:, j])

# separacio en classes: StillAlive
print "Separant valors PCA en classes, utilitzant StillAlive com a classe..."
num_elems_class_true = sum(myClass)
num_elems_class_false = len(myClass) - num_elems_class_true
d_PCA_class_true = zeros((num_elems_class_true, numero_components))
d_PCA_class_false = zeros((num_elems_class_false, numero_components))
posi_class_false = 0
posi_class_true = 0
for i in range(len(myClass)):
    if (myClass[i] == 0):
        for j in range(d_PCA.shape[1]):
            d_PCA_class_false[posi_class_false][j] = d_PCA[i][j]
        posi_class_false += 1
    else:
        for j in range(d_PCA.shape[1]):
            d_PCA_class_true[posi_class_true][j] = d_PCA[i][j]
        posi_class_true += 1

print "Plotejant valors PCA segons la classe..."
fig2 = plot.figure()
sp2 = fig2.gca(projection='3d')
sp2.scatter(d_PCA_class_false[:, 0], d_PCA_class_false[:, 1], d_PCA_class_false[:, 2], c='r', marker='x')
sp2.scatter(d_PCA_class_true[:, 0], d_PCA_class_true[:, 1], d_PCA_class_true[:, 2], c='b', marker='o')
plot.show()

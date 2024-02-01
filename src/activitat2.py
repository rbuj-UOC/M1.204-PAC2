from lib.class_patients import Patients
from math import *
from numpy import *

def mitja_Aritmetica(d):
    resultat = zeros(d.shape[1])
    for i in range(d.shape[1]):
        resultat[i] = sum(d[:, i]) / d.shape[0]
    return resultat

def analisi_Multivariable(d):
    centroides = d.mean(0) # centroides = mitja_Aritmetica(d)
    A = d - centroides
    matriu_autocorrelacio = dot(A.T, A)
    return A, centroides, matriu_autocorrelacio

def descomposicio_Valors_Singulars(matcov):
    return linalg.eig(matcov)

print "Activitat: 2"
print

# llegir dades fitxers
patients = Patients("echocardiogram.csv")

num_variables = 7
d, myClass = patients.convertToProcessData(num_variables)
A, centroides, matriu_autocorrelacio = analisi_Multivariable(d)

# Obtenir els valors singulars
valors_Propis, vectors_Propis = descomposicio_Valors_Singulars(matriu_autocorrelacio)

# Obtenir els valors propis ordenats per ordre decreixent
indexs_creixent = argsort(valors_Propis)  # orden creciente 
indexs_decreixent = indexs_creixent[::-1] # orden decreciente 
valors_Propis_OrdreDecreixent = valors_Propis[indexs_decreixent] # valores propios en orden decreciente

# determinar el nombre necessari de components per obtenir un 95% de variancia
valors_Propis_suma = sum(valors_Propis)
numero_components = 1
while ((sum(valors_Propis_OrdreDecreixent[:numero_components]) / valors_Propis_suma) < 0.95):
    numero_components += 1
print "Es requereixen", numero_components, "components per obtenir un", (sum(valors_Propis_OrdreDecreixent[:numero_components]) / valors_Propis_suma) * 100, "% de variancia"

llista_variables=[]
for num_variable in range(numero_components):
    llista_variables.append(indexs_decreixent[num_variable])
print "Variables seleccionades:",patients.getVariablesName(llista_variables)

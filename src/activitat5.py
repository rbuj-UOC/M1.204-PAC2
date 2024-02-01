from lib.class_patients import Patients
from numpy import *
import pylab
from sklearn.lda import LDA

def analisi_Multivariable(d):
    centroides = d.mean(0) # centroides = mitja_Aritmetica(d)
    A = d - centroides
    matriu_autocorrelacio = dot(A.T, A)
    return A, centroides, matriu_autocorrelacio

def descomposicio_Valors_Singulars(matcov):
    return linalg.eig(matcov)

print "Activitat: 5"
print

# llegir dades fitxer
patients = Patients("echocardiogram.csv")

num_variables = 7
d, myClass = patients.convertToProcessData(num_variables)

"""
    Linear Discriminant Analysis (LDA)

    Parameters
    ----------

    n_components: int
        Number of components (< n_classes - 1)

    priors : array, optional, shape = [n_classes]
        Priors on classes

    Attributes
    ----------
    `means_` : array-like, shape = [n_classes, n_features]
        Class means
    `xbar_` : float, shape = [n_features]
        Over all mean
    `priors_` : array-like, shape = [n_classes]
        Class priors (sum to 1)
    `covariance_` : array-like, shape = [n_features, n_features]
        Covariance matrix (shared by all classes)
    
    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.lda import LDA
    >>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    >>> y = np.array([1, 1, 1, 2, 2, 2])
    >>> clf = LDA()
    >>> clf.fit(X, y)
    LDA(n_components=None, priors=None)
    >>> print clf.predict([[-0.8, -1]])
[1]

See also
--------
QDA

"""
# ref: http://pydoc.net/scikit-learn/0.9/sklearn.lda
# n_samples : numero d'obserbacions
# n_features : numero de variables

print "Exercici 1..."
num_variables = 7
d, myClass = patients.convertToProcessData(num_variables)

print "Entrenament LDA ex 1..."
clf = LDA(n_components=None, priors=None)
X = asarray(d)
y = asarray(myClass)
# X_LDA = clf.fit(X, y, store_covariance=False, tol=1.0e-4).transform(X)
clf.fit(X, y, store_covariance=True, tol=1.0e-4)

print "Puntuacio:",clf.score(X,y)


print
print "Exercici 2..."
# Obtenir els valors singulars
A, centroides, matriu_autocorrelacio = analisi_Multivariable(d)
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

d_red = zeros([shape(d)[0], numero_components], float)
for i in range(shape(d)[0]):
    j=0
    for variable in range(numero_components):
        d_red[i][j] = d[i][indexs_decreixent[variable]]
        j +=1

print "Entrenament LDA ex 2..."
clf = LDA(n_components=None, priors=None)
X = asarray(d_red)
y = asarray(myClass)
#X_LDA_red = clf.fit(X, y, store_covariance=False, tol=1.0e-4).transform(X)
clf.fit(X, y, store_covariance=True, tol=1.0e-4)

print "Puntuacio:",clf.score(X,y)

from math import sqrt

def euclidean(v1, v2):
    n = len(v1)
    # Calcular la suma de quadrats dels elements comuns als dos diccionais
    sumatori_diff_quadrat = sum([(v1[i]-v2[i])**2 for i in range(n)])
    return sumatori_diff_quadrat**0.5

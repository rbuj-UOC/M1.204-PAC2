from math import sqrt

# Coeficient de Pearson entre dos diccionaris
def pearson(v1, v2):
    n = len(v1)
    # Sumatori dels elements dels vectors
    suma_valors_v1 = sum(v1)
    suma_valors_v2 = sum(v2)
    # Sumatori de les arrels
    suma_arrels_v1 = sum([elem ** 2 for elem in v1])
    suma_arrels_v2 = sum([elem ** 2 for elem in v2])
    # sumatori dels productes
    suma_productes = sum([v1[i] * v2[i] for i in range(n)])
    # Calcular r (Pearson score)
    numerador = suma_productes - (suma_valors_v1 * suma_valors_v2) / n
    denominador = sqrt((suma_arrels_v1-(suma_valors_v1 ** 2) / n) * (suma_arrels_v2-(suma_valors_v2 ** 2) / n))
    if denominador == 0:
        return 0
    return 1.0 - numerador / denominador

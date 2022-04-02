import numpy as np

def EuclideanMetrics(p1, p2, type = 'matrix'):
    """
    Function returns EuclideanDistanace between two points or two matrixes.
    Params:
        p1 - point or matrix
        p2 - point or matrix
        type - possible values: matrix or points
    """
    if type == "matrix":
        result = EuclideanMetricsMatrix(p1, p2)
    elif type == "points":
        result = EuclideanMetricsPoints(p1, p2)
    return result    

def EuclideanMetricsPoints(p1, p2):
    d = 0
    for a, b in zip(p1,p2):
        d += (a - b) ** 2
    return np.sqrt(d)

def EuclideanMetricsMatrix(A, B):
    d = []
    for i in range(B.shape[0]):
        d.append(np.sqrt((A-B[i, :]) @ (A-B[i, :]).T))
    return np.array(d)

def ManhattanMetrics(p1, p2) -> float:
    d = 0
    for a, b in zip (p1, p2):
        d += np.abs(a - b)
    return d

def CosinusMetrics(p1, p2) -> float:
    a =( p1[0] * p2[0] + p1[1] * p2[1] )/(np.linalg.norm(p1) + np.linalg.norm(p2))
    return 1 - a 
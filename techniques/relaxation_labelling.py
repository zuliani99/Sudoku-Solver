import numpy as np
from .utils import DIMENSION, getDomainCells
import copy


Rij = np.zeros((81, 9))


def defineProbabilities(dom):
    return [1/len(dom) if num+1 in dom else 0 for num in range(DIMENSION)]


def defineDistributions(domains):
    distributions = []
    for row in range(DIMENSION):
        distributions.extend(defineProbabilities(domains[row * 9 + col]) for col in range(DIMENSION))
    return distributions
    
    
def compatibility(i, j, lb, mu): #ok
    if i == j: return 0
    if lb != mu: return 1
    if sameRow(i, j) or sameCol(i, j) or sameBox(i, j): return 0
    return 1

def sameRow(i, j): return i[0] == j[0]
def sameCol(i, j): return i[1] == j[1]
def sameBox(i, j): return (i[1] // 3) == (j[1] // 3) and (i[0] // 3) == (j[0] // 3)


def computeAllQ(probDist):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            for uLabel in range(DIMENSION):
                Rij[row * 9 + col][uLabel] = computeQ(probDist, (row, col), uLabel+1)


def computeAllP(probDist):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            s = sum(np.multiply(probDist[row * 9 + col], Rij[row * 9 + col]))
            for uLabel in range(DIMENSION):
                probDist[row * 9 + col][uLabel] = (
                    (probDist[row * 9 + col][uLabel] * Rij[row * 9 + col][uLabel]) / s
                )


def computeQ(probDist, obj, lLabel):
    sum = 0
    rowObj, colObj = obj
    for col in range(DIMENSION):
        if colObj != col:
            for uLabel in range(DIMENSION):
                sum += compatibility(obj, (rowObj, col), lLabel, uLabel + 1) * probDist[rowObj * 9 + col][uLabel]

    for row in range(DIMENSION):
        if rowObj != row:
            for uLabel in range(DIMENSION):
                sum += compatibility(obj, (row, colObj), lLabel, uLabel + 1) * probDist[row * 9 + colObj][uLabel]

    for row in range((rowObj // 3) * 3, (rowObj // 3) * 3 + 3):
        for col in range((colObj // 3) * 3, (colObj // 3) * 3 + 3):
            if (row, col) != obj:
                for uLabel in range(DIMENSION):
                    sum += compatibility(obj, (row, col), lLabel, uLabel + 1) * probDist[row * 9 + col][uLabel]
    return sum


def chooseBestFittableValue(matrix, probDist):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            matrix[row][col] = probDist[row * 9 + col].index(max(probDist[row * 9 + col]))+1
    return matrix


def euclideanDistance(prodDist, oldProb):
    return np.linalg.norm(np.array(oldProb).ravel()-np.array(prodDist).ravel())


def solveRelaxationLabeling(matrix):
    domain = getDomainCells(matrix)
    probDist = defineDistributions(domain)
    diff = 1
    iterations = 0
    
    oldProb = copy.deepcopy(probDist)
    while diff > 0.001:
        computeAllQ(probDist)
        computeAllP(probDist)
        
        diff = euclideanDistance(probDist, oldProb)
        oldProb = copy.deepcopy(probDist)
        iterations += 1
        #print("Actual difference : ", diff)
        
    return chooseBestFittableValue(matrix, probDist), iterations
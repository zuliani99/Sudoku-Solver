import numpy as np
import copy

from techniques.utils import getDomainCells

qu = np.zeros((81, 9))


def define_probabilities(dom):
    list = []
    for i in range(1, 10):
        if i in dom:
            list.append(1/len(dom))
        else:
            list.append(0)
    return list


def define_distributions(domains):
    distributions = []
    for i in range(0, 9):
        for j in range(0, 9):
            distributions.append(define_probabilities(domains[i*9 + j]))

    return distributions


def compatibility(i, j, lb, mu):
    if i == j:
        return 0
    if lb != mu:
        return 1
    if valid(i, j) == 0:
        return 0
    return 1


def valid(obj1, obj2):
    if obj1[0] == obj2[0] or obj1[1] == obj2[1]:
        return 0

    if (obj1[1] // 3) == (obj2[1] // 3) and (obj1[0] // 3) == (obj2[0] // 3):
        return 0
    return 1


def compute_all_q(p):
    for i in range(0, 9):
        for j in range(0, 9):
            for u in range(1, 10):
                qu[i*9 + j][u-1] = q(p, (i, j), u)


def compute_all_p(p):
    for i in range(0, 9):
        for j in range(0, 9):
            somma = sum(np.multiply(p[i * 9 + j], qu[i * 9 + j]))
            for u in range(1, 10):
                p[i*9+j][u-1] = p[i*9+j][u-1]*qu[i*9+j][u-1]/somma


def q(p, obj, l):
    sum = 0

    #row
    for i in range(0, 9):
        if obj[1] != i:
            for u in range(1, 10):
                #print(compatibility(obj, (obj[0], i), l, u))
                #print(p[obj[0]*9 + i][u-1])
                sum += compatibility(obj, (obj[0], i), l, u) * p[obj[0]*9 + i][u-1]

    #column
    for i in range(0, 9):
        if obj[0] != i:
            for u in range(1, 10):
                sum += compatibility(obj, (i, obj[1]), l, u) * p[i * 9 + obj[1]][u-1]

    #box
    box_x = obj[1] // 3
    box_y = obj[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if (i, j) != obj:
                for u in range(1, 10):
                    sum += compatibility(obj, (i, j), l, u) * p[i*9 + j][u-1]
    return sum


def choose_values(matrix, p):
    for i in range(0, 9):
        for j in range(0, 9):
            matrix[i][j] = p[i*9+j].index(max(p[i*9+j]))+1
    return matrix


def compute_distance_euclidean(p, old_p):
    return np.linalg.norm(np.array(old_p).ravel()-np.array(p).ravel())


def solveRelaxationLabeling(matrix):
    domain = getDomainCells(matrix)
    p = define_distributions(domain)
    diff = 1
    iterations = 0
    old_p = copy.deepcopy(p)
    while diff > 0.001:
        compute_all_q(p)
        compute_all_p(p)
        diff = compute_distance_euclidean(p, old_p)
        old_p = copy.deepcopy(p)
        iterations += 1
        print("Actual difference : ", diff)

    return choose_values(matrix, p), iterations

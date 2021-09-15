from numpy import sqrt

def dist(x2, x1, y2, y1):
    return sqrt((x2-x1)**2 + (y2-y1)**2)


def xy_dist(x2, x1, y2, y1):
    return [x2-x1, y2-y1]


def dist_da_cibo(organismo, cibo):
    return dist(cibo.x, organismo.x, cibo.y, organismo.y)


def xy_dist_da_cibo(organismo, cibo):
    return xy_dist(cibo.x, organismo.x, cibo.y, organismo.y)


def dist_da_vicino(org1, org2):
    return dist(org2.x, org1.x, org2.y, org1.y)


def xy_dist_da_vicino(org1, org2):
    return xy_dist(org2.x, org1.x, org2.y, org1.y)
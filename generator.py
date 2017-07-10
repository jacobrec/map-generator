from opensimplex import OpenSimplex
from multiprocessing import Pool
from functools import partial


class Generator():
    complexity = 5

    def __init__(this, seed):
        this.gen = OpenSimplex(seed)

    def generateHeightmap(this, size, featuresize, detail):
        width = size
        height = size

        p_genColumn = partial(this.genColumn, width, height, detail, featuresize)

        with Pool() as p:
            value = list(p.map(p_genColumn, range(width)))

        return value

    def noise(this, nx, ny, scale=255):
        return int((this.gen.noise2d(nx*this.complexity, ny*this.complexity) / 2.0 + 0.5)*scale)

    def genColumn(this, width, height, detail, featuresize, x):
        col = [0]*height
        for y in range(height):
            nx = x/width - 0.5
            ny = y/height - 0.5
            a = 0
            b = 0
            for t in range(-featuresize, detail-featuresize):
                n = 2**t
                b += 1/n
                a += this.noise(n * nx, n * ny)/n
            col[y] = a/b
        return col

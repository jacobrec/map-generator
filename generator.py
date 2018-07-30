from opensimplex import OpenSimplex
from joblib import Parallel, delayed
import multiprocessing


class Generator():
    complexity = 5
    def __init__(self, seed):
        self.gen = OpenSimplex(seed)
    def generateHeightmap(self, size, featuresize, detail):
        self.width = size
        self.height = size
        self.featuresize = featuresize
        self.detail = detail

        value = Parallel(n_jobs=multiprocessing.cpu_count())(delayed(self.doRow)(y) for y in range(self.height))
        return value

    def doRow(self, y):
        val = []
        for x in range(self.width):
            nx = x/self.width - 0.5
            ny = y/self.height - 0.5
            a = 0
            b = 0
            for t in range(-self.featuresize, self.detail-self.featuresize):
                n = 2**t
                b += 1/n
                a += self.noise(n * nx, n * ny)/n
            val.append(a/b)
        return val
            

    def noise(self,nx, ny, scale = 255):
        return int((self.gen.noise2d(nx*self.complexity, ny*self.complexity) / 2.0 + 0.5)*scale)

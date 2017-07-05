from opensimplex import OpenSimplex


class Generator():
    complexity = 5
    def __init__(this, seed):
        this.gen = OpenSimplex(seed)
    def generateHeightmap(this,size, featuresize, detail):
        width = size
        height = size
        value = []
        for x in range(width):
            value.append([]);
            for y in range(height):
                value[x].append(0)


        for y in range(height):
            for x in range(width):
                nx = x/width - 0.5
                ny = y/height - 0.5
                a = 0
                b = 0
                for t in range(-featuresize,detail-featuresize):
                    n = 2**t
                    b += 1/n
                    a += this.noise(n * nx, n * ny)/n
                value[x][y] = a/b

        return value

    def noise(this,nx, ny, scale = 255):
        return int((this.gen.noise2d(nx*this.complexity, ny*this.complexity) / 2.0 + 0.5)*scale)

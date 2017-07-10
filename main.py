from generator import *
from viewer import *
import sys
import random
import threading

seed = int(random.random()*1000000)
view = VIEW_NORMAL

windowsize = 2**10
x = 7
featuresize = 2
detail = 5
shouldSave = True
size = 16

moisture = []
heights = []

generator = Generator(seed)
viewer = Viewer()

isDone = False

def main():
    global x
    global windowsize
    global seed
    global generator
    global viewer
    global featuresize

    if len(sys.argv) not in {1, 2, 3, 4}:
        print("Try the following:\nmain.py [res] [zoom] [seed]\nmain.py help")
        sys.exit(0)
    if len(sys.argv) >= 2 and sys.argv[1] == "help":
        print("main.py [res] [zoom] [seed]")
        print("The size of the image is 2^[res]")
        print("[zoom] is how close the image is, enter a value from [-3,3] you probably want something around 0. The higher the number the more zoomed in")
        print("All arguments are optional, if you enter two arguments it assumes main.py [res] [zoom] and one assumes main.py [res]")
        sys.exit(0)
    if len(sys.argv) >= 2:
        x = int(sys.argv[1])
    if len(sys.argv) >= 3:
        featuresize = int(sys.argv[2])
    if len(sys.argv) >= 4:
        seed = int(sys.argv[3])

    print("Seed: "+str(seed))
    generator = Generator(seed)

    updateRes(x)

    img = Image.new( 'RGB', (size,size), "black") # create a new black image
    pixels = img.load() # create the pixel map

    for x in range(size):
        for y in range(size):
            pixels[x,y] = hexToTriple(getColour(heights[x][y], moisture[x][y])) # set the colour accordingly

    #img.show()
    img.save('test.png')



def updateRes(newRes):
    global heights
    global moisture
    global size

    size = 2**newRes

    print("Generating maps at res("+str(x)+")")
    if view is not VIEW_MOISTURE_ONLY:
        heights = generator.generateHeightmap(size,featuresize,detail)
        print("Made height map")
    if view is not VIEW_HEIGHT_ONLY:
        moisture = generator.generateHeightmap(size,featuresize,detail)
        print("Made moisture map")



main()

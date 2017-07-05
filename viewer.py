#!/usr/bin/python

import tkinter as tk
from colors import *
from PIL import Image

VIEW_NORMAL = 0
VIEW_HEIGHT_ONLY = 1
VIEW_MOISTURE_ONLY = 2

class Viewer():
    isShowing = False
    def makeWindow(this, windowsize, size, heights, moisture, view):
        top = tk.Tk()

        this.windowsize = 2**10
        this.pixSize = int(windowsize/size)

        this.c = tk.Canvas(top, height=windowsize, width=windowsize)
        this.c.pack(expand=1,fill=tk.BOTH)

        this.heights = heights
        this.moisture = moisture
        this.view = view
        this.size = size

        this.paintScreen()


        print("Displaying")
        return top

    def paintScreen(this):
        for x in range(this.size):
            for y in range(this.size):
                if this.view == VIEW_NORMAL:
                    this.paintPoint(x*this.pixSize, y*this.pixSize,this.pixSize, getColour(this.heights[x][y], this.moisture[x][y]))
                elif this.view == VIEW_MOISTURE_ONLY:
                    this.paintPoint(x*this.pixSize, y*this.pixSize,this.pixSize, getGreyScale(this.moisture[x][y]))
                elif this.view == VIEW_HEIGHT_ONLY:
                    this.paintPoint(x*this.pixSize, y*this.pixSize,this.pixSize, getGreyScale(this.heights[x][y]))


    def paintPoint(this,x,y,pixSize=1,paint="red"):
        x1, y1 = x,y
        x2, y2 = (x + pixSize), (y + pixSize)
        this.c.create_rectangle(x1, this.windowsize-y1, x2, this.windowsize-y2, fill=paint, outline="")


    def display(this, windowsize, size, heights, moisture, view):
        print("And ", end="")
        w = this.makeWindow(windowsize,size, heights, moisture, view)
        isShowing = True
        w.mainloop()
    def saveImage(this):
        img = Image.new( 'RGB', (this.size,this.size), "black") # create a new black image
        pixels = img.load() # create the pixel map

        for x in range(this.size):
            for y in range(this.size):
                pixels[x,y] = hexToTriple(getColour(this.heights[x][y], this.moisture[x][y])) # set the colour accordingly

        #img.show()
        img.save('test.bmp')
    def updateWindow(this, size, heights, moisture, view):
        this.heights = heights
        this.moisture = moisture
        this.view = view
        this.size = size

        this.pixSize = int(this.windowsize/size)

        this.paintScreen()

class BoardHandler:
    _pixels            = None
    _width             = None
    _height            = None
    
    if constants.PI:
        import neopixel, board
        pixel_pin = board.D18
        num_pixels = width * height
        order = neopixel.GRB
        self._pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=constants.LED_BRIGHTNESS, auto_write=False,pixel_order=order)

    def drawPixel(self, x, y, color):
        if constants.PI:
            try:
                if (x>=0 and y>=0 and color >=0):
                    self._pixels[self.getPixelFromGrid(x,y)] = constants.COLORS[color]
            except:
                print(str(x) + ' --- ' + str(y))   
        else:
            pygame.draw.rect(self._DISPLAYSURF, constants.COLORS[color], (x*constants.SIZE+1, y*constants.SIZE+1, constants.SIZE-2, constants.SIZE-2))

    #helper to translate the continuous strip into a grid
    #works for following setup

    # 9 10 11
    # 8 7 6
    # 3 4 5
    # 2 1 0

    def getPixelFromGrid(self, x, y):
        if (x%2 == 0):
            y = self._height - y - 1
        return self._height*(self._width - x - 1) + y

    #blank the screen
    def clear(self):
        if constants.PI:
            self._pixels.fill((0,0,0))
        else:
            self._DISPLAYSURF.fill(constants.BGCOLOR)

    #update the leds/pixels
    def updateScreen(self):
        if constants.PI:
            self._pixels.show()
        else:
            pygame.display.update()

    #main update that gets called during the loop to update the screen
    def update(self):
        self.clear()
        self.updateScreen()

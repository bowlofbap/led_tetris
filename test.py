import time
import board
import neopixel

# Update these values to match your setup
pixel_pin = board.D18  # GPIO pin connected to the data line
num_pixels = 200  # Number of LEDs on your strip

# Create the NeoPixel object
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)

# Test the LEDs
try:
    pixels.fill((0, 0, 0))
    pixels.show()

except KeyboardInterrupt:
    # Turn off LEDs on exit
    pixels.fill((0, 0, 0))
    pixels.show()
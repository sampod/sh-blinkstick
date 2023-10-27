from blinkstick import blinkstick
import psutil
import time

bstick = blinkstick.find_first()

if bstick is None:
    print ("No BlinkSticks found...")
else:
    maxbright=32
    print ("Displaying CPU usage (Green = 0%, Amber = 50%, Red = 100%)")
    print ("Maximum brightness =", maxbright)
    print ("Press Ctrl+C to exit")

    #go into a forever loop
    while True:
        cpu = psutil.cpu_percent(interval=1)
        intensity = int(maxbright * cpu / 100)
        try:
          bstick.turn_off()
#          bstick.blink(red=0, green=0, blue=0, delay=500)
          time.sleep(0.1)
          bstick.set_color(red=intensity, green=maxbright - intensity, blue=0)
        except:
          print("An exception occurred")

import pyautogui
import math
import sys

print("PerfectCircle by shokifrend77")

# this is the size of the circle in pixels
radius = 300
# this is how many steps it will take
# greater value means greater accuracy
steps = 10000
# this is the delay between each step
# if it says "TOO SLOW" try setting this value lower
# zero is too fast
pyautogui.PAUSE = 0.00001

print("[i] Config:")
print("      radius:", radius)
print("      steps:", steps)
print("      pyautogui.PAUSE:", pyautogui.PAUSE)


# locate the center dot on the screen
print("[i] Looking for center dot...")
center = pyautogui.locateCenterOnScreen('dot.png', grayscale=True)
if not center == None:
    print("[i] Center dot found:", center[0], center[1])
else:
    print("[E] Center dot could not be found!")
    print("Tip: Try taking a screenshot of the browser and then crop it to the center dot.")
    sys.exit(1)

print("[i] Calculating positions")

# init the position lists
pos_x, pos_y = [0], [0]

# create a starting point
pos_x[0] = center[0] + (radius * math.cos(0*math.pi/180))
pos_y[0] = center[1] + (radius * math.sin(0*math.pi/180))

# loop through each step and add the positions to the lists
for angle in [(360/steps)*i for i in range(steps)]:
    pos_x.append(center[0] + (radius * math.cos(angle*math.pi/180)))
    pos_y.append(center[1] + (radius * math.sin(angle*math.pi/180)))

# sometimes it will not make a full circle, so add some end points
pos_x.append(center[0] + (radius * math.cos(0*math.pi/180)))
pos_y.append(center[1] + (radius * math.sin(0*math.pi/180)))
pos_x.append(center[0] + (radius * math.cos(1*math.pi/180)))
pos_y.append(center[1] + (radius * math.sin(1*math.pi/180)))

print("[i] Calculating all positions done!")
print("[i] Exevuting positions...")

# move the cursor to the start position
pyautogui.moveTo(pos_x[0], pos_y[0])
# press and hold the mouse button
pyautogui.mouseDown()
# loop over all positions and move the cursor to them
for i in range(0, len(pos_x)):
    pyautogui.moveTo(pos_x[i], pos_y[i])
# finally, release the mouse button
pyautogui.mouseUp

print("[i] Execution finished!")

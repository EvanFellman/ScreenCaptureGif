from pynput import mouse
from PIL import Image
import mss.tools
import keyboard
import time
import pyautogui
import os

x1, y1 = (-1, -1)
x2, y2 = (-1, -1)


print("Click the two corners of the area you would like to record.  Then press control and space to finish recording.")


def on_move(x, y):
	pass


def on_click(x, y, button, pressed):
	global x1
	global x2
	global y1
	global y2
	if button == mouse.Button.left and pressed:
		if (x1, y1) == (-1, -1):
			x1, y1 = (x, y)
		else:
			if (x2, y2) == (-1, -1):
				x2, y2 = (x, y)
				listener.stop()


def on_scroll(x, y, dx, dy):
	pass


with mouse.Listener(
	on_move=on_move,
	on_click=on_click,
	on_scroll=on_scroll) as listener:
	listener.join()

listener = mouse.Listener(
	on_move=on_move,
	on_click=on_click,
	on_scroll=on_scroll)
listener.start()

if x2 < x1:
	temp = x2
	x2 = x1
	x1 = temp
if y2 < y1:
	temp = y2
	y2 = y1
	y1 = temp

flag = True
print("\nRecording...\n\nPress control and space on me to finish recording :)")
images = []
mousePositions = []
with mss.mss() as sct:
	mon = sct.monitors[1]
monitor = {"top": y1, "left": x1, "width": (x2 - x1), "height": (y2 - y1)}
while flag:
	with mss.mss() as sct:
		mousePositions.append(pyautogui.position())
		images.append(sct.grab(monitor))
		if keyboard.is_pressed('ctrl+space'):
			flag = False
			print('Finished recording. Now making the GIF. I will close when it is done.')
		time.sleep(0.15)
for i in range(len(images)):
	temp = Image.frombytes("RGB", images[i].size, images[i].bgra, "raw", "BGRX")
	mouseImage = Image.open("data/mouse.png")
	mx, my = mousePositions[i]
	mx -= x1
	my -= y1
	temp.paste(mouseImage, (mx, my))
	images[i] = temp
flag2 = True
i = 0
while flag2:
	try:
		i += 1
		if not os.path.isfile('HereYouGo' + str(i) + '.gif'):
			images[0].save('HereYouGo' + str(i) + '.gif', save_all=True, append_images=images[1:], duration=200, loop=0)
			flag2 = False
	except Exception:
		pass

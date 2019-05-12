from pynput import mouse
from PIL import Image
import mss.tools
import keyboard
import time
import pyautogui
# import win32gui
# import win32con
# win32gui.SetWindowPos(hWnd, win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

firstPoint = (-1, -1)
secondPoint = (-1, -1)


print("click at the two corners to record at.  Then press 's' to finish recording.")


def on_move(x, y):
	pass


def on_click(x, y, button, pressed):
	global firstPoint
	global secondPoint
	if button == mouse.Button.left and pressed:
		if firstPoint == (-1, -1):
			firstPoint = (x, y)
		else:
			if secondPoint == (-1, -1):
				secondPoint = (x, y)
				listener.stop()

def on_scroll(x, y, dx, dy):
	pass


# Collect events until released
with mouse.Listener(
	on_move=on_move,
	on_click=on_click,
	on_scroll=on_scroll) as listener:
	listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
	on_move=on_move,
	on_click=on_click,
	on_scroll=on_scroll)
listener.start()

while secondPoint == (-1, -1):
	print('hi')
	pass

x1, y1 = firstPoint
x2, y2 = secondPoint

if x2 < x1:
	firstPoint = (x2, y1)
	seoncPoint = (x1, y2)
	temp = x2
	x2 = x1
	x1 = temp
if y2 < y1:
	firstPoint = (x1, y2)
	seoncPoint = (x2, y1)
	temp = y2
	y2 = y1
	y1 = temp

i = 0
flag = True
print("press 's' on me to finish recording :)")
images = []
while flag:
	with mss.mss() as sct:
		# The screen part to capture
		mon = sct.monitors[1]
		yahyeet = pyautogui.position()
		monitor = {"top": y1, "left": x1, "width": (x2 - x1), "height": (y2 - y1)}
		# Grab the data
		sct_img = sct.grab(monitor)
		screenShot = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
		mmmm = Image.open("data/mouse.png")
		ya, yeet = yahyeet
		ya -= x1
		yeet -= y1
		screenShot.paste(mmmm, (ya, yeet))
		images.append(screenShot)
		i += 1
		time.sleep(0.1)
		if keyboard.is_pressed('s'):
			flag = False
			print('Finished recording. Now making the GIF.')
try:
	images[0].save('hereYouGo.gif', save_all=True, append_images=images[1:], duration=100, loop=0)
except Exception:
	print('Failed :(')
	input()

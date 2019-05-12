from PIL import Image
import mss.tools
import keyboard
import time
import pyautogui
i = 0
flag = True
print("press 's' on me to finish recording :)")
images = []
while flag:
	with mss.mss() as sct:
		# The screen part to capture
		mon = sct.monitors[1]
		yahyeet = pyautogui.position()
		monitor = {"top": mon["top"], "left": mon["left"], "width": mon["width"], "height": mon["height"]}
		# Grab the data
		sct_img = sct.grab(monitor)
		screenShot = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
		mouse = Image.open("data/mouse.png")
		screenShot.paste(mouse, yahyeet)
		images.append(screenShot)
		i += 1
		time.sleep(0.1)
		if keyboard.is_pressed('s'):
			flag = False
images[0].save('hereYouGo.gif', save_all=True, append_images=images[1:], duration=100, loop=0)

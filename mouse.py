import pyautogui
import time
time.sleep(1)
pyautogui.hotkey("win","r")
time.sleep(0.3)
pyautogui.typewrite("RUNDLL32 USER32.DLL,SwapMouseButton", interval=0.02)
time.sleep(0.2)
pyautogui.hotkey("enter")

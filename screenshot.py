import pyautogui

screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

print("Screenshot taken successfully!")
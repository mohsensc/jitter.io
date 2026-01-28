import pyautogui
import random
import time
from pynput import mouse
from threading import Lock

# Initialize position
prev_x, prev_y = pyautogui.position()
startTime = time.time()
lastSixSecMove = 0
lastSevenSecMove = 0

# Click detection
click_detected = False
click_lock = Lock()

def on_click(x, y, button, pressed):
    global click_detected
    if pressed:  # Only trigger on mouse down
        with click_lock:
            click_detected = True

# Mouse listener
listener = mouse.Listener(on_click=on_click)
listener.start()

while True:
    current_time = time.time()
    elapsed = current_time - startTime
    
    time.sleep(0.01)
    
    # Current mouse position
    x, y = pyautogui.position()
    
    # Move every 6/7seconds
    if elapsed - lastSixSecMove >= 6:
        offset_x = random.choice([-67, 67])
        offset_y = random.choice([-67, 67])
        pyautogui.move(offset_x, offset_y, duration=0.06)
        time.sleep(0.5)
        lastSixSecMove = time.time() - startTime

    if elapsed - lastSevenSecMove >= 7:
        offset_x = random.choice([-67, 67])
        offset_y = random.choice([-67, 67])
        pyautogui.move(offset_x, offset_y, duration=0.07)
        time.sleep(0.5)
        lastSevenSecMove = time.time() - startTime
    
    # Move on click
    with click_lock:
        if click_detected:
            offset_x = random.randint(-444, 444)
            offset_y = random.randint(-444, 444)
            pyautogui.move(offset_x, offset_y, duration=0.05)
            click_detected = False
            time.sleep(0.3)
    
    # Move if mouse slowed down but not when still (user's about to click)
    if (0 < abs(x - prev_x) < 5) and (0 < abs(y - prev_y) < 5):
        offset_x = random.randint(-50, 50)
        offset_y = random.randint(-50, 50)
        pyautogui.move(offset_x, offset_y, duration=0.05)
        time.sleep(0.5)  # Cooldown
    
    if (abs(x - prev_x) == 0) and (abs( y - prev_y) == 0):
        offset_x = random.choice([-5, 5])
        offset_y = random.choice([-5, 5])
        pyautogui.move(offset_x, offset_y, duration=0.05)
        time.sleep(2)  # Cooldown
    
    # Update previous position for next iteration
    prev_x, prev_y = x, y
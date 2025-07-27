PRINTFLAG = True  # 是否打印事件
print("请按F12开始录制，再次按下结束录制。")
print('注意，无法录制快捷键，因为转义字符不会被识别为键盘的按键')

# 等待开始录制
import time
from pynput import keyboard, mouse

def on_release(key): 
    if key == keyboard.Key.f12:
        return False 

wait = keyboard.Listener(on_release=on_release)
wait.start() 
wait.join() 

# 开始录制
print('已开始录制')
startTime = time.time()
Event = []

def on_listen_press(key):
    if key == keyboard.Key.f12:
        return False
    if isinstance(key, keyboard.KeyCode):
        Event.append((time.time() - startTime, 'pressKeyCode', key.char))
    elif isinstance(key, keyboard.Key):
        Event.append((time.time() - startTime, 'pressKey', str(key)))

def on_listen_release(key):
    if isinstance(key, keyboard.KeyCode):
        Event.append((time.time() - startTime, 'releaseKeyCode', key.char))
    elif isinstance(key, keyboard.Key):
        Event.append((time.time() - startTime, 'releaseKey', str(key)))

#lastMoveTime = 0
#moveInterval = 0.1  # 移动事件的最小间隔时间
#def on_listen_move(x, y):
#    global lastMoveTime
#    if time.time() - lastMoveTime > moveInterval:  # 限制移动事件的频率
#        Event.append((time.time() - startTime, 'moveTo', (x, y)))
#        lastMoveTime = time.time()

def on_listen_scroll(x, y, dx, dy):
    Event.append((time.time() - startTime, 'scroll', (x, y, dx, dy)))

def on_listen_click(x, y, button, pressed):
    if pressed:
        Event.append((time.time() - startTime, 'pressButton', (x, y, str(button))))
    else:
        Event.append((time.time() - startTime, 'releaseButton', (x, y, str(button))))

keyRecorder = keyboard.Listener(on_press=on_listen_press, on_release=on_listen_release)
mouseRecorder = mouse.Listener(on_click=on_listen_click, on_scroll=on_listen_scroll)

mouseRecorder.start()
keyRecorder.start()

keyRecorder.join()

if mouseRecorder.running:
    mouseRecorder.stop()

print('录制结束')

# 打印录制事件
if PRINTFLAG:
    print('事件如下：')
    for event in Event:
        print(f"{event[0]:.2f}s {event[1]} {event[2]}\n")

with open('Z://python//recordAndControl_better//event.txt', 'w') as f:
    for event in Event:
        f.write(f"{event[0]:.4f} {event[1]} {event[2]}\n")
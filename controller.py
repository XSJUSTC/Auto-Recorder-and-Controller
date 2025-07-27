# 物理坐标
import ast
import time
from pynput import keyboard, mouse

# 等待
def on__release(key):
    if key == keyboard.Key.f12:
        return False

mouseController = mouse.Controller()
keyboardController = keyboard.Controller()


isReset = input("是否每次更改次数和倍率,y|n:")
resetFlag = True

while True:
    if resetFlag:
        Runtimes, speedFactor = map(float, input("输入循环次数和速度倍率: ").split())
        scale = 1.25
        Mininterval = 0.00005
        print(f'目前循环次数为{Runtimes}, 速度倍率为{speedFactor}, 坐标缩放为{scale}')
        if isReset.lower() == 'n':
            resetFlag = False
    
    print('按f12开始执行，再次按下退出执行')

    wait = keyboard.Listener(on_release=on__release)
    wait.start()
    wait.join()

    print("已开始执行")
    
    # 执行操作
    wait = keyboard.Listener(on_release=on__release)
    wait.start()
    lastActionTime = 0.0

    Rt = Runtimes
    while Rt>0 and wait.running:
        Rt -= 1
        averageInterval =  0
        actionCount = 0
        with open('event.txt', 'r') as f:
            while wait.running and (line:=f.readline()) != '':
                timestamp, action, args = line.strip().split(maxsplit=2)
                timestamp = float(timestamp)
                interval = (timestamp - lastActionTime) / speedFactor
                if interval < Mininterval:
                    interval = Mininterval
                time.sleep(interval)
                averageInterval += interval
                actionCount += 1

                match action:
                    case 'scroll':
                        x, y, _, dy = ast.literal_eval(args)
                        #time.sleep(Mininterval)
                        mouseController.position = (x / scale, y / scale)
                        #time.sleep(Mininterval)
                        mouseController.scroll(dy)
                        lastActionTime = timestamp
                    case 'pressButton':
                        x, y, buttonStr = ast.literal_eval(args)
                        #time.sleep(Mininterval)
                        mouseController.position = (x / scale, y / scale)
                        #time.sleep(Mininterval)
                        _, name = buttonStr.split('.')
                        name = getattr(mouse.Button, name)
                        mouseController.press(name)
                        lastActionTime = timestamp
                    case 'releaseButton':
                        x, y, buttonStr = ast.literal_eval(args)
                        #time.sleep(Mininterval)
                        mouseController.position = (x / scale, y / scale)
                        #time.sleep(Mininterval)
                        _, name = buttonStr.split('.')
                        name = getattr(mouse.Button, name)
                        mouseController.release(name)
                        lastActionTime = timestamp
                    case 'clickButton':
                        x, y, buttonStr = ast.literal_eval(args)
                        #time.sleep(Mininterval)
                        mouseController.position = (x / scale, y / scale)
                        #time.sleep(Mininterval)
                        _, name = buttonStr.split('.')
                        name = getattr(mouse.Button, name)
                        mouseController.click(name)
                        lastActionTime = timestamp
                    case 'pressKey' | 'pressKeyCode':
                        if action == 'pressKey':
                            _, key = args.split('.')
                            key = getattr(keyboard.Key, key)
                        elif action == 'pressKeyCode':
                            key = keyboard.KeyCode(char=args)
                        keyboardController.press(key)
                        lastActionTime = timestamp
                    case 'releaseKey' | 'releaseKeyCode':
                        if action == 'releaseKey':
                            _, key = args.split('.')
                            key = getattr(keyboard.Key, key)
                        elif action == 'releaseKeyCode':
                            key = keyboard.KeyCode(char=args)
                        keyboardController.release(key)
                        lastActionTime = timestamp
                if actionCount <= 0:
                    actionCount = 1
                time.sleep(averageInterval / actionCount)

    print('执行完毕')
                




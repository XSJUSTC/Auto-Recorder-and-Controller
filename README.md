# Auto-Recorder-and-Controller 录屏与执行之脚本
An automation script written in Python using pynput - my beginner project. So it might be not very easy to use, but this guide is here to help you get started

这是一个用Python的pynput写的自动化脚本，也是我的入门代码。因此您用起来可能并不方便，本文将起到一定帮助。

### Python
Fisrt, make sure you have python installed, along with the `pynput` library.To install `pynput`, you can use the following command:

首先确保您安装了python及pynput库. 后者可以使用以下指令安装.

```bash
pip install pynput
```

### recorder.py

Due to limited technical skill, this script does not support recording hotkeys. If you really want to simulate hotkey combinations, please manually add them to `event.txt`.

因为技术力不足，本脚本不支持记录热键。如果你需要模拟热键，请手动在`event.txt`中添加。

### event.txt

Recorded actions will be stored here. You can freely edit this file if you want to change the recorded sequence.

您的被录制的操作将会存在其中，您可直接修改其中的操作。

### controller.py

Before your first use, open this file and adjust the coordinate scaling ratio to match your PC settings.

在第一次使用前，请先打开文件并将其中的坐标缩放倍率调整为与您的电脑设置保持一致。

If Chinese charactors are not displayed correctly, try changing your terminal's character encoding to GBK. 

如果中文字符不能正确显示，尝试将终端字符编码改为GBK。

You can also choose whether to re-enter the repeat count and speed multiplier each time you resume after pausing the script.

你可以选择每次暂停后，继续执行时是否重新输入循环次数和运行速度倍率。


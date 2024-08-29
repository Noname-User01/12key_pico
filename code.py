import board
import digitalio
import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

print("import set")
# キーボードオブジェクトを作成
keyboard = Keyboard(usb_hid.devices)
print("key object set")
# 各ボタンのピンを設定
button0 = digitalio.DigitalInOut(board.GP0)
button0.direction = digitalio.Direction.INPUT
button0.pull = digitalio.Pull.UP

button1 = digitalio.DigitalInOut(board.GP1)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.GP2)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

button3 = digitalio.DigitalInOut(board.GP3)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.UP

button4 = digitalio.DigitalInOut(board.GP4)
button4.direction = digitalio.Direction.INPUT
button4.pull = digitalio.Pull.UP

button5 = digitalio.DigitalInOut(board.GP5)
button5.direction = digitalio.Direction.INPUT
button5.pull = digitalio.Pull.UP

button6 = digitalio.DigitalInOut(board.GP6)
button6.direction = digitalio.Direction.INPUT
button6.pull = digitalio.Pull.UP

button7 = digitalio.DigitalInOut(board.GP7)
button7.direction = digitalio.Direction.INPUT
button7.pull = digitalio.Pull.UP

button8 = digitalio.DigitalInOut(board.GP8)
button8.direction = digitalio.Direction.INPUT
button8.pull = digitalio.Pull.UP

button9 = digitalio.DigitalInOut(board.GP9)
button9.direction = digitalio.Direction.INPUT
button9.pull = digitalio.Pull.UP

button10 = digitalio.DigitalInOut(board.GP10)
button10.direction = digitalio.Direction.INPUT
button10.pull = digitalio.Pull.UP

button11 = digitalio.DigitalInOut(board.GP11)
button11.direction = digitalio.Direction.INPUT
button11.pull = digitalio.Pull.UP

print("switch set")
led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT
print("LED set")


fg_sleep = True
fg_1 = True
fg_2 = True
fg_3 = True
fg_4 = True
fg_5 = True
fg_6 = True
fg_7 = True
fg_8 = True
fg_9 = True
fg_10 = True
fg_11 = True
bt5_num = 0
bt8_num = 0
window = 0
mute_LED = 0
LED_num = 0
print("flag set")
print("-----start switch-----")

# writeを使う為の関数
def type_string(string):
    for char in string:
        keycode = getattr(Keycode, char.upper())
        keyboard.press(keycode)


        keyboard.release(keycode)
        time.sleep(0.1)

while True:
    # スリープ
    if not button0.value:  # ボタン0が押された場合
        print("0")
    else:
        if fg_sleep == False:

            fg_sleep = True

    # ---------9key start---------
    # soundデバイス変更
    if not button1.value:  # ボタン1が押された場合
        keyboard.press(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.F7)
        led.value = True  # LEDをオン
        print("1")
    else:
        keyboard.release(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.F7)

    if not button2.value:  # ボタン2が押された場合
        keyboard.press(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.F11)
        print("2")
    else:
        keyboard.release(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.F11)

    # コードの保存
    if not button3.value:  # ボタン3が押された場合
        keyboard.press(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.M)
        print("3")
    else:
        keyboard.release(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.M)

    if not button4.value:  # ボタン4が押された場合
        #keyboard.press(Keycode.LEFT_CONTROL, Keycode.S)
        print("4")
    else:
        #keyboard.release(Keycode.LEFT_CONTROL, Keycode.S)
        pass

    if not button5.value:  # ボタン5が押された場合
        if bt5_num == 0:
            keyboard.press(Keycode.WINDOWS)
            keyboard.press(Keycode.D)
            bt5_num += 1
            time.sleep(0.1)
            print("5")
        else:
            pass

    else:
        keyboard.release(Keycode.WINDOWS, Keycode.D)
        bt5_num = 0

    # 作業ウィンドウの移動
    if not button6.value:  # ボタン6が押された場合
        print("6")
        if window == 1:  # 三番目
            keyboard.press(Keycode.LEFT_CONTROL, Keycode.WINDOWS, Keycode.LEFT_ARROW)
            print("→")
        elif window == 0:  # 最初に引っ掛かる
            keyboard.press(Keycode.LEFT_CONTROL, Keycode.WINDOWS, Keycode.RIGHT_ARROW)
            print("←")
        fg_6 = False
    else:
        if window == 1 and fg_6 == False:  # 4番目
            keyboard.release(Keycode.LEFT_CONTROL, Keycode.WINDOWS, Keycode.LEFT_ARROW)
            window = 0
            print("D→")
            fg_6 = True
        if window == 0 and fg_6 == False:  # 二番目
            keyboard.release(Keycode.LEFT_CONTROL, Keycode.WINDOWS, Keycode.RIGHT_ARROW)
            window = 1
            print("D←")
            fg_6 = True

    #
    if not button7.value:  # ボタン7が押された場合
        keyboard.press(Keycode.WINDOWS, Keycode.R)
        print("7")
        fg_7 = False
    else:
        if fg_7 == False:
            keyboard.release(Keycode.WINDOWS, Keycode.R)
            time.sleep(0.03)
            type_string("cmd")
            time.sleep(0.07)
            keyboard.press(Keycode.ENTER)
            keyboard.release(Keycode.ENTER)
            fg_7 = True

    # Discord ミュートボタン -----ミュート時はライトを点灯させる-----
    if not button8.value:  # ボタン8が押された場合
        keyboard.release(Keycode.LEFT_ALT, Keycode.TAB)
        # 基本ここを通る
        if bt8_num == 0:
            bt8_num += 1
            keyboard.release(Keycode.LEFT_ALT, Keycode.TAB)
            keyboard.press(Keycode.WINDOWS, Keycode.ONE)
            time.sleep(0.2)
            keyboard.release(Keycode.WINDOWS, Keycode.ONE)
            keyboard.release(Keycode.LEFT_ALT, Keycode.TAB)
            print("8")
            # LED消す
            if mute_LED == 1:
                LED_num += 1
                print("cccccccccc")
                led.value = False
                mute_LED = 0
                fg_8 = False

        else:
            # あくまでも保険のrelease
            keyboard.release(Keycode.LEFT_ALT, Keycode.TAB)
        keyboard.release(Keycode.LEFT_ALT, Keycode.TAB)
        fg_8 = False
    else:
        if fg_8 == False:
            time.sleep(0.1)
            keyboard.release(Keycode.WINDOWS, Keycode.ONE)
            keyboard.release(Keycode.LEFT_ALT, Keycode.TAB)
            print("離す")
            keyboard.press(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.M)
            keyboard.release(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.M)
            keyboard.release(Keycode.LEFT_ALT, Keycode.TAB)
            print("消す")
            keyboard.press(Keycode.LEFT_ALT, Keycode.TAB)
            keyboard.release(Keycode.LEFT_ALT, Keycode.TAB)
            bt8_num = 0
            # LEDつける
            print("out_LED_num:",LED_num)
            if mute_LED == 0 and fg_8 == False:
                print("in_LED_num:",LED_num)
                if LED_num % 2 == 0:
                    keyboard.release(Keycode.LEFT_ALT, Keycode.TAB)
                    mute_LED = 1
                    led.value = True
                    print("1ccccccccc")
                    keyboard.release(Keycode.LEFT_ALT, Keycode.TAB)
                elif LED_num % 2 == 1:
                    keyboard.release(Keycode.LEFT_ALT, Keycode.TAB)
                    mute_LED = 1
                    print("c2cccccccc")
                    keyboard.release(Keycode.LEFT_ALT, Keycode.TAB)
            fg_8 = True

    if not button9.value:  # ボタン9が押された場合
        keyboard.press(Keycode.LEFT_SHIFT, Keycode.T, Keycode.WINDOWS)
        print("9")
    else:
        keyboard.release(Keycode.LEFT_SHIFT, Keycode.T, Keycode.WINDOWS)

    # ---------9key end---------

    if not button10.value:  # ボタン0が押された場合
        keyboard.press(Keycode.WINDOWS, Keycode.X)
        keyboard.release(Keycode.WINDOWS, Keycode.X)
        fg_10 = False
        print("10")
    else:
        if fg_sleep == False:
            time.sleep(0.2)
            keyboard.release(Keycode.WINDOWS, Keycode.X)
            keyboard.press(Keycode.U)
            keyboard.release(Keycode.U)
            #keyboard.press(Keycode.S)
            #keyboard.release(Keycode.S)
            fg_10 = True




    if not button11.value:  # ボタン11が押された場合
        keyboard.press(Keycode.LEFT_CONTROL, Keycode.ONE)
        print("11")
    else:
        keyboard.release(Keycode.LEFT_CONTROL, Keycode.ONE)


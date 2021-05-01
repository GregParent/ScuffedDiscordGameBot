from pynput.keyboard import Controller, Key
import time

keyboard = Controller()


def sendInput(input):
    time.sleep(2)
    inputCharacter = input.lower()
    if inputCharacter == "start":
        keyboard.press(Key.enter)
    if inputCharacter == "select":
        keyboard.press(Key.shift_r)
    if inputCharacter == 'f1':  # RetroArch Menu button
        keyboard.press('Key.f1')
    if inputCharacter == 'up':
        keyboard.type('w')
    if inputCharacter == 'left':
        keyboard.type('a')
    if inputCharacter == 'down':
        keyboard.type('s')
    if inputCharacter == 'right':
        keyboard.type('d')

    if inputCharacter == 'a':  # A button
        keyboard.type('6')
    if inputCharacter == 'b':  # B button
        keyboard.type('2')
    if inputCharacter == 'x':  # X button
        keyboard.type('8')
    if inputCharacter == 'y':  # Y button
        keyboard.type('4')

    if inputCharacter == 'l1':  # L1 button
        keyboard.type('7')
    if inputCharacter == 'l2':  # R1 button
        keyboard.type('9')
    if inputCharacter == 'l2':  # L2 button
        keyboard.type('o')
    if inputCharacter == 'r2':  # R2 button
        keyboard.type('p')
    if inputCharacter == 'l3':  # L3 button
        keyboard.type('k')
    if inputCharacter == 'r3':  # R3 button
        keyboard.type('l')

    if inputCharacter == 'anu':  # Analog Up button
        keyboard.type('b')
    if inputCharacter == 'and':  # Analog Down button
        keyboard.type('n')
    if inputCharacter == 'anl':  # Analog Left button
        keyboard.type('m')
    if inputCharacter == 'anr':  # Analog Right button
        keyboard.type(',')


sendInput("start")

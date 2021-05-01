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
    if inputCharacter == 'w':
        keyboard.type('w')
    if inputCharacter == 'a':
        keyboard.type('a')
    if inputCharacter == 's':
        keyboard.type('s')
    if inputCharacter == 'd':
        keyboard.type('d')
    if inputCharacter == '6':  # A button
        keyboard.type('6')
    if inputCharacter == '2':  # B button
        keyboard.type('2')
    if inputCharacter == '8':  # X button
        keyboard.type('8')
    if inputCharacter == '4':  # Y button
        keyboard.type('4')
    if inputCharacter == '7':  # L1 button
        keyboard.type('7')
    if inputCharacter == '9':  # R1 button
        keyboard.type('9')


sendInput("start")
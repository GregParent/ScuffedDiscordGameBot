from pynput.keyboard import Controller, Key
import time
import pyautogui
import pydirectinput
keyboard = Controller()


def sendInput(input):
    inputCharacter = input.lower()
    if inputCharacter == "start":
        pydirectinput.press('enter')
    if inputCharacter == "select":
        pydirectinput.press('shiftright')
    if inputCharacter == 'f1':  # RetroArch Menu button
        pydirectinput.press('f1')
    if inputCharacter == 'up':
        pydirectinput.press('w')
    if inputCharacter == 'left':
        pydirectinput.press('a')
    if inputCharacter == 'down':
        pydirectinput.press('s')
    if inputCharacter == 'right':
        pydirectinput.press('d')

    if inputCharacter == 'a':  # A button
        pydirectinput.press('6')
    if inputCharacter == 'b':  # B button
        pydirectinput.press('2')
    if inputCharacter == 'x':  # X button
        pydirectinput.press('8')
    if inputCharacter == 'y':  # Y button
        pydirectinput.press('4')

    if inputCharacter == 'l1':  # L1 button
        pydirectinput.press('7')
    if inputCharacter == 'l2':  # R1 button
        pydirectinput.press('9')
    if inputCharacter == 'l2':  # L2 button
        pydirectinput.press('o')
    if inputCharacter == 'r2':  # R2 button
        pydirectinput.press('p')
    if inputCharacter == 'l3':  # L3 button
        pydirectinput.press('k')
    if inputCharacter == 'r3':  # R3 button
        pydirectinput.press('l')

    if inputCharacter == 'anu':  # Analog Up button
        pydirectinput.press('b')
    if inputCharacter == 'and':  # Analog Down button
        pydirectinput.press('n')
    if inputCharacter == 'anl':  # Analog Left button
        pydirectinput.press('m')
    if inputCharacter == 'anr':  # Analog Right button
        pydirectinput.press(',')


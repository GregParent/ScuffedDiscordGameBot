from pynput.keyboard import Controller

keyboard = Controller()


def sendInput(input):
    inputCharacter = input.lower()

    if inputCharacter == 'w' or inputCharacter == 'W':
        keyboard.type('w')
    if inputCharacter == 'a' or inputCharacter == 'A':
        keyboard.type('a')
    if inputCharacter == 's' or inputCharacter == 'S':
        keyboard.type('s')
    if inputCharacter == 'd' or inputCharacter == 'D':
        keyboard.type('d')
    if inputCharacter == '6':  # A button
        keyboard.type('6')
    if inputCharacter == '2':  # B button
        keyboard.type('2')
    if inputCharacter == '8':  # X button
        keyboard.type('8')
    if inputCharacter == '4':  # Y button
        keyboard.type('4')

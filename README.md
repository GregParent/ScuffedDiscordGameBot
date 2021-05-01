# 60FPS Emu Discord Bot
This bot was created for Systemshacks 2021: Scuffedhacks Hackathon!
The main goal was to create something scuffed, and so we decided to make a
bot that would allow you to play emulator games on Discord in a scuffed way 
that includes typing controls and delayed screenshots!

Please don't make fun the source code, it finished in less than a day...

## How to setup
This app was created for Windows only in mind, and as such you must download a
copy of Retroarch portable, and put its contents in a folder named "retroarch"
in the same level as main.py, and you may put the games anywhere.

Before launching main.py, you should set up the cores and games, as the script
will automatically navigate to the "History" tab in Retroarch to have an easy list
of games.

Set up the controls in Retroarch as follows:

Retroarch Control | Keyboard Control
----------------- | --------------
Start | Enter
Select | Right Shift
Up | W
Left | A
Down | S
Right | D
A | 6
B | 2
X | 8
Y | 4
L1 | 7
R1 | 9
L2 | O
R2 | P
L3 | K
R3 | L
Left Analog Up | B
Left Analog Left | M
Left Analog Down | N
Left Analog Right | ,

## Discord Commands
```The controls for the Emulator are:
Start emulator = emuStart
Stop emulator = emuStop
Open RetroArch menu = F1
START = start
SELECT = select

D-PAD UP = UP
D-PAD DOWN = DOWN
D-PAD LEFT = LEFT
D-PAD RIGHT = RIGHT

A-BUTTON = A
B-BUTTON = B
X-BUTTON = X
Y-BUTTON = Y

L1 = L1
R1 = R1
L2 = L2
R2 = R2
L3 = L3
R3 = R3

ANALOG UP = ANU
ANALOG DOWN = AND
ANALOG LEFT = ANL
ANALOG RIGHT = ANR
```
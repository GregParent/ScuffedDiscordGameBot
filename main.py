# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import asyncio
import io

import discord
import json
import os
import subprocess
import threading
import time

from PIL import ImageGrab
import win32gui
from discord.ext import tasks
from input import sendInput
from retroarchpythonapi import RetroArchPythonApi as RetroAPI

client = discord.Client()

retroarchOpen = False
retroarchProcess = None

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global retroarchOpen
    global retroarchProcess

    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$startGame'):
        response = "Starting game" + message.content[10::1]
        await message.channel.send(response)

    if message.content.startswith('emuStart'):
        if retroarchOpen:
            await message.channel.send('Retroarch was already started!')
        else:
            retroarchProcess = subprocess.Popen('./retroarch/retroarch.exe')
            if process_exists('retroarch.exe'):
                retroarchOpen = True

                time.sleep(1)  # navigate to the history menu for easy game access
                sendInput("left")
                sendInput("down")
                sendInput("down")
                sendInput("down")
                sendInput("right")

                send_screenshot.start(message.channel)  # start the screenshot thread
                await message.channel.send('Started Retroarch!')
            else:
                await message.channel.send('Retroarch was not started...')

    if message.content.startswith('emuStop'):
        if retroarchOpen:
            retroarchProcess.terminate()
            send_screenshot.stop()
            retroarchOpen = False
            await message.channel.send('Stopped Retroarch!')
        else:
            await message.channel.send('No Retroarch process to stop...')

    if message.content.lower().startswith('start') and retroarchOpen:
        sendInput("start")
    if message.content.lower().startswith('select') and retroarchOpen:
        sendInput("select")
    if message.content.lower().startswith('up') and retroarchOpen:
        sendInput("up")
    if message.content.lower().startswith('down') and retroarchOpen:
        sendInput("down")
    if message.content.lower().startswith('left') and retroarchOpen:
        sendInput("left")
    if message.content.lower().startswith('right') and retroarchOpen:
        sendInput("right")
    if message.content.lower().startswith('a') and retroarchOpen:
        sendInput("a")
    if message.content.lower().startswith('b') and retroarchOpen:
        sendInput("b")
    if message.content.lower().startswith('x') and retroarchOpen:
        sendInput("x")
    if message.content.lower().startswith('y') and retroarchOpen:
        sendInput("y")
    if message.content.lower().startswith('l1') and retroarchOpen:
        sendInput("l1")
    if message.content.lower().startswith('r1') and retroarchOpen:
        sendInput("r1")
    if message.content.lower().startswith('l2') and retroarchOpen:
        sendInput("l2")
    if message.content.lower().startswith('r2') and retroarchOpen:
        sendInput("r2")
    if message.content.lower().startswith('l3') and retroarchOpen:
        sendInput("l3")
    if message.content.lower().startswith('r3') and retroarchOpen:
        sendInput("r3")
    if message.content.lower().startswith('anu') and retroarchOpen:
        sendInput("anu")
    if message.content.lower().startswith('and') and retroarchOpen:
        sendInput("and")
    if message.content.lower().startswith('anl') and retroarchOpen:
        sendInput("anl")
    if message.content.lower().startswith('anr') and retroarchOpen:
        sendInput("anr")

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())


@tasks.loop(seconds=1.0)
async def send_screenshot(channel):
    # take a screenshot and save to disk
    toplist, winlist = [], []

    def enum_cb(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

    win32gui.EnumWindows(enum_cb, toplist)

    retroarch = [(hwnd, title) for hwnd, title in winlist if 'retroarch' in title.lower()]
    # just grab the hwnd for first window matching retroarch
    retroarch = retroarch[0]
    hwnd = retroarch[0]

    # win32gui.SetForegroundWindow(hwnd)
    bbox = win32gui.GetWindowRect(hwnd)
    img = ImageGrab.grab(bbox)
    arr = io.BytesIO()
    img.save(arr, format='PNG')
    arr.seek(0)
    file = discord.File(arr, 'a.png')
    # send screenshot to channel
    message = await channel.send(file=file)
    await asyncio.sleep(1)
    await message.delete()

with open('token.json') as json_file:
    token_json = json.load(json_file)
    token = token_json['token']
client.run(token)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

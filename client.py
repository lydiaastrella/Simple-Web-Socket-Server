#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import time
import hashlib

async def hello():
    #uri = "ws://f3439234.ngrok.io"
    uri = "ws://localhost:8080"
    async with websockets.connect(uri) as websocket:
        #name = input("What's your name? ")

        await websocket.send("!echo Hallo1")

        name = input("What's your name? ")

        await websocket.send("!echo Hallo2")

        name = input("What's your name? ")

        await websocket.send("!echo Hallo3")

        name = input("What's your name? ")

        await websocket.send("!echo Lorem ipsum consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit. Etiam feugiat ipsum malesuada dui pulvinar, non rhoncus arcu faucibus. Pellentesque aliquam ex mollis blandit aliquam. Proin accumsan urna ac enim aliquet, quis fringilla sapien convallis. Nam fermentum felis eget nibh ullamcorper pretium. Nullam tincidunt lacus id bibendum aliquam.!echo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit. Etiam feugiat ipsum malesuada dui pulvinar, non rhoncus arcu faucibus. Pellentesque aliquam ex mollis blandit aliquam. Proin accumsan urna ac enim aliquet, quis fringilla sapien convallis. Nam fermentum felis eget nibh ullamcorper pretium. Nullam tincidunt lacus id bibendum aliquam.!echo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit. Etiam feugiat ipsum malesuada dui pulvinar, non rhoncus arcu faucibus. Pellentesque aliquam ex mollis blandit aliquam. Proin accumsan urna ac enim aliquet, quis fringilla sapien convallis. Nam fermentum felis eget nibh ullamcorper pretium. Nullam tincidunt lacus id bibendum aliquam.!echo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit. Etiam feugiat ipsum malesuada dui pulvinar, non rhoncus arcu faucibus. Pellentesque aliquam ex mollis blandit aliquam. Proin accumsan urna ac enim aliquet, quis fringilla sapien convallis. Nam fermentum felis eget nibh ullamcorper pretium. Nullam tincidunt lacus id bibendum aliquam.!echo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit. Etiam feugiat ipsum malesuada dui pulvinar, non rhoncus arcu faucibus. Pellentesque aliquam ex mollis blandit aliquam. Proin accumsan urna ac enim aliquet, quis fringilla sapien convallis. Nam fermentum felis eget nibh ullamcorper pretium. Nullam tincidunt lacus id bibendum aliquam.!echo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit.")

        name = input("What's your name? ")

        await websocket.send("!echo Lorem ipsum consectetnt lacus id bibendum aliquam.!echo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit. Etiam feugiat ipsum malesuada dui pulvinar, non rhoncus arcu faucibus. Pellentesque aliquam ex mollis blandit aliquam. Proin accumsan urna ac enim aliquet, quis fringilla sapien convallis. Nam fermentum felis eget nibh ullamcorper pretium. Nullam tincidunt lacus id bibendum aliquam.!echo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit. Etiam feugiat ipsum malesuada dui pulvinar, non rhoncus arcu faucibus. Pellentesque aliquam ex mollis blandit aliquam. Proin accumsan urna ac enim aliquet, quis fringilla sapien convallis. Nam fermentum felis eget nibh ullamcorper pretium. Nullam tincidunt lacus id bibendum aliquam.!echo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit. Etiam feugiat ipsum malesuada dui pulvinar, non rhoncus arcu faucibus. Pellentesque aliquam ex mollis blandit aliquam. Proin accumsan urna ac enim aliquet, quis fringilla sapien convallis. Nam fermentum felis eget nibh ullamcorper pretium. Nullam tincidunt lacus id bibendum aliquam.!echo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit. Etiam feugiat ipsum malesuada dui pulvinar, non rhoncus arcu faucibus. Pellentesque aliquam ex mollis blandit aliquam. Proin accumsan urna ac enim aliquet, quis fringilla sapien convallis. Nam fermentum felis eget nibh ullamcorper pretium. Nullam tincidunt lacus id bibendum aliquam.!echo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit. Etiam feugiat ipsum malesuada dui pulvinar, non rhoncus arcu faucibus. Pellentesque aliquam ex mollis blandit aliquam. Proin accumsan urna ac enim aliquet, quis fringilla sapien convallis. Nam fermentum felis eget nibh ullamcorper pretium. Nullam tincidunt lacus id bibendum aliquam.!echo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit. Etiam feugiat ipsum malesuada dui pulvinar, non rhoncus arcu faucibus. Pellentesque aliquam ex mollis blandit aliquam. Proin accumsan urna ac enim aliquet, quis fringilla sapien convallis. Nam fermentum felis eget nibh ullamcorper pretium. Nullam tincidunt lacus id bibendum aliquam.!echo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit. Etiam feugiat ipsum malesuada dui pulvinar, non rhoncus arcu faucibus. Pellentesque aliquam ex mollis blandit aliquam. Proin accumsan urna ac enim aliquet, quis fringilla sapien convallis. Nam fermentum felis eget nibh ullamcorper pretium. Nullam tincidunt lacus id bibendum aliquam.!echo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit. Etiam feugiat ipsum malesuada dui pulvinar, non rhoncus arcu faucibus. Pellentesque aliquam ex mollis blandit aliquam. Proin accumsan urna ac enim aliquet, quis fringilla sapien convallis. Nam fermentum felis eget nibh ullamcorper pretium. Nullam tincidunt lacus id bibendum aliquam.!echo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit. Etiam feugiat ipsum malesuada dui pulvinar, non rhoncus arcu faucibus. Pellentesque aliquam ex mollis blandit aliquam. Proin accumsan urna ac enim aliquet, quis fringilla sapien convallis. Nam fermentum felis eget nibh ullamcorper pretium. Nullam tincidunt lacus id bibendum aliquam.!echo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit. Etiam feugiat ipsum malesuada dui pulvinar, non rhoncus arcu faucibus. Pellentesque aliquam ex mollis blandit aliquam. Proin accumsan urna ac enim aliquet, quis fringilla sapien convallis. Nam fermentum felis eget nibh ullamcorper pretium. Nullam tincidunt lacus id bibendum aliquam.!echo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit. Etiam feugiat ipsum malesuada dui pulvinar, non rhoncus arcu faucibus. Pellentesque aliquam ex mollis blandit aliquam. Proin accumsan urna ac enim aliquet, quis fringilla sapien convallis. Nam fermentum felis eget nibh ullamcorper pretium. Nullam tincidunt lacus id bibendum aliquam.!echo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit. Etiam feugiat ipsum malesuada dui pulvinar, non rhoncus arcu faucibus. Pellentesque aliquam ex mollis blandit aliquam. Proin accumsan urna ac enim aliquet, quis fringilla sapien convallis. Nam fermentum felis eget nibh ullamcorper pretium. Nullam tincidunt lacus id bibendum aliquam.!echo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit. Etiam feugiat ipsum malesuada dui pulvinar, non rhoncus arcu faucibus. Pellentesque aliquam ex mollis blandit aliquam. Proin accumsan urna ac enim aliquet, quis fringilla sapien convallis. Nam fermentum felis eget nibh ullamcorper pretium. Nullam tincidunt lacus id bibendum aliquam.!echo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit. Etiam feugiat ipsum malesuada dui pulvinar, non rhoncus arcu faucibus. Pellentesque aliquam ex mollis blandit aliquam. Proin accumsan urna ac enim aliquet, quis fringilla sapien convallis. Nam fermentum felis eget nibh ullamcorper pretium. Nullam tincidunt lacus id bibendum aliquam.!echo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed facilisis augue. Nunc eu pharetra elit. Etiam feugiat ipsum malesuada dui pulvinar, non rhoncus arcu faucibus. Pellentesque aliquam ex mollis blandit aliquam. Proin accumsan urna ac enim aliquet, quisfringilla sapien convallis. Nam fermentum felis eget nibh ullamcorper pretium.")
        
        name = input("What's your name? ")

        await websocket.send("!submission")

        # print(f"> {name}")

        greeting = await websocket.recv()
        time.sleep(5)
        print(f"< {greeting}")

        await websocket.send("!submission")
        # print(f"> {name}")

        greeting = await websocket.recv()
        fileA = open("teste.zip",'wb')
        fileA.write(greeting)
        fileA.close()
        time.sleep(5)
        
        pong_waiter = await websocket.ping()
        time.sleep(5)
        print(f"< {pong_waiter}")
        
        await websocket.send(greeting)
        # print(f"> {name}")

        greeting = await websocket.recv()
        time.sleep(5)
        print(f"< {greeting}")
        

asyncio.get_event_loop().run_until_complete(hello())


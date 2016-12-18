# -*- coding: latin-1 -*-
import os
import sys
import math
import pygame as pg

import time
current_milli_time = lambda: ((time.time() * 1000))

from gameplay import SpectreGameplay

os.environ["SDL_VIDEODRIVER"] = "dummy"



#init gameplay
game = SpectreGameplay()
sounds = []

class Control(object):
    def __init__(self):
        self.done = False
        self.lastTime = current_milli_time()
		
    def event_loop(self):
        for event in pg.event.get(): 
            if event.type == pg.QUIT: 
                self.done  = True 
            elif event.type == pg.KEYDOWN: 
                print("touche")
                if event.key == pg.K_s: 
                    print("Start")
                    sounds[0].play()
                    game.startNewRandomSpectre()
                if event.key == pg.K_ESCAPE: 
                    self.done = True 

    def update(self):
	dt = current_milli_time() - self.lastTime
        self.lastTime = current_milli_time()
        game.update(dt)
	#print(dt)

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.update()


if __name__ == "__main__":
    global sounds
    pg.mixer.init()
    pg.mixer.pre_init(44100, -16, 2, 2048)
    pg.init()
    screen = pg.display.set_mode((1,1))

    
    sounds.append(pg.mixer.Sound('sound/on-off.wav'))

    gameLoop = Control()
    gameLoop.main_loop()
    
    pg.quit()
    sys.exit()


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

class Control(object):
    def __init__(self):
        self.done = False
        self.lastTime = current_milli_time()
		
    def event_loop(self):
        for event in pg.event.get(): 
            if event.type == pg.QUIT: 
                self.done  = True 
            elif event.type == pg.KEYDOWN: 
                print("touch")
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

    pg.init()

    gameLoop = Control()
    gameLoop.main_loop()
    
    pg.quit()
    sys.exit()

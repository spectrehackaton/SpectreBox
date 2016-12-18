import urllib
import json
import random
import subprocess
from subprocess import Popen
import string
import sys
sys.dont_write_bytecode = True

from firebase import firebase
FirebaseAddres = "https://spectre-e5ff7.firebaseio.com/"
firebase = firebase.FirebaseApplication(FirebaseAddres,authentication=None)

from arduio import ArduinoIO
io = ArduinoIO()

SOUND_CMD = "aplay"
SOUND_PATH = "sound/"

def playSound(path):
    print("playing : "+path)
    Popen([SOUND_CMD , SOUND_PATH + path.lower()])
    
class Color:
    def decode(self, dic):
        self.r = dic["r"]
        self.g = dic["g"]
        self.b = dic["b"]
    def __init__(self):
        self.r = 255
        self.g = 255
        self.b = 255
    def set(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
class SpectreGameplay:
    def __init__(self):
        print("init Game Engine")
        self.spectres = []

        self.retrieveSpectre()
        self.timer = 0
        self.challengeCount = 0
        self.currentSeq = None
        #spectres.append(Spectre("Casper", "red", 1, 1))
        
    def getCurrentSeq(self):
        return self.currentSeq

    def retrieveSpectre(self):
        result = firebase.get('/spectres', None)[1:]
        print (result)
        self.spectres = []
        for i in range(0, len(result)):
            r = result[i]
            s = Spectre(r["name"], r["force"], r["rythm"])
            s.color = Color()
            s.color.decode(r["color"])
            self.spectres.append(s)
       # resultJson = json.loads(result)
       # print (resultJson)
       
    def startNewRandomSpectre(self):
        if self.challengeCount ==0:
            r = self.spectres[0]
        else :
            r = random.choice(self.spectres[1:])
        self.startNewSpectreSequence(r)
        self.challengeCount = self.challengeCount + 1

    def startNewSpectreSequence(self, spectre):
        print( "start new spectre : " + spectre.name)
        self.currentSeq = SpectreSequence(self, spectre)
        self.currentSeq.OnStart()
        
    def terminateCurrentSequence(self):
        if self.currentSeq is None:
            return
        self.currentSeq.OnVictory()
        self.currentSeq = None
       
    def update(self, dt):
        self.timer += dt
        if (self.currentSeq is not None):
            self.currentSeq.update(dt)

class Spectre:
    def __init__(self, name, force, rythm):
        self.name = name
        self.rythm = rythm
        self.force = force
        self.Color = Color()
    def __str__(self):
        return self.name + " - F " + str(self.force) + " - R " + str(self.rythm)

class SpectreSequence(object):
    def __init__(self, game, spectre):
        self.game = game
        self.spectre = spectre
        self.timer = 0
        self.isFinished = False
        self.distance = io.getDistance()
        
    def isFinished(self):
        return self.isFinished
        
    def OnStart(self):
        playSound(self.spectre.name + "_apparition.wav")
        io.setLed(0,False)
        io.setLed(1,False)
        io.setLed(2,False)
        io.setLed(3,True)
        io.setRGB(1, self.spectre.color.r,self.spectre.color.g, self.spectre.color.b, self.spectre.rythm)
        
    def OnVictory(self):
        playSound(self.spectre.name + "_disparition.wav")
		io.setRGB(1,0,0,0, self.spectre.rythm)
        
    def OnDefeat(self):
        pass
        
    def update(self, dt):
        self.timer += dt
        self.distance = io.getDistance()
        
class SSCasper(SpectreSequence):
    def __init__(self, spectre):
        super(spectre, self).__init__(name)
    def update(self, dt):
        self.timer += dt


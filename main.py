

from flask import Flask, jsonify
from firebase import firebase
import gameplay
from gameplay import SpectreGameplay

try :
    FirebaseAddres = "https://spectre-e5ff7.firebaseio.com/"
    firebase = firebase.FirebaseApplication(FirebaseAddres,authentication=None)
    result = firebase.get('/spectres', None)
    print (result)
except :
    print ("cannot run firebase")

#init gameplay
game = SpectreGameplay()


app = Flask(__name__)

@app.route("/")
def get_page():
    s = ""
    c = game.getCurrentSeq()
    if c is None:
        s += "No Spectre inside"
    else :
        s += "There is a spectre inside : " + c.spectre.name
    return s

@app.route("/spectres")
def get_spectres():
    res = ""
    for s in game.spectres:
        res += "<br>" + str(s)
    return res

@app.route("/start")
def evt_start():
    print("start game")
    game.startNewRandomSpectre()
    return get_page()
	
@app.route("/stop")
def evt_stop():
    print("stop game")
    game.terminateCurrentSequence()
    return get_page()

@app.route("/sound/<soundname>")
def evt_sound(soundname):
    playSound(soundname)
    return "sound : " + soundname

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80")
    #print("suite appliction")

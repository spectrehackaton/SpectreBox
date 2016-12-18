import serial

class ArduinoIO:
    def __init__(self):
        self.ser = serial.Serial()
        self.ser.port = 'COM6'
        self.ser.baudrate = 9600
        self.ser.timeout = 1
        self.ser.setDTR(False)
        self.ser.bytesize  = serial.EIGHTBITS
        self.ser.parity = serial.PARITY_NONE
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.open()

        #self.ser = serial.Serial('COM7',9600, rtscts=1)
        print("Port série ouvert")
    def sendToArduino(self,data):
        print(data)
        self.ser.write(data.encode('utf-8'))#BLOQUANT ACTUELLEMENT changer en raw_input sur python 2.7
        print("setLed");

   	#GETTERS
    def getFromArduino(self,req):
    	sendToArduino(req)
    	ans = self.set.readline()
    	return ans

    def getDistance(self):
        print("demande de la distance")
        commande = "inDistance:?"+";"
        answer = self.getFromArduino(commande)
        return answer

    #SETTERS
    def setRGB(self, mode,rouge,vert,bleu,rythme):
    	commande="outRGB:"+str(mode)+","+str(rouge)+","+str(vert)+","+str(bleu)+","+str(rythme)+";"
    	self.sendToArduino(commande)

    def setLed(self,idLed,state):
        commande="outLED:"+str(idLed)+","+str(state)+";"
        self.sendToArduino(commande)
        print("setLed");

    def setVibreur(self, state):
    	commande="outVibreurs:"+str(state)+";"
    	self.sendToArduino(commande)

    def setSolenoid(self, nbCoups,delay):
    	commande="outPok:"+str(nbCoups)+","+str(delay)+";"
    	self.sendToArduino(commande)

    def setMatrice(self,state,mode):
        commande="out88:"+str(state)+","+str(mode)+";"
        self.sendToArduino(commande)

    def setAiguille(self,angle):
        commande="outAiguille:"+str(angle)+";"
        self.sendToArduino(commande)

test = ArduinoIO();
test.setLed(0,1);
test.setRGB(1,0,0,255,10);
test.setLed(1,1);
#test.setVibreur(0);
#test.setSolenoid(1000,1);
#test.setMatrice(1,4);
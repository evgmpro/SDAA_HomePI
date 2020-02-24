import os
import RPi.GPIO as GPIO
from time import sleep
from flask import Flask, render_template, request, Response
from camera_pi import Camera

app = Flask(__name__)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN)

global AnguloX
global AnguloY
global senPIREstado
AnguloX = 90
AnguloY = 70
panPin = 12
tiltPin = 13
senPIREstado= 2

"""Pagina de inicio"""
@app.route('/')
def index():
    senPIREstado= GPIO.input(40)
    """os.system("EnvioEmail.py")""" 
    templateData = {
      'AnguloX'	: AnguloX,
      'AnguloY'	: AnguloY,
      'senPIR'  : senPIREstado
	}
    return render_template('index.html', **templateData)

"""Funcion de generacion de video"""
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

"""Envio de video"""
@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

"""Gestion servos"""
@app.route('/', methods=['POST'])
def servos():
	global AnguloX
	global AnguloY
	global senPIREstado
	nuevoAnguloX= int(request.form['AnguloX'])
	if (nuevoAnguloX != AnguloX):
		AnguloX = nuevoAnguloX 
		os.system("python ServoX.py " + str(AnguloX))
        senPIREstado= GPIO.input(40)
	nuevoAnguloY= int(request.form['AnguloY'])
	if (nuevoAnguloY != AnguloY):
		AnguloY = nuevoAnguloY
		os.system("python ServoY.py " + str(AnguloY))
        senPIREstado= GPIO.input(40)    
	templateData = {
      'AnguloX'	: AnguloX,
      'AnguloY'	: AnguloY,
      'senPIR'  : senPIREstado         
	}
	return render_template('index.html', **templateData)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port =88, debug=True, threaded=True)

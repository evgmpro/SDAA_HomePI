import stmplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import time
import RPi.GPIO as GPIO
# Pines sensor IR
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN)
# Datos de envio
SourceAdress = "sdaahomepi@gmail.com"
DestinyAdress = "sdaahomepi@gmail.com"

server = stmplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(SourceAdress, "sdaamiera1!")

msg = MIMEMultipart()
msg['From'] = SourceAdress
msg['To'] = DestinyAdress
msg['Subject'] = "Alerta de seguridad"

mensaje = "ALERTA! Se ha detectado una presencia en la camara numero 1."
msg.attach(MIMEText(mensaje, 'plain'))
Texto = msg.as_string()

if GPIO.input(40) == 1:
	print "Enviando correo de alerta"
	server.sendmail(SourceAdress, DestinyAdress, Texto)
	time.sleep(5)
    
else:
	print "No se detecto ninguna presencia"
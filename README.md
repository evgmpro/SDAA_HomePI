# SDAA_HomePI
Proyecto de la asignatura de Sistemas Digitales, MIERA Universidad de Sevilla

El proyecto consiste en usar una raspberry pi para hacer streeming de video de la pi cam usando servidor Flask, mover la camara usando dos servos controlados por PWM y un sensor PIR para detectar presencia.

Archivos:

camera_pi.py - codigo diseñado por Miguel Grinberg que habilita la camara y permite hacer video streaming MJPEG
HomePI.py - arranca el servidor Flask y gestiona la API
ServoX e Y.py - gestion de servos
EnvioEmail.py manda un email si la API detecta presencia

# -*- encoding: utf-8 -*-
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
def enviador(correos,tu_correo,contra,asunto,mensaje):
	
	msg = MIMEMultipart()
	password = contra
	msg['From'] = tu_correo
	msg['To'] = correos
	msg['Subject'] = asunto
 
	msg.attach(MIMEText(mensaje, 'plain'))
	server = smtplib.SMTP('smtp.gmail.com: 587')
	server.starttls()
	server.login(msg['From'], password)
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	server.quit()
	print ("Correo enviado satisfactoriamente a %s:" % (msg['To']))

def alerta_correo(correo,tucorreo,contraseña,x):
	#def alerta_correo(correo,x,dicc_alertas=1,dicc_mensajes=1):
	dicc_alertas= { 1:'cacola',
					2:'pedete',
					3:'mamading'}

	dicc_mensajes= { 1:'Alerta por cagada masiva en el salon\nMandar al equipo de limpieza pero ya.\nGracias.',
					 2:'Alerta por pedete maloliente de nivel 5\nMandar al equipo de aspiracion pero ya.\nGracias.',
					 3:'Mamadas gratis para todos.\nEl que avisa no es traidor.'}
					
	enviador(correo,tucorreo,contraseña,dicc_alertas[x],dicc_mensajes[x])







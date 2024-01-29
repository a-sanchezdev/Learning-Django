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
            # pedido = r.recognize_google(audio,language = 'es-mx')

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

# transformar_audio_en_texto()

#funcion para que el asistente pueda ser escuchado

def hablar(mensaje):
    #encender el motor de pyttsx3
    engine = pyttsx3.init()

    #configurar tipo de voz
    voices = engine.getProperty('voices')
    # print(voices)
    engine.setProperty('voice', voices[2].id)
    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


#informar el dia de la semana
def pedir_dia():
    #crear variable con datos de hoy
    dia=datetime.date.today()
    # print(dia)

    #crear una variable para el dia de semana
    dia_semana= dia.weekday()
    # diccionario con dias

    calendario = {0:'Lunes',
                  1:"Martes",
                  2:"Miércoles",
                  3:"Jueves",
                  4:"Viernes",
                  5:"Sábado",
                  6:"Domingo"}
    
    #decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')
    # print(dia_semana)

# pedir_dia()
# hablar('Hola mundo')

#informar que hora es

def pedir_hora():
    #crear variable con datos de la hora
    hora = datetime.datetime.now()
    # print(hora)
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    # decir la hora
    hablar(hora)

# pedir_hora()

def saludo_inicial():
    #decir el saludo
    #crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour >20:
        momento = 'Buenas noches'
    elif  6 <= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'
    
    hablar(f'Hola {momento}, soy Helena, tu asistente personal. Por favor, dime en que te puedo ayudar')


# saludo_inicial()

def pedir_cosas():
    saludo_inicial()
    
    #variable de corte
    comenzar=True
    #loop

    while  comenzar:
        #activar micro y guardar el pedido en string
        pedido = transformar_audio_en_texto().lower()
        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué dia es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando resultado en wikipedia')
            pedido = pedido.replace('wikipedia','')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido,sentences = 1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet','')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado:')
            continue
        elif 'repducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdón no la he encontrado')
                continue

        elif 'adios' in pedido:
            hablar('Me voy a descansar, cualquier cosa me avisas')
            break

pedir_cosas()
import re
import unicodedata
import sys
import random

class ChatBot:

    #Constructor
    def __init__(self):
        pass


    #Regresa una respuesta en base al mensaje que escribio el usuario
    def answer(self, user_input):
        return self.check_all_messages(self.clean_str(user_input))


    #Devuelve la cadena depurada dentro de una lista
    def clean_str(self, str):
    
        #Removemos acentos
        accents = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
        str_normalized = unicodedata.normalize('NFD', str)
        str = str_normalized.translate(accents)
        
        #Removemos caracteres especiales
        str = re.split(r'\s|[,.:;¿?¡!-_#$%&/1234567890]\s*', str.lower())
        
        for i in range(str.count('')):
            str.remove('')
        
        return str
    

    #Calcula la probabilidad de más de una posible respuesta en base a una serie de parametros
    def message_probability(self, user_message, recognized_words, single_response=False, required_word=[]):
        message_certainty = 0
        has_required_words = True

        #Recorrido del mensaje para encontra palabras clave
        for word in user_message:
            if word in recognized_words:
                message_certainty +=1

        #percentage = float(message_certainty) / float (len(recognized_words))

        #Recorrido del mensaje para encontrar palabra obligatoria
        for word in required_word:
            if word not in user_message:
                has_required_words = False
                break

        #Regresa la certeza del mensaje
        if has_required_words or single_response:
            return message_certainty
        else:
            return 0

    #Revisa el mensaje enviado por el usuario y busca palabras clave para escojer una respuesta
    def check_all_messages(self, message):
            highest_prob = {}

            def response(bot_response, list_of_words, single_response = False, required_words = []):
                nonlocal highest_prob
                highest_prob[random.choice(bot_response)] = self.message_probability(message, list_of_words, single_response, required_words)

 
            #Respuestas a saludos
            response(['Hola, ¿puedo ayudarte en algo?', 'Gracias por saludar, ¿puedo servirte en algo?'], ['hola', 'tal', 'saludos', 'buenas', 'tardes', 'buenos', 'dias'], single_response=True)
            #Respuestas a despedidas
            response(['¡Nos vemos!', 'Hasta luego...', 'Bye'],['adios','hasta','luego','nos','vemos','bye','me','voy'], single_response=True)
            #Respuestas a agradecimientos
            response(['De nada, me alegro haber sido de utilidad', '¡Es un placer!', '¡De nada!'], ['gracias', 'agradezco', 'thanks','ha','sido','util','utilidad','agradecer','agradecerte'], single_response=True)
            #Respuestas de ¿Como estas?
            response(['Me siento bien, ¿que tal tú?', 'Estoy bien, ¿y tú?'], ['estas', 'va', 'vas', 'sientes','sentir'])
            #Respuestas existenciales 
            response(['Soy una IA con el único proposito de responder algunas preguntas acerca del zoológico de Chapultepec, ¿requieres alguna información?'],['eres', 'quien', 'haces', 'limitaciones', 'existes', 'crearon', 'humano'], single_response=True)
            #Respuestas de pago por entrada
            response(['La entrada al zoológico es totalmente gratis', 'No se cobra por la entrada al zoológico'], ['entrada', 'visita', 'entrar', 'visitar'], single_response=True)
            #Respuestas de estacionamiento
            response(['Hay más de un estacionamiento en la zona, da click el siguiente enlace para conocer más detalles de estos. https://www.chapultepec.org.mx/wp-content/uploads/2019/01/estacionamientos-y-ban%CC%83os.pdf'],['estacionamiento', 'entrar', 'estacionarme', 'carro', 'auto', 'aparcar', 'estacionar', 'aparcamiento'], single_response=True)



            best_match = max(highest_prob, key=highest_prob.get)

            return self.unknown() if highest_prob[best_match] < 1 else best_match


    #Respuestas para mensajes que no entiende
    def unknown(self):
        response = random.choice(['¿Puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'No entiendo tu pregunta', 'No puedo responder esa pregunta'])
        return response
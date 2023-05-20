import Chatbot

cb = Chatbot.ChatBot()


#Ciclo de preguntas
mensaje_inicial =  "Bot: Hola, ¿en que puedo ayudarte?"

print(mensaje_inicial)

while True:
    user_input = input('You: ')

    if user_input == "salir":
      break;

    print("Bot: " + cb.answer(user_input))
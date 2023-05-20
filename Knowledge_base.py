class Base:

    def __init__(self):
        #Diccionario de datos del zoológico
        self.zoologico = {
            
            "dirección": "Dirección General de Zoológicos y Vida Silvestre. Calle Chivatito s/n 1ª sección del Bosque de Chapultepec, Col. San Miguel Chapultepec, C.P. 11850, Delegación Miguel Hidalgo, México D.F. Tel. 5553-6263 ext. 2000.",
            
            "habitats": {
                "desierto": ["dromedarios", "camello", "lince rojo", "licaon", "tortuga africana", "papion sagrado", "borrego cimarron", "tarantula", "lobo mexicano"],
                "pastizales": ["loro gris", "puerco espin", "hiena", "tortuga aldabra", "tortuga mapini", "tortuga leopardo", "tortuga patas amarillas", "tortuga patas rojas", "leon africano", "rinoceronte blanco", "antilope acuatico", "ganso egipcio", "antilope sable", "hipopotamo", "ganso chino", "antilope orix", "antilope ñu", "cebra", "jirafa", "gallina de guinea", "grulla coronada", "avestruz", "antilope nilgo", "venado cerdo", "muflon europeo", "antilope gemsbock", "wallaby", "canguro rojo", "llama", "antilope nyala", "bisonte americano", "liebre de la patagonia"],
                "franja costera": ["pinguino", "lobo marino"],
                "tundra": ["oso polar"],
                "aviario": ["flamenco", "cisne", "aguila real", "halcon peregrino", "condor de los andes", "aguila cola blanca", "aguila rojinegra", "aguililla cola roja", "aguila caminera", "zopilote rey", "buho", "caracara", "zopilote comun", "condor de california", "pato pijiji", "emú"],
                "bosque templado": ["xoloitzcuintle", "venado cola blanca", "pavo real", "guajolote norteño", "teporingo", "mono japones", "mapache", "cacomixtle", "zorrillo", "oso pardo", "caracal", "lobo canadiense", "gamo", "zorro artico", "panda rojo", "panda gigante", "venado sika", "wapiti", "lobo mexicano", "tigre de sumatra"],
                "bosque tropical": ["ajolote", "jaguar negro", "ocelote", "capibara", "cotorra de la patagonia", "mono ardilla", "jaguar", "mono araña", "capuchino de cuernos", "coati", "martucha", "capuchino de gargante blanca", "oso de anteojos", "binturong", "mono rhesus", "mono araña", "chimpance", "puma", "paloma verde", "venado temazate", "aguti dorado", "orangutan", "cocodrilo", "titi de goeldi", "titi cabeza de leon dorado", "titi copete de algodon", "gorila", "pantera", "leopardo", "tapir", "mono patas", "tigre de bengala"]
            }

        }


    def find_animal(self, word_list):
        encontrar_habitats = []
        for habitat, animal_lista in self.zoologico["habitats"].items():
            for animal in animal_lista:
                if all(token in tokens for token in animal.split()):
                    encontrar_habitats.append(habitat)
        if encontrar_habitats:
            return f"Los animales que buscas se encuentran en los siguientes hábitats del zoológico de Chapultepec: {', '.join(encontrar_habitats)}."
        else:
            return "Lo siento, no se encontraron animales de ese tipo en el zoológico de Chapultepec."
        


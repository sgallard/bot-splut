import telegram
import random
from telegram.ext import Updater
from telegram.ext import CommandHandler
import requests


import copy
from parse import urlencode
TOKEN = '399695637:AAEnj9GkwMMZAvYVuFmozEq4D7epsSj5KC0'
mi_bot = telegram.Bot(token=TOKEN)
mi_bot_updater = Updater(mi_bot.token)

prioridades = {
	"Tanax237": 12440,
	"Rigonzal": 12000,
	"vlizana":12500,
	"Pollo_chicken":12990,
	"Ignacio":12600,
}




syn_parameters = {
    'text': '',
    'voice': 'es-ES_EnriqueVoice',
    'download': True,
    'accept': 'audio/ogg'
}


def synthesize(text):
    # Don't modify the original object
    parameters = copy.copy(syn_parameters)

    # Set the text
    parameters['text'] = text
    print text

    # Request foo!

    r = requests.get('https://text-to-speech-demo.mybluemix.net/api/synthesize?' + "text="+text+"&voice="+parameters['voice']+"&en-US_AllisonVoice&download=True&accept=audio%2Fogg")

    return r



def start(bot=mi_bot, update=mi_bot_updater):
	print "Iniciada conversacion: "
	print update.message.chat_id
	bot.sendMessage(chat_id=update.message.chat_id, text="Holi!!! usa /? para ver los comandos qlos")


def ayuda(bot=mi_bot, update=mi_bot_updater):
 	print "Solicita ayuda"
 	bot.sendMessage(chat_id=update.message.chat_id, text="/start: iniciar conversacion")
 	bot.sendMessage(chat_id=update.message.chat_id, text="/split: mostrar al split culiaito")
 	bot.sendMessage(chat_id=update.message.chat_id, text="/sexysplit: mostrar a un sexy split")
 	bot.sendMessage(chat_id=update.message.chat_id, text="/splitnumber: agrega el numero del split pa putearlo")
 	bot.sendMessage(chat_id=update.message.chat_id, text="/kicksplit: Echa al split por culiaito")
 	bot.sendMessage(chat_id=update.message.chat_id, text="/studyIO: Estudiar pal control de IO")
 	bot.sendMessage(chat_id=update.message.chat_id, text="/studyCC: preparar ano para CC")
 	bot.sendMessage(chat_id=update.message.chat_id, text="/makeISWproject: obtener ayuda y motivacion para el proyecto de ISW")
 	bot.sendMessage(chat_id=update.message.chat_id, text="/getNota: revisar nota de IO/CC")
 	bot.sendMessage(chat_id=update.message.chat_id, text="/angery: enviar angery")
	bot.sendMessage(chat_id=update.message.chat_id, text="/notaCC: ver la nota de CC del tercer certamen pa pasar la caga de ramo")
	bot.sendMessage(chat_id=update.message.chat_id, text="/react [like | laik | love | haha | wow | sad | angery | angry | me emperra | emperrado | emperra]: react a la wea que mando el saco wea anterior")
	bot.sendMessage(chat_id=update.message.chat_id, text="/getPrioridad: ver tu caga de prioridad")
	bot.sendMessage(chat_id=update.message.chat_id, text="/zurdito: ver el estado de animo del zurdo")
	bot.sendMessage(chat_id=update.message.chat_id, text="/tts [text]")



def split(bot=mi_bot, update=mi_bot_updater):
	print "spluteaoasdsad"
	foto = open('images/18447923_1909116285889212_160549128_n.jpg', 'rb')
	bot.sendPhoto(chat_id=update.message.chat_id, photo=foto)

def sexysplit(bot=mi_bot,update=mi_bot_updater):
	print "Sensual split"
	foto = open('images/12729013_10205749710398407_5346918339122478552_n-2.png', 'rb')
	bot.sendPhoto(chat_id=update.message.chat_id, photo=foto)

def sendsplitnumber(bot=mi_bot, update=mi_bot_updater):
	print "Split number"
	numero = "(+56) 975196815"
	bot.sendContact(chat_id=update.message.chat_id, phone_number=numero,first_name= "Splut")
def kicksplit(bot=mi_bot,update=mi_bot_updater):
	split = 228108913
	print split
	bot.kickChatMember(chat_id=update.message.chat_id, user_id=split)

def riff(bot = mi_bot, update=mi_bot_updater):
	foto = open('images/26673412.jpg', 'rb')
	bot.sendPhoto(chat_id=update.message.chat_id, photo=foto)
def CC(bot =mi_bot, update=mi_bot_updater):
	foto = open('images/18716851_1204762706301647_363081161_n.png', 'rb')
	bot.sendPhoto(chat_id=update.message.chat_id, photo=foto)
def famancil(bot =mi_bot, update=mi_bot_updater):
	foto = open('images/10336817_10208027393784185_6690153196930108246_n.png', 'rb')
	bot.sendPhoto(chat_id=update.message.chat_id, photo=foto)

def nota(bot=mi_bot, update=mi_bot_updater):
	print "random number"
	nota = random.randint(0,100)
	if nota>=55:
		bot.sendMessage(chat_id=update.message.chat_id, text="Wena culiaito, te sacaste un "+str(nota))
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text="Puta el m3n, te sacaste un "+str(nota))
def angery(bot=mi_bot, update=mi_bot_updater):
	foto_name = "images/angery" + str(random.randint(1,10))
	if foto_name=="images/angery7":
		foto_name = foto_name + ".gif"
		print foto_name
		foto = open(foto_name, 'rb')
		bot.sendDocument(chat_id=update.message.chat_id, document=foto)
	else:
		foto_name = foto_name + ".jpg"
		print foto_name
		foto = open(foto_name, 'rb')
		bot.sendPhoto(chat_id=update.message.chat_id, photo=foto)



def calculate_CC(nota1, nota2):
	nota = (55**3)/((nota1 + nota2)/2)**2
	print nota
	return str(int(nota))

def notaCC(bot=mi_bot, update=mi_bot_updater):
	username = update.message.from_user.username
	print update.message.from_user.username

	if (username == 'Rigonzal'):
		bot.sendMessage(chat_id=update.message.chat_id, text="Splut qlo ke wea, necesitai un  "+calculate_CC(22.0,100.0))
	elif (username == 'vlizana'):
		bot.sendMessage(chat_id=update.message.chat_id, text="Lizana qlo ke wea, necesitai un  "+calculate_CC(46.0,89.0))
	elif (update.message.from_user.first_name == 'Ignacio'):
		bot.sendMessage(chat_id=update.message.chat_id, text="Zurdo qlo ke wea, necesitai un  "+calculate_CC(37.0,77.0))
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text="aweonaito no estay dando el ramo.Un 0 y un angery por weon")
		foto_name = "images/angery" + str(random.randint(1,10))
		if foto_name=="images/angery7":
			foto_name = foto_name + ".gif"
			print foto_name
			foto = open(foto_name, 'rb')
			bot.sendDocument(chat_id=update.message.chat_id, document=foto)
		else:
			foto_name = foto_name + ".jpg"
			print foto_name
			foto = open(foto_name, 'rb')
			bot.sendPhoto(chat_id=update.message.chat_id, photo=foto)

def react(bot=mi_bot, update=mi_bot_updater):
	diccionario = {"like":"CAADAQADfgEAAs2YnAG4WSL0AwxiWQI",
					"laik":"CAADAQADfgEAAs2YnAG4WSL0AwxiWQI",
					"love":"CAADAQADgAEAAs2YnAH285wHzomsjQI",
					"haha":"CAADAQADggEAAs2YnAEP4oedspigpQI",
					"wow":"CAADAQADggEAAs2YnAEP4oedspigpQI",
					"sad":"CAADAQADhwEAAs2YnAGCKUQnmxaIhAI",
					"angery":"CAADAQADiQEAAs2YnAGiEIFH8h6rtQI",
					"angry":"CAADAQADiQEAAs2YnAGiEIFH8h6rtQI",
					"me emperra":"CAADAQADiQEAAs2YnAGiEIFH8h6rtQI",
					"emperrado":"CAADAQADiQEAAs2YnAGiEIFH8h6rtQI",
					"emperra":"CAADAQADiQEAAs2YnAGiEIFH8h6rtQI",}

	string = str(update.message.text)[7::]
	if string in diccionario:
		bot.sendSticker(chat_id=update.message.chat_id, sticker=diccionario[string])
	else:
		bot.sendSticker(chat_id=update.message.chat_id, sticker="CAADAgADDwIAAtzyqwflTv80MV32fgI")

def getPrioridad(bot=mi_bot, update=mi_bot_updater):
	username = update.message.from_user.username

	if (update.message.from_user.first_name == 'Ignacio'):
		username = "Ignacio"

	print update.message.from_user.username
	message = "Oe "+str(username)+", tu prioridad es de: "+str(prioridades[username])
	print prioridades[username]

	bot.sendMessage(chat_id=update.message.chat_id, text=message)
	prioridades[username]-=random.randint(1,500)

def zurdito(bot=mi_bot,update=mi_bot_updater):
	print "zurdi"
	foto = open('images/19489513_10213537875309483_1719765454_n.png', 'rb')
	bot.sendPhoto(chat_id=update.message.chat_id, photo=foto)

def tts(bot=mi_bot, update=mi_bot_updater):

    text = (update.message.text).strip("/tts ")
    print text, 'tts'

    tmp_f = open('tmp.ogg', 'wb+')
    tmp_f.write(synthesize(text).content)
    tmp_f.close()

    bot.sendAudio(chat_id=update.message.chat_id, audio=open('tmp.ogg', 'rb'))


    os.remove('tmp.ogg')








#Creamos nuestra instancia "mi_bot" a partir de ese TOKEN




#Definimos para cada comando la funcion que atendera la peticion
start_handler = CommandHandler('start', start)
ayuda_handler = CommandHandler('?', ayuda)
split_handler = CommandHandler('split',split)
sexy_split_handler = CommandHandler('sexysplit', sexysplit)
sendsplitnumber_handler = CommandHandler('splitnumber',sendsplitnumber)
kick_split_handler = CommandHandler('kicksplit', kicksplit)
riff_handler = CommandHandler('studyIO',riff)
CC_handler = CommandHandler('studyCC',CC)
famancil_handler = CommandHandler('makeISWproject',famancil)
nota_handler = CommandHandler('getNota',nota)
angery_handler = CommandHandler('angery',angery)
nota_cc_handler = CommandHandler('notaCC',notaCC)
react_handler = CommandHandler('react',react)
get_prioridad_handler = CommandHandler('getPrioridad',getPrioridad)
zurdito_handler = CommandHandler('zurdito',zurdito)
tts_handler = CommandHandler('tts',tts)

dispatcher = mi_bot_updater.dispatcher

dispatcher.add_handler(start_handler)
dispatcher.add_handler(ayuda_handler)
dispatcher.add_handler(split_handler)
dispatcher.add_handler(sexy_split_handler)
dispatcher.add_handler(sendsplitnumber_handler)
dispatcher.add_handler(kick_split_handler)
dispatcher.add_handler(riff_handler)
dispatcher.add_handler(CC_handler)
dispatcher.add_handler(famancil_handler)
dispatcher.add_handler(nota_handler)
dispatcher.add_handler(angery_handler)
dispatcher.add_handler(nota_cc_handler)
dispatcher.add_handler(react_handler)
dispatcher.add_handler(get_prioridad_handler)
dispatcher.add_handler(zurdito_handler)
dispatcher.add_handler(tts_handler)

mi_bot_updater.start_polling()

while True: #Ejecutamos nuestro programa por siempre
    pass

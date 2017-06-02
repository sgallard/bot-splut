import telegram  
import random
from telegram.ext import Updater  
from telegram.ext import CommandHandler  
TOKEN = '399695637:AAEnj9GkwMMZAvYVuFmozEq4D7epsSj5KC0'
mi_bot = telegram.Bot(token=TOKEN)  
mi_bot_updater = Updater(mi_bot.token)  

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




def split(bot=mi_bot, update=mi_bot_updater):
	print "splut"
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

mi_bot_updater.start_polling()

while True: #Ejecutamos nuestro programa por siempre  
    pass
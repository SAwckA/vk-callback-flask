# Представление команд бота
#
# Представляет из себя бизнес логику команд
#
# Пример использования:
#
# @Command.bind(<str: команда бота>) // Определения триггер функции на команду <command>
# def exaple(message, ctx):	     // Функция, обязательно принимает:
#				     // 1. message <VKHandler.MessageNewObj: объект полученного сообщения>
# 				     // 2. ctx <list: список аргументов переданных с командой
# 	#do something		     // Алгоритм при вызове команды
# 	pass
#


from .VKcommands import Command
from .VKapi import Messages


@Command.bind('echo')
def start(message, ctx):
	api = Messages()
	print(':::CTX ', ctx)
	res = api.send(message.from_id, str(ctx) if ctx else 'echo')
	print(res)


@Command.bind('ex')
def ex(message, ctx):
	pass



# Модуль описания логики комманд
#
#

import settings
#import VKapi
from typing import Callable


class VKcommands:
	def __init__(self):
		pass



class Command:
	"""Factory функций связанных с командами бота"""
	registery = {}

	@classmethod
	def bind(cls, command:str) -> Callable:
		"""Декоратор, добавляющий функцию в список команд"""
		def inner_wrapper(func):
			cls.registery[settings.COMMAND_PREFIX+command] = func
			return func
		return inner_wrapper

	@classmethod
	def get_command(cls, text:str, msg):
		"""Возвращает ассоциированную функцию || Возвращает None, если функция не существует"""
		ctx = Command._parse_args(text)
		command = ctx[0]

		if command not in cls.registery:
			print('Command does not exist')
			return None

		exec_func = cls.registery[command]
		return exec_func(msg, ctx[1:])

	@staticmethod
	def _parse_args(text):
		return text.split(' ')


if __name__ == "__main__":
	pass

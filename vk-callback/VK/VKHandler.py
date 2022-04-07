# Модуль VKHandler
# Endpoint method: method(type:<str: тип события получаемый от сервера>, 
# 			  recv_data:<dict: полученный объект от сервера>)
#
# Выполняет промежуточную роль определения события

from . import VKapi
from . import ViewsCommands
import settings


def method(type, recv_data):
	"""Определяет тип полученного события"""
	{
		'message_new':message_new
	}.get(recv_data.get('type'))(recv_data)

class MessageNewObj:
	"""Объект полученного сообщения, типом события message_new"""
	def __init__(self, data):
		obj = data.get('object').get('message')
		self.id = obj.get('id')
		self.date = obj.get('date')
		self.peer_id = obj.get('peer_id')
		self.from_id = obj.get('from_id')
		self.text = obj.get('text')
		self.random_id = obj.get('random_id')
		self.ref = obj.get('ref')
		self.ref_source = obj.get('ref_source')
		self.attachments = obj.get('attachments')
		self.important = obj.get('important')
		self.geo = obj.get('geo')
		self.payload = obj.get('payload')
		self.keyboard = obj.get('keyboard')
		self.fwd_message = obj.get('fwd_message')
		self.reply_message = obj.get('reply_message')
		self.action = obj.get('action')
		self.admin_author_id = obj.get('admin_author_id')
		self.conversation_message_id = obj.get('conversation_message_id')
		self.is_cropped = obj.get('is_cropped')
		self.member_cont = obj.get('members_count')
		self.update_time = obj.get('update_time')
		self.was_listened = obj.get('was_listened')
		self.pinned_at = obj.get('pinned_at')
		self.message_tag = obj.get('message_tag')


def message_new(data:dict):
	"""Обработка полученного события"""
	message = MessageNewObj(data)
	if is_command(message):
		return ViewsCommands.Command.get_command(message.text, message)
	return MessageNewObj(data)
	# echo VKapi.Messages().send(obj.from_id, obj.text)

def is_command(message:MessageNewObj) -> bool:
	"""Проверка является ли командой сообщение"""
	if message.text.startswith(settings.COMMAND_PREFIX):
		return True
	return False

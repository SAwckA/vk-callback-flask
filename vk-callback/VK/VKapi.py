
# Модуль для работы с API вконтакте
#
# Описаны только основные методы, полный перечень можно найти здесь:
# 	https://api.vk.com/method/
# Родительский класс: API

import requests
import settings
import numpy
import json


class API:
	def __init__(self):
		self.url = settings.BASE_URL_API
		self.v = settings.API_VERSION

class Messages(API):
	def __init__(self):
		super(Messages, self).__init__()
		self.url += 'messages.'

	def send(self, user_id, message):
		data = {
			'user_id':user_id,
			'access_token':settings.GROUP_TOKEN,
			'v':settings.API_VERSION,
			'message': message,
			'random_id': numpy.random.randint(2**31)
		}
		r = requests.post(self.url+'send', params=data)
		r = json.loads(r.content)
		if r.get('error'):
			return r
		return 'ok'

# Файл настроек
#
# BASE_URL_API <str: корневой URL адрес API>
#
# API_VERSION <str: Актуальная версия API>
#
# TOKEN <str: сервисный ключ>
#
# GROUP_TOKEN <str: токен сообщества>
#
#

import os


BASE_URL_API = 'https://api.vk.com/method/'

API_VERSION = '5.131'

TOKEN = ''

GROUP_TOKEN = os.environ.get('GROUP_TOKEN')

COMMAND_PREFIX = '/'

GROUP_ID = ''

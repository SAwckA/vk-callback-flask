from flask import Flask, request
from VK.VKHandler import method

app = Flask(__name__)


@app.route('/vk', methods=['POST'])
def vk():
	data = request.get_json()
	type = data.get('type')
	if data.get('type') == 'confirmation':
		return '727ef563'

	method(type, data)
	return 'ok'


@app.route('/index', methods=['GET'])
def index():
	return '<h1>TESTING WEBHOOKS USING VPS/VDS SERVERS<h1>'



if __name__ == "__main__":
	app.run(host='0.0.0.0', port='80', debug=True)

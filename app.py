from flask import Flask, render_template
from paho.mqtt import client as mc

app = Flask(__name__)

broker = 'broker.emqx.io'

port = 1883
add = 'topicName/time'

clientid = 'IoT'
username = 'root'
password = ''


@app.route('/')
def index():
    return render_template('index.html')


def connect_mqtt():
	client = mc.Client(clientid)
	client.username_pw_set(username, password)

	client.connect(broker, port);

	return client



@app.route('/main', methods=['POST'])

def main():
	return render_template("main.html")


@app.route('/1', methods=['POST'])

def release():
	testRelease()
	return render_template("1.html")

def testRelease():
	client = connect_mqtt()
	client.loop_start()
	sendReleaseData(client)


@app.route('/2', methods=['POST'])

def engine():
	engineTest()
	return render_template("2.html")

def engineTest():
	client = connect_mqtt()
	client.loop_start()
	sendEngineData(client)


@app.route('/3', methods=['POST'])

def activate():
	activateTest()
	return render_template("3.html")

def activateTest():
	client = connect_mqtt()
	client.loop_start()
	sendActivateData(client)



@app.route('/4', methods=['POST'])

def ignite():
	igniteRelease()
	return render_template("4.html")

def igniteRelease():
	client = connect_mqtt()
	client.loop_start()
	sendIgniteData(client)



@app.route('/5', methods=['POST'])

def vent():
	testVent()
	return render_template("5.html")

def testVent():
	client = connect_mqtt()
	client.loop_start()
	sendVentData(client)



@app.route('/6', methods=['POST'])

def srb():
	testSRB()
	return render_template("6.html")

def testSRB():
	client = connect_mqtt()
	client.loop_start()
	sendSRBData(client)












def sendReleaseData(client):
	msg = '1'
	result = client.publish(add, msg)
	status = result[0]
	if status == 0 :
		print("Send '{msg}' to address '{add}'")


def sendEngineData(client):
	msg = '2'
	result = client.publish(add, msg)
	status = result[0]
	if status == 0 :
		print("Send '{msg}' to address '{add}'")


def sendActivateData(client):
	msg = '3'
	result = client.publish(add, msg)
	status = result[0]
	if status == 0 :
		print("Send '{msg}' to address '{add}'")


def sendIgniteData(client):
	msg = '4'
	result = client.publish(add, msg)
	status = result[0]
	if status == 0 :
		print("Send '{msg}' to address '{add}'")


def sendVentData(client):
	msg = '5'
	result = client.publish(add, msg)
	status = result[0]
	if status == 0 :
		print("Send '{msg}' to address '{add}'")


def sendSRBData(client):
	msg = '6'
	result = client.publish(add, msg)
	status = result[0]
	if status == 0 :
		print("Send '{msg}' to address '{add}'")






if __name__ == "__main__":
    app.run(port='5001')
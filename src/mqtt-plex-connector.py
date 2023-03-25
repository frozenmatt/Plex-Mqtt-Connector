from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import requests
import json
import paho.mqtt.publish as publish
import os

app = Flask(__name__)
api = Api(app)

# Get environment variables
broker_address = os.getenv('MQTT_BROKER_HOST')
broker_port = int(os.getenv('MQTT_BROKER_PORT'))
broker_user = os.getenv('MQTT_BROKER_USER')
broker_pass = os.getenv('MQTT_BROKER_PASSWORD')
topic = os.getenv('MQTT_TOPIC')

#Debugging
print (f"Broker Info: {broker_address}:{broker_port}{topic}")

@app.route('/', methods=['POST'])
def webhook():
    data = json.loads(request.form['payload'])

    #Debugging
    print(f"Posting: TOPIC: {topic} PLAYER-UUID: {data['Player']['uuid']} EVENT: {data['event']}")

    # Assign the user and password for the MQTT Broker
    mqtt_auth = { 'username': broker_user, 'password': broker_pass }

    publish.single(topic + "/" + data['Player']['uuid'] + "/event", data['event'], hostname=broker_address, port=broker_port, auth=mqtt_auth)
    # publish.single(topic + data['Player']['uuid'] + '/title', data['Metadata']['title'],
    #                hostname=broker_address, port=broker_port, auth=mqtt_auth)
    # publish.single(topic + data['Player']['uuid'] + '/type', data['Metadata']['type'],
    #                hostname=broker_address, port=broker_port, auth=mqtt_auth)
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode
import logging
import paramiko
import cv2
from darkflow.net.build import TFNet

global tf
global ssh
global sftp

options = {"model": "cfg/yolo.cfg", "load": "bin/yolov2.weights", "threshold": 0.1}
tf = TFNet(options)
app = Flask(__name__)
ask = Ask(app, "/test")
log = logging.getLogger("flask_ask").setLevel(logging.DEBUG)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.0.0.67', 22, 'pi', 'pi')
sftp = ssh.open_sftp()

@ask.launch
def start_skill():
    welcome = "Hello Leo! How can I help you today?"
    return question(welcome)

@ask.intent("photoIntent")
def photo_skill():
    stdin, stdout, stderr = ssh.exec_command('cd /home/pi/alexa-avs-sample-app/test && sudo modprobe bcm2835-v4l2 && python3 snapshot.py')
    time.sleep(1)
    print(stdout.readlines())
    file = getFile()
    result = str(process(file))
    return statement(result)

@ask.intent("yesIntent")
def yes_intent():
    text = "Nice weather today"
    return statement(text)

@ask.intent("noIntent")
def no_intent():
    bye = "I don't understand"
    return statement(bye)

@ask.intent("countIntent")
def count(num):
    num = 3
    return statement(3)

def getFile():
    localPath = "C://Codes/darkflow/darkflow-master/darkflow-master/photos/"
    remotePath = '/home/pi/alexa-avs-sample-app/test/photos/'
    stdin, stdout, stderr = ssh.exec_command('ls -l /home/pi/alexa-avs-sample-app/test/photos/')
    cnt = 0
    fileNames = stdout.readlines()
    fileName = ""
    for fileName in fileNames:
        fileName = str(fileName)
    fileName = fileName.split(" ")
    fileName = fileName[-1]
    fileName = fileName[:-1]
    remoteFile = remotePath + fileName
    localFile = localPath + fileName
    sftp.get(remoteFile, localFile) #from where to where
    return fileName

def process(fileName):
    img = cv2.imread("photos/" + fileName)
    return tf.return_predict(img)

if __name__ == '__main__':
    app.run(debug=True, port = 8000)

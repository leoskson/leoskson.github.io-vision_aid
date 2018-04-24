import paramiko, os, cv2, time
from darkflow.net.build import TFNet
local_file = "C://Codes/darkflow/darkflow-master/darkflow-master/photos/"
remote_file = '/home/pi/alexa-avs-sample-app/test/photos/'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.0.0.67', 22, 'pi', 'pi')
sftp = ssh.open_sftp()
##################3
img = ""
options = {"model": "cfg/yolo.cfg", "load": "bin/yolov2.weights", "threshold": 0.1}
tf = TFNet(options)


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


command = "python3 voice.py "
def process(fileName):
    img = cv2.imread("photos/" + fileName)
    return tf.return_predict(img)
    #ssh.exec_command(command + result)

_, count, _ = ssh.exec_command('cd /home/pi/alexa-avs-sample-app/test/photos; ls -l | grep -v ^d | wc -l')
prevCount=int(count.readlines()[0])
newCount = prevCount
print("waiting")
while True:
    ### count update
    time.sleep(1)
    _, count, _ = ssh.exec_command('cd /home/pi/alexa-avs-sample-app/test/photos; ls -l | grep -v ^d | wc -l')
    newCount=int(count.readlines()[0])
    for line in count:
        newCount = int(line)
    if (newCount != prevCount):
        print("new File Found... Processing")
        file = getFile()
        result = str(process(file))
        b = result.replace(" ","")

        #result2 = "".join(result.split())
        testing = '[{"test":"abc","a":"b"},{"test":"abc","a":"b"},{"test":"abc","a":"b"},{"test":"abc","a":"b"},{"test":"abc","a":"b"},{"test":"abc","a":"b"},{"test":"abc","a":"b"}]'
        a = '[{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"},{"a":"b"}]'
        #remotePath = "/home/pi/alexa-avs-sample-app/test/" + file
        #localPath = "C://Codes/darkflow/darkflow-master/darkflow-master/photos/" + file
        #sftp.put(localFile, remoteFile) #from where to where
        print(b)
        a, res, c = ssh.exec_command('cd /home/pi/alexa-avs-sample-app/test; python read.py ' + b)
        print(res.readlines())
        prevCount = newCount
    else:
        print("waiting")


sftp.close()
ssh.close()

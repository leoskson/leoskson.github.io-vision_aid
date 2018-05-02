<img src="icon.png" align="right" />

# Project Description and API

## Motivation
- Technology for people with discomfort requires more improvement and effort
- ~1.1 Million blind people in the US alone
- Products for the blind are either very expensive or not helpful
- A lot of technical challenges can be overcome by advanced computer vision algorithms and deep learning neural network
- Portability +  Accuracy +  Reliability = Wearable Device 


## Overall Architecture
![capture](https://user-images.githubusercontent.com/17104166/39505897-59a0a990-4da3-11e8-82c2-efebffab20dd.JPG)

## Hardware Specification
![capture2](https://user-images.githubusercontent.com/17104166/39505919-7e04dcd4-4da3-11e8-8a37-161ecfdf738a.JPG)
- Since it is a wearable device, we focused on making the prototype simple and lightweight
- External Aux: Either connects to the speaker or headphones
- USB Microphone


## Software Specification

- Flask-Ask API: Rapid Alexa Skills kit Development: Helps construct ask and tell responses
- Tensorflow (deep-learning workstation; machine learning engine): for training process (natural language processing)
- YOLO V2: real-time object detection system proposed by Joseph Redmon. Relatively simple algorithm but very very fast
- Paramiko API(implementation of the SSHv2 protocol) to communicate between server on Pi 3 and client (by linux command)

## Manual
- Upon user’s command, REST API Server triggers snapshot.py on Pi3
- Photo from Pi automatically transfers to the main computer
- Main computer classifies the object and POSTs the output result to the server that is integrated with AlexaPi
- AlexaPi spits out the result in word

## Demo
![capture3](https://user-images.githubusercontent.com/17104166/39505938-a1a3faee-4da3-11e8-92bf-0907cc0938d4.JPG)
![kakaotalk_20180502_012618656](https://user-images.githubusercontent.com/17104166/39506635-f0ca6eec-4da7-11e8-95f3-3fa22e642474.jpg)
- Video Link: https://www.youtube.com/watch?v=yNhVX7sTI3Q&feature=youtu.be



## Developers
![kakaotalk_20180502_012005577](https://user-images.githubusercontent.com/17104166/39506590-93e3d812-4da7-11e8-82f5-eb277e40e313.jpg)
- Seung Kwang Son
- Ronald Fadehan
- Keeseok Hong
- Changmin Lee


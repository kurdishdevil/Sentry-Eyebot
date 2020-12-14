import servoController
from datetime import datetime
import json
import urllib
from firebase import Firebase
config = {
    'apiKey': "AIzaSyBfw-o9Bj5XmwOTOpJI9FjCUqmUZ8R0wwI",
    'authDomain': "sentry-eyebot.firebaseapp.com",
    'databaseURL': "https://sentry-eyebot-default-rtdb.europe-west1.firebasedatabase.app",
    'projectId': "sentry-eyebot",
    'storageBucket': "sentry-eyebot.appspot.com",
    'messagingSenderId': "778059947065",
    'appId': "1:778059947065:web:1be738fbaaca081d2d01e8",
    'measurementId': "G-7KJYCKWH01"
}
firebase = Firebase(config)
lastServoValue=0
while True:
    db = firebase.database()
    servoValue = db.child("servo1").get().val()
    if servoValue != lastServoValue:
        servoController.SetAngle(servoValue)
        print(servoValue)
        lastServoValue=servoValue
    

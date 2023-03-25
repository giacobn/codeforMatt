import pyrebase
import time
class api_caller: 
    _config = {
        "apiKey": "AIzaSyDCSVVTezCeKcScHTc-OuXIm8KhhLRhkL8",
        "authDomain": "usersignin-fbecc.firebaseapp.com",
        "projectId": "usersignin-fbecc",
        "storageBucket": "usersignin-fbecc.appspot.com",
        "messagingSenderId": "648351672323",
        "appId": "1:648351672323:web:8cc3e25319c35d0ae34636",
        "measurementId": "G-KB4P0VTSRZ",
        "serviceAccount": "serviceAccount.json",
        "databaseURL": "https://usersignin-fbecc-default-rtdb.firebaseio.com/"
    }
    frameCount = 0
    fireSmokePeopleCount = 0
    firesmokeCount = 0
    def __init__(self):
        pass
    def uploadFire(image):
        firebase = pyrebase.initialize_app(api_caller._config)
        storage = firebase.storage()
        while True:
            # Upload the file to Firebase Storage
            storage.child(image).put(image)

            # Refresh the file list in Firebase Storage
            files = storage.list_files()
            print("List of files in Firebase Storage:")
            for file in files:
                print(file.name)

            # Wait for a few seconds before repeating the loop
            time.sleep(1)
    def count_update(fire,people,frame):
        api_caller.frameCount+=1
        if(fire and not(people)):
            api_caller.firesmokeCount +=1
        elif(fire and people):
            api_caller.fireSmokePeopleCount +=1
        if(api_caller.firesmokeCount>1):
            api_caller.uploadFire(frame)
        if(api_caller.fireSmokePeopleCount>0):
            print("warning")
            #pushnotification
            api_caller.uploadFire(frame)
        if api_caller.frameCount>2:
            api_caller.frameCount = 0
            api_caller.fireSmokePeopleCount = 0
            api_caller.firesmokeCount = 0
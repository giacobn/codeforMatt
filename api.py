import cv2
import requests

class FirebaseStorageUploader:
    project_id = "usersignin-fbecc"
    bucket_name = "usersignin-fbecc.appspot.com"
    access_token = "3ebde5d70fa8171a9832b4d053068452b96a358"
    fire_count = 0
    people_count = 0
    
    def upload_image(self, image, file_name):
        # Create the URL for the Firebase Storage upload API
        url = f"https://firebasestorage.googleapis.com/v0/b/{self.bucket_name}/o?name={file_name}"

        # Create the request headers with the access token and content type
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "image/jpeg"
        }

        # Encode the OpenCV image as JPEG and send a POST request to the Firebase Storage upload API
        _, encoded_image = cv2.imencode(".jpg", image)
        response = requests.post(url, headers=headers, data=encoded_image.tobytes())

        # Print the response from the Firebase Storage upload API
        print(response.text)
        
    def check_fire(self, frame, fire_detected, people_detected):
        if fire_detected:
            self.fire_count += 1
            if self.fire_count >= 2 and self.people_count>=1:
                # Upload the frame to Firebase Storage
                file_name = f"fire_{self.fire_count}.jpg"
                self.upload_image(frame, file_name)
                print("Warning: Fire detected for two consecutive frames!")
            elif self.fire_count >= 2 and self.people_count<1:
                # Upload the frame to Firebase Storage
                file_name = f"fire_{self.fire_count}.jpg"
                self.upload_image(frame, file_name)
                print("Alarm: Fire detected for two consecutive frames!")
        else:
            self.fire_count = 0
        if people_detected:
            self.people_count += 1
        else:
            self.people_count = 0
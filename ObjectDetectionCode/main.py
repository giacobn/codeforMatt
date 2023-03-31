import requests

# Replace with your Firebase project ID and Storage bucket name
project_id = "usersignin-fbecc"
bucket_name = "usersignin-fbecc.appspot.com"

# Replace with your Firebase Storage access token
access_token = "3ebde5d70fa8171a9832b4d053068452b96a358"

# Replace with the path to the local image file you want to upload
local_file_path = "fire.jpeg"

# Create the URL for the Firebase Storage upload API
url = f"https://firebasestorage.googleapis.com/v0/b/{bucket_name}/o?name={local_file_path}"

# Create the request headers with the access token and content type
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "image/jpeg"
}

# Open the local image file and send a POST request to the Firebase Storage upload API
with open(local_file_path, "rb") as f:
    response = requests.post(url, headers=headers, data=f)

# Print the response from the Firebase Storage upload API
print(response.text)
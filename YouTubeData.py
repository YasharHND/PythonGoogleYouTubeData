import os

from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient import discovery
from googleapiclient.http import MediaFileUpload

load_dotenv()

SERVICE_ACCOUNT_FILE = "resources/service_account.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly", "https://www.googleapis.com/auth/youtube.upload"]
DELEGATED_USER_EMAIL = os.getenv("DELEGATED_USER_EMAIL")

CHANNEL_ID = os.getenv("CHANNEL_ID")
VIDEO_FILE_PATH = "resources/Hello World.MOV"

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
delegated_credentials = credentials.with_subject(DELEGATED_USER_EMAIL)
service = discovery.build("youtube", "v3", credentials=delegated_credentials)

request = service.channels().list(part="snippet,contentDetails,statistics", id=CHANNEL_ID)
channel_info = request.execute()

for item in channel_info.get("items", []):
    print(f"Channel Name: {item['snippet']['title']}")
    print(f"Channel ID: {item['id']}")
    print(f"Subscribers: {item['statistics']['subscriberCount']}")
    print(f"Views: {item['statistics']['viewCount']}")
    print(f"Video Count: {item['statistics']['videoCount']}")

request_body = {
    "snippet": {
        "title": "Hellow World",
        "description": "My first YouTube channel",
        "categoryId": 22,
    },
    "status": {
        "privacyStatus": "public",
    }
}

media = MediaFileUpload(VIDEO_FILE_PATH, resumable=True)
request = service.videos().insert(part="snippet,status", body=request_body, media_body=media)
response = request.execute()
print(f"Video ID: {response['id']}")

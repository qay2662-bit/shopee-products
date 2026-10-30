
import os
import requests
import sys

def publish_threads(text):
    token = os.environ["THREADS_ACCESS_TOKEN"]
    user_id = os.environ["THREADS_USER_ID"]

    url = f"https://graph.threads.net/v1.0/{user_id}/threads"
    response = requests.post(url, data={
        "media_type": "TEXT",
        "text": text,
        "access_token": token
    })
    response.raise_for_status()
    creation_id = response.json()["id"]

    publish_url = f"https://graph.threads.net/v1.0/{user_id}/threads_publish"
    result = requests.post(publish_url, data={
        "creation_id": creation_id,
        "access_token": token
    })
    result.raise_for_status()
    print("Threads 發布成功")

def publish_facebook(text):
    token = os.environ["FACEBOOK_PAGE_ACCESS_TOKEN"]
    page_id = os.environ["FACEBOOK_PAGE_ID"]

    url = f"https://graph.facebook.com/v23.0/{page_id}/feed"
    response = requests.post(url, data={
        "message": text,
        "access_token": token
    })
    response.raise_for_status()
    print("Facebook 粉絲專頁發布成功")

def main():
    text = os.environ.get("POST_TEXT", "").strip()

    if not text:
        print("錯誤：尚未設定 POST_TEXT")
        sys.exit(1)

    publish_threads(text)
    publish_facebook(text)

if __name__ == "__main__":
    main()
 

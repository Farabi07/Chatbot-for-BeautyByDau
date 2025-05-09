import requests

INSTAGRAM_ACCESS_TOKEN = "your_access_token"
PAGE_ID = "your_page_id"

# Define Webhook URL for Instagram Messages (you need to handle this in your Django app)
def send_instagram_message(message, recipient_id):
    url = f"https://graph.facebook.com/v12.0/{PAGE_ID}/messages"
    headers = {"Authorization": f"Bearer {INSTAGRAM_ACCESS_TOKEN}"}
    
    payload = {
        "messaging_type": "RESPONSE",
        "recipient": {"id": recipient_id},
        "message": {"text": message}
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

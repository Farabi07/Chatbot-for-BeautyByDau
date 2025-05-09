from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chatbot.instagram_integration import send_instagram_message
import json

# Webhook handler for Instagram messages
@csrf_exempt
def instagram_webhook(request):
    if request.method == 'GET':
        # Facebook requires verification token to confirm webhook
        hub_mode = request.GET.get('hub.mode')
        hub_challenge = request.GET.get('hub.challenge')
        hub_verify_token = request.GET.get('hub.verify_token')

        if hub_mode == 'subscribe' and hub_verify_token == 'your_verification_token':
            return JsonResponse({"hub.challenge": hub_challenge})
    
    elif request.method == 'POST':
        # Handle incoming messages from Instagram
        data = json.loads(request.body)
        # Get the sender's ID and the message text
        sender_id = data['entry'][0]['messaging'][0]['sender']['id']
        message_text = data['entry'][0]['messaging'][0]['message']['text']
        
        # Process the message (For example, reply with a greeting)
        send_instagram_message("Hello, how can I assist you?", sender_id)

        return JsonResponse({"status": "success"})

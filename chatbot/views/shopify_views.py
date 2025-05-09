from chatbot.shopify_integration import fetch_products
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def chatbot_response(request):
    user_message = request.data.get('message')
    if not user_message:
        return Response({"error": "No message provided."}, status=400)
    # Here you can implement your chatbot logic
    # For example, if the user asks for product recommendations
    if 'recommend' in user_message.lower():
        products = fetch_products()
        product_list = [{"name": product.title, "price": product.price, "description": product.body_html} for product in products]
        return Response({"response": "Here are some recommended products:", "products": product_list}, status=200)
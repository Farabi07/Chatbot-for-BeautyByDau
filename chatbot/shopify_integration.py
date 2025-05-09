from .shopify_integration import fetch_products
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import shopify

# Connect to Shopify Store (use the credentials from your private app)
def connect_shopify():
    shop_url = "https://your-store-name.myshopify.com/admin"
    api_key = "your_api_key"
    password = "your_password"
    
    shopify.ShopifyResource.set_site(shop_url)
    shopify.ShopifyResource.set_credentials(api_key, password)

# Fetch all products from Shopify
def fetch_products():
    connect_shopify()
    products = shopify.Product.find()
    return products



@api_view(['POST'])
def chatbot_response(request):
    user_message = request.data.get('message')
    
    # Example: Recommend products based on the message
    if 'recommend' in user_message.lower():
        products = fetch_products()
        product_list = [{"name": product.title, "price": product.price, "description": product.body_html} for product in products]
        return Response({"response": "Here are some recommended products:", "products": product_list}, status=200)

from .shopify_integration import fetch_products
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





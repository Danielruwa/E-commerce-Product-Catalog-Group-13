111837

E-commerce Product Catalog API   
The API allows users to manage products, categories, and reviews. Users must authenticate to access protected endpoints.


1. Models and Relationships
I designed the following models to represent the domain:

Category – Represents product `categories` (e.g., Electronics, Clothing).  
Product – Represents items available in the catalog. Each `product` belongs to a Category.  
Review– Represents user reviews for products. Linked to a Product.  
User– Uses Django's built-in `User` model to represent registered users.  
Order – Represents `orders` that include multiple products.

Relationships: 
Product has a foreign key to Category and Review has a foreign key to Product and optionally to User.  

2. Serializers
Each model has a corresponding serializer and the Validation rules ensure required fields are filled and data types are correct for example: `ProductSerializer` validates that the price is a positive number.


3. Views / ViewSets
I used DRF ViewSets for each model to simplify CRUD operations:

CategoryViewSet– Allows listing, creating, updating, and deleting categories.  
ProductViewSet– Allows CRUD operations on products.  
ReviewViewSet– Allows users to create and manage reviews.  
Permissions: Only authenticated users can create, update, or delete resources.  

4. URL Patterns
The API routes are organized as follows:
/api/categories/ - List, Create, Update, Delete categories
/api/products/ - List, Create, Update, Delete products
/api/reviews/ - List, Create, Update, Delete reviews

All routes are included in the main project `urls.py` using DRF routers.

5. Testing Evidence
I tested the API endpoints using Postman by first creating a superuser and obtaining authentication tokens, tested all endpoints (GET, POST, PUT, DELETE) for categories, products, and reviews, verified that permissions work correctly (unauthenticated users cannot modify data)
The Postman Screenshots are located in docs/screenshots.
 
Example response for creating a product:
json
{
    "id": 1,
    "name": "Smartphone",
    "category": 2,
    "price": 500.00,
    "description": "A modern smartphone with 128GB storage."
}
    • Health check endpoint successfully returned:
{"status": "ok"}
All endpoints behaved as expected.

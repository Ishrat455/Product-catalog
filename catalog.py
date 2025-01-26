import json


products = [
    {
        "id": 1,
        "name": "Matte Lipstick",
        "brand": "Joya",
        "category": "Lipstick",
        "price": 350,
        "ratings": [5, 4, 3]
    },
    {
        "id": 2,
        "name": "Liquid Foundation",
        "brand": "Parachute",
        "category": "Foundation",
        "price": 700,
        "ratings": [4, 5]
    },
    {
        "id": 3,
        "name": "Eyeliner",
        "brand": "Joya",
        "category": "Eyeliner",
        "price": 200,
        "ratings": [3, 3, 4]
    },
    {
        "id": 4,
        "name": "Lip Gloss",
        "brand": "Parachute",
        "category": "Lipstick",
        "price": 500,
        "ratings": [4, 5, 4]
    },
    {
        "id": 5,
        "name": "Face Cream",
        "brand": "Aloe Vera",
        "category": "Skin Care",
        "price": 450,
        "ratings": [5, 5, 4]
    },
    {
        "id": 6,
        "name": "Nail Polish",
        "brand": "MAYBELLINE",
        "category": "Nail Care",
        "price": 120,
        "ratings": [4, 5, 4]
    },
    {
        "id": 7,
        "name": "Bronzer",
        "brand": "L'Oréal",
        "category": "Makeup",
        "price": 650,
        "ratings": [3, 4, 4]
    },
    {
        "id": 8,
        "name": "Concealer",
        "brand": "Maybelline",
        "category": "Foundation",
        "price": 250,
        "ratings": [4, 4, 5]
    },
    {
        "id": 9,
        "name": "Blush Powder",
        "brand": "Revlon",
        "category": "Makeup",
        "price": 300,
        "ratings": [4, 5, 5]
    },
    {
        "id": 10,
        "name": "Eye Shadow Palette",
        "brand": "Urban Decay",
        "category": "Eyes",
        "price": 1200,
        "ratings": [5, 4, 4]
    },
    {
        "id": 11,
        "name": "Setting Spray",
        "brand": "MAC",
        "category": "Makeup",
        "price": 1000,
        "ratings": [5, 5, 5]
    },
    {
        "id": 12,
        "name": "Highlighter",
        "brand": "Fenty Beauty",
        "category": "Makeup",
        "price": 850,
        "ratings": [5, 5, 4]
    },
    {
        "id": 13,
        "name": "BB Cream",
        "brand": "Olay",
        "category": "Foundation",
        "price": 550,
        "ratings": [4, 4, 5]
    },
    {
        "id": 14,
        "name": "Face Scrub",
        "brand": "St. Ives",
        "category": "Skin Care",
        "price": 300,
        "ratings": [4, 3, 4]
    },
    {
        "id": 15,
        "name": "Lip Liner",
        "brand": "NYX",
        "category": "Lipstick",
        "price": 180,
        "ratings": [4, 4, 5]
    },
    {
        "id": 16,
        "name": "Mascara",
        "brand": "L'Oréal",
        "category": "Eyes",
        "price": 400,
        "ratings": [5, 4, 4]
    },
    {
        "id": 17,
        "name": "Makeup Remover",
        "brand": "Garnier",
        "category": "Skin Care",
        "price": 350,
        "ratings": [5, 4, 5]
    },
    {
        "id": 18,
        "name": "Tinted Moisturizer",
        "brand": "Clinique",
        "category": "Skin Care",
        "price": 900,
        "ratings": [4, 5, 4]
    },
    {
        "id": 19,
        "name": "Eye Cream",
        "brand": "Neutrogena",
        "category": "Skin Care",
        "price": 750,
        "ratings": [5, 5, 4]
    },
    {
        "id": 20,
        "name": "Cleansing Balm",
        "brand": "Clinique",
        "category": "Skin Care",
        "price": 1200,
        "ratings": [4, 3, 5]
    }
]


# Function to show products by category
def show_products_by_category(category=None):
    filtered_products = [product for product in products if not category or product["category"].lower() == category.lower()]
   
    print(f"\n--- Products in {category if category else 'All Categories'} ---")
    for product in filtered_products:
        avg_rating = sum(product["ratings"]) / len(product["ratings"]) if product["ratings"] else 0
        print(f"{product['name']} - {avg_rating:.2f} stars | Price: {product['price']} BDT | Category: {product['category']}")


# Main catalog page for displaying products
def catalog_page():
    while True:
        print("\n1. View All Products")
        print("2. View Products by Category")
        print("3. Exit")
       
        choice = input("Choose an option: ")
       
        if choice == '1':
            show_products_by_category()  # Display all products
        elif choice == '2':
            category = input("Enter category (e.g., Lipstick, Foundation): ")
            show_products_by_category(category)  # Display products by category
        elif choice == '3':
            break
        else:
            print("Invalid option, please try again.")






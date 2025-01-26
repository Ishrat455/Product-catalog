from catalog import products


# Display Product Details
def display_product_details(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
   
    if product:
        avg_rating = sum(product["ratings"]) / len(product["ratings"]) if product["ratings"] else 0
        print(f"\n--- Product Details ---")
        print(f"Name: {product['name']}")
        print(f"Brand: {product['brand']}")
        print(f"Category: {product['category']}")
        print(f"Price: {product['price']} BDT")
        print(f"Average Rating: {avg_rating:.2f} stars")
        print(f"Ratings: {product['ratings']}")
    else:
        print("Product not found.")


# Submit Rating
def submit_rating(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
   
    if product:
        rating = int(input("Enter your rating (1-5): "))
        if 1 <= rating <= 5:
            product["ratings"].append(rating)
            print("Thank you! Your rating has been added.")
        else:
            print("Invalid rating. Please enter a value between 1 and 5.")
    else:
        print("Product not found.")


# Display Reviews
def display_reviews(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
   
    if product:
        print(f"\n--- Reviews for {product['name']} ---")
        if product["ratings"]:
            for idx, rating in enumerate(product["ratings"], 1):
                print(f"Review {idx}: {rating} stars")
        else:
            print("No reviews yet.")
    else:
        print("Product not found.")
       
# Sort Products by Rating
def sort_products_by_rating(descending=True):
    sorted_products = sorted(products, key=lambda
    p: sum(p["ratings"]) / len(p["ratings"])
    if p["ratings"]
    else 0, reverse=descending)
    return sorted_products


# Main Program Loop
def main():
    while True:
        print("\n1. View Product Details")
        print("2. Submit Rating")
        print("3. Display Reviews")
        print("4. Sort Products by Rating")
        print("5. Exit")
       
        choice = input("Choose an option: ")
       
        if choice == '1':
            product_id = int(input("Enter the product ID to view details: "))
            display_product_details(product_id)


        elif choice == '2':
            product_id = int(input("Enter the product ID to rate: "))
            submit_rating(product_id)


        elif choice == '3':
            product_id = int(input("Enter the product ID to view reviews: "))
            display_reviews(product_id)


        elif choice == '4':
            sorted_products = sort_products_by_rating()
            for product in sorted_products:
                avg_rating = sum(product["ratings"]) / len(product["ratings"]) if product["ratings"] else 0
                print(f"{product['name']} - {avg_rating:.2f} stars")


        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()







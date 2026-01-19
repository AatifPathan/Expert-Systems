expert_system={
      "Products": {
        "Electronics": [
            {"name": "Gaming Laptop A", "type": "gaming", "price": 1500, "battery": "medium"},
            {"name": "Ultrabook B", "type": "business", "price": 1200, "battery": "long"},
            {"name": "Budget Laptop C", "type": "casual", "price": 600, "battery": "short"},
            {"name": "Workstation D", "type": "professional", "price": 2000, "battery": "medium"},
            {"name": "Gaming Laptop E", "type": "gaming", "price": 1300, "battery": "long"},
        ],
        "Books": [
            {"name": "The Hitchhiker's Guide to the Galaxy", "genre": "Sci-Fi", "price": 10, "author": "Douglas Adams"},
            {"name": "Pride and Prejudice", "genre": "Romance", "price": 8, "author": "Jane Austen"},
            {"name": "1984", "genre": "Dystopian", "price": 12, "author": "George Orwell"},
        ],
        "Clothing": [
            {"name": "T-Shirt", "category": "Apparel", "price": 20, "size": ["S", "M", "L", "XL"]},
            {"name": "Jeans", "category": "Apparel", "price": 50, "size": ["28", "30", "32", "34", "36"]},
        ]
      },
      "Services": [
            {"name": "Laptop Repair", "type": "Repair", "cost": 100},
            {"name": "Mobile Screen Replacement", "type": "Repair", "cost": 80},
            {"name": "Home Insurance - Basic", "type": "Insurance", "cost": 500},
            {"name": "Travel Insurance - International", "type": "Insurance", "cost": 150},
            {"name": "Extended Warranty - Laptop", "type": "Device Protection", "cost": 200},
            {"name": "Data Recovery Service", "type": "Repair", "cost": 300},
      ]
}
def get_user_preferences():
    print("Welcome to the Recommendation Expert System!")
    category = input("Are you looking for 'Products' or 'Services'? ").strip().capitalize()

    user_input = {"category": category}

    if category == "Products":
        print("\nWhich product category are you interested in?")
        product_category = input(f"Available categories: {', '.join(expert_system['Products'].keys())}: ").strip().capitalize()
        user_input["product_category"] = product_category

        if product_category in expert_system["Products"]:
            print("\nPlease provide your preferences for this category.")
            if product_category == "Electronics":
                type_pref = input("What type of electronics? (e.g., gaming, business, casual, professional) or press Enter to skip: ").strip().lower()
                max_price = input("Maximum price? (e.g., 1500) or press Enter to skip: ").strip()
                battery_pref = input("Battery life preference? (short/medium/long) or press Enter to skip: ").strip().lower()

                user_input["preferences"] = {
                    "type": type_pref if type_pref else None,
                    "max_price": int(max_price) if max_price.isdigit() else 999999,
                    "battery": battery_pref if battery_pref else None
                }
            elif product_category == "Books":
                genre_pref = input("Preferred genre? (e.g., Sci-Fi, Romance, Dystopian) or press Enter to skip: ").strip().capitalize()
                max_price = input("Maximum price? or press Enter to skip: ").strip()
                author_pref = input("Preferred author? or press Enter to skip: ").strip()

                user_input["preferences"] = {
                    "genre": genre_pref if genre_pref else None,
                    "max_price": int(max_price) if max_price.isdigit() else 999999,
                    "author": author_pref if author_pref else None
                }
            elif product_category == "Clothing":
                category_pref = input("What type of clothing? (e.g., Apparel) or press Enter to skip: ").strip().capitalize()
                max_price = input("Maximum price? or press Enter to skip: ").strip()
                size_pref = input("Preferred size? or press Enter to skip: ").strip().upper()

                user_input["preferences"] = {
                    "category": category_pref if category_pref else None,
                    "max_price": int(max_price) if max_price.isdigit() else 999999,
                    "size": size_pref if size_pref else None
                }
            else:
                print("Sorry, we don't have specific preference questions for that product category yet.")
                user_input["preferences"] = {}
        else:
            print("Invalid product category.")
            user_input["product_category"] = None
    elif category == "Services":
        print("\nPlease provide your preferences for services.")
        type_pref = input("What type of service are you looking for? (e.g., Repair, Insurance, Device Protection) or press Enter to skip: ").strip().capitalize()
        max_cost = input("Maximum cost? or press Enter to skip: ").strip()
        user_input["preferences"] = {
            "type": type_pref if type_pref else None,
            "max_cost": int(max_cost) if max_cost.isdigit() else 999999,
        }
    else:
        print("Invalid category. Please choose 'Products' or 'Services'.")
        user_input["category"] = None
    return user_input
def recommend_items(user_preferences, expert_system):
    recommendations = []
    category = user_preferences.get("category")

    if category == "Products":
        product_category = user_preferences.get("product_category")
        preferences = user_preferences.get("preferences", {})
        if product_category and product_category in expert_system["Products"]:
            available_items = expert_system["Products"][product_category]
            for item in available_items:
                match = True
                if preferences.get("type") and item.get("type") and preferences["type"] != item["type"]:
                    match = False
                if preferences.get("max_price") and item.get("price") and item["price"] > preferences["max_price"]:
                    match = False
                if preferences.get("brand") and item.get("brand") and preferences["brand"].lower() != item["brand"].lower():
                    match = False
                if preferences.get("battery") and item.get("battery") and preferences["battery"] != item["battery"]:
                    match = False
                if preferences.get("genre") and item.get("genre") and preferences["genre"] != item["genre"]:
                    match = False
                if preferences.get("author") and item.get("author") and preferences["author"].lower() != item["author"].lower():
                    match = False
                if preferences.get("category") and item.get("category") and preferences["category"] != item["category"]:
                    match = False
                if preferences.get("size") and item.get("size") and preferences["size"] not in item["size"]:
                    match = False

                if match:
                    recommendations.append(item)
    elif category == "Services":
        preferences = user_preferences.get("preferences", {})
        available_items = expert_system["Services"]
        for item in available_items:
            match = True
            if preferences.get("type") and item.get("type") and preferences["type"] != item["type"]:
                match = False
            if preferences.get("max_cost") and item.get("cost") and item["cost"] > preferences["max_cost"]:
                match = False
            if match:
                recommendations.append(item)
    return recommendations
user_preferences = get_user_preferences()
print("\nUser Preferences:")
print(user_preferences)
recommended_items = recommend_items(user_preferences, expert_system)
print("\nRecommended Items:")
if recommended_items:
    for item in recommended_items:
        print(f"- {item['name']}")
else:
    print("No items found matching your preferences.")

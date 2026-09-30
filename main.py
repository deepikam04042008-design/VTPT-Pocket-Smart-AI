def home_recommendations(category: str, situation: str):
    """
    Generate product recommendations based on category and situation.
    """

    products = []

    # Categorize based on situation
    if category == "home":
        if situation == "living_room":
            products = [
                {
                    "name": "Sofa",
                    "category": "Furniture",
                    "search": "living room sofa",
                    "amazon": "https://www.amazon.in/s?k=living+room+sofa",
                    "flipkart": "https://www.flipkart.com/search?q=living%20room%20sofa",
                    "ikea": "https://www.ikea.com/in/en/search/?q=sofa"
                },
                {
                    "name": "Table Lamp",
                    "category": "Lighting",
                    "search": "living room table lamp",
                    "amazon": "https://www.amazon.in/s?k=table+lamp",
                    "flipkart": "https://www.flipkart.com/search?q=table%20lamp",
                    "ikea": "https://www.ikea.com/in/en/search/?q=table%20lamp"
                }
            ]

        elif situation == "bedroom":
            products = [
                {
                    "name": "Bed",
                    "category": "Furniture",
                    "search": "bedroom bed",
                    "amazon": "https://www.amazon.in/s?k=bedroom+bed",
                    "flipkart": "https://www.flipkart.com/search?q=bedroom%20bed",
                    "ikea": "https://www.ikea.com/in/en/search/?q=bed"
                }
            ]

        elif situation == "kitchen":
            products = [
                {
                    "name": "Kitchen Storage",
                    "category": "Storage",
                    "search": "kitchen storage",
                    "amazon": "https://www.amazon.in/s?k=kitchen+storage",
                    "flipkart": "https://www.flipkart.com/search?q=kitchen%20storage",
                    "ikea": "https://www.ikea.com/in/en/search/?q=kitchen%20storage"
                }
            ]

    elif category == "party":

        if situation == "birthday":
            products = [
                {
                    "name": "Birthday Decorations",
                    "category": "Decoration",
                    "search": "birthday party decorations",
                    "amazon": "https://www.amazon.in/s?k=birthday+party+decorations",
                    "flipkart": "https://www.flipkart.com/search?q=birthday%20party%20decorations",
                    "ikea": "https://www.ikea.com/in/en/search/?q=party%20decoration"
                }
            ]

        elif situation == "wedding":
            products = [
                {
                    "name": "Wedding Decorations",
                    "category": "Decoration",
                    "search": "wedding decorations",
                    "amazon": "https://www.amazon.in/s?k=wedding+decorations",
                    "flipkart": "https://www.flipkart.com/search?q=wedding%20decorations",
                    "ikea": "https://www.ikea.com/in/en/search/?q=decoration"
                }
            ]

    elif category == "jewelry":

        products = [
            {
                "name": "Necklace",
                "category": "Jewelry",
                "search": "fashion necklace",
                "amazon": "https://www.amazon.in/s?k=fashion+necklace",
                "flipkart": "https://www.flipkart.com/search?q=fashion%20necklace"
            },
            {
                "name": "Earrings",
                "category": "Jewelry",
                "search": "fashion earrings",
                "amazon": "https://www.amazon.in/s?k=fashion+earrings",
                "flipkart": "https://www.flipkart.com/search?q=fashion%20earrings"
            }
        ]

    return products
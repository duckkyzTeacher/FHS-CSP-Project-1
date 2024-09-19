print("Welcome to the Intergalactic Snack Recommendation System!")

# Asking questions
alien_type = input("Which type of alien are you (Martian, Venusian, Jovian)? ").lower()
snack_texture = input("Do you prefer snacks that are (crunchy, gooey, fluffy)? ").lower()
snack_appearance = input("Would you like your snack to be (glowing, sparkly, ordinary)? ").lower()

# Providing recommendations based on answers
if alien_type == "martian":
    if snack_texture == "crunchy":
        if snack_appearance == "glowing":
            print("We recommend 'Galactic Crunchies'—glowing and extra crispy!")
        else:
            print("We recommend 'Martian Popcorn'—crunchy and out of this world!")
    elif snack_texture == "gooey":
        if snack_appearance == "sparkly":
            print("We recommend 'Meteorite Goo'—sparkly and irresistibly gooey!")
        else:
            print("We recommend 'Martian Slime'—gooey and slightly mysterious!")
    else:
        if snack_appearance == "ordinary":
            print("We recommend 'Martian Marshmallows'—fluffy and classic!")
        else:
            print("We recommend 'Martian Cloud Puffs'—fluffy and magically sparkly!")
elif alien_type == "venusian":
    if snack_texture == "crunchy":
        if snack_appearance == "glowing":
            print("We recommend 'Venusian Crunch Bars'—glowing and out of this world!")
        else:
            print("We recommend 'Venusian Crisps'—crunchy and light!")
    elif snack_texture == "gooey":
        if snack_appearance == "sparkly":
            print("We recommend 'Venusian Goo Balls'—sparkly and delightfully gooey!")
        else:
            print("We recommend 'Venusian Slime Nuggets'—gooey and cosmic!")
    else:
        if snack_appearance == "ordinary":
            print("We recommend 'Venusian Fluffies'—fluffy and heavenly!")
        else:
            print("We recommend 'Venusian Cloud Puffs'—fluffy and sparkly!")
elif alien_type == "jovian":
    if snack_texture == "crunchy":
        if snack_appearance == "glowing":
            print("We recommend 'Jovian Crunchies'—glowing and ultra-crispy!")
        else:
            print("We recommend 'Jovian Crunch Munch'—crunchy and full of flavor!")
    elif snack_texture == "gooey":
        if snack_appearance == "sparkly":
            print("We recommend 'Jovian Goo Drops'—sparkly and delightfully gooey!")
        else:
            print("We recommend 'Jovian Gooey Slugs'—gooey and unique!")
    else:
        if snack_appearance == "ordinary":
            print("We recommend 'Jovian Fluff Nuggets'—fluffy and surprisingly satisfying!")
        else:
            print("We recommend 'Jovian Star Fluffs'—fluffy and magically sparkly!")
else:
    print("Oops! We don't have snacks for that alien type. How about a cosmic cookie instead?")

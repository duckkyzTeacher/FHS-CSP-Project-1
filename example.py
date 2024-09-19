print("Welcome to the Movie Recommendation System!")
# Asking questions
genre = input("What genre do you prefer (action, comedy, drama)? ").lower()
mood = input("Are you in the mood for something (exciting, relaxing)? ").lower()
length = input("Do you prefer a movie that's (short, long)? ").lower()

# Providing recommendations based on answers
if genre == "action":
    if mood == "exciting":
        if length == "short":
            print("We recommend 'Mad Max: Fury Road'!")
        else:
            print("We recommend 'The Dark Knight'!")
    else:
        if length == "short":
            print("We recommend 'Die Hard'!")
        else:
            print("We recommend 'Gladiator'!")
elif genre == "comedy":
    if mood == "exciting":
        if length == "short":
            print("We recommend 'Superbad'!")
        else:
            print("We recommend 'Step Brothers'!")
    else:
        if length == "short":
            print("We recommend 'Groundhog Day'!")
        else:
            print("We recommend 'The Big Lebowski'!")
elif genre == "drama":
    if mood == "exciting":
        if length == "short":
            print("We recommend 'The Social Network'!")
        else:
            print("We recommend 'The Shawshank Redemption'!")
    else:
        if length == "short":
            print("We recommend 'Her'!")
        else:
            print("We recommend 'Forrest Gump'!")
else:
    print("Sorry, we don't have recommendations for that genre.")

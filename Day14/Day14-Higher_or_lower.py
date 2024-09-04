import random

# Fictional numbers
instagram_followers = {
    "Nicky Minaj" : ["singer", "USA", 10000],
    "David Beckham" : ["ex-footbaler", "UK", 2400],
    "Steffi Graf" : ["ex-tennis player", "Germany" , 1200],
    "Iga Swiatek" : ["Tennis player", "Poland", 15000],
    "Kim Kardashian" : ["celebrity", "America" , 12000],
    "Chris Rock" : ["comedian", "US" , 12500],
}

# TODO pick random person
def pick_random_person(dictionary):
    random_person, list_of_attributes = random.choice(list(dictionary.items()))
    return random_person, list_of_attributes

user_score = 0
continue_game = True
#
while continue_game:
    person_A = pick_random_person(instagram_followers)
    person_B = pick_random_person(instagram_followers)
    if person_A != person_B:
        person_A_followers = person_A[1][2]
        person_B_followers = person_B[1][2]
        print(f"Compare A: {person_A[0]}, a {person_A[1][0]} , from {person_A[1][1]}")
        print(f"Compare B: {person_B[0]}, a {person_B[1][0]} , from {person_B[1][1]}")
        chosen_person = input("Who has more followers? Type 'A' or 'B': ").lower()
        if person_A_followers > person_B_followers:
            if chosen_person == "a":
                user_score += 1
                print(f"You're right, your current score is {user_score}" )
            else:
                print(f"Not right - Your final score is {user_score}")
                user_score = 0
                continue_game = False
        elif person_B_followers > person_A_followers:
            if chosen_person == "b":
                user_score += 1
                print(f"You're right, your current score is {user_score}")
            else:
                print(f"Not right - Your final score is {user_score}")
                user_score = 0
                continue_game = False
        # else:
        #     print(f"A and B are the same person lol, start over - Your final score is {user_score}")
        #     continue_game = False


#Fake news Headline generator

import random
import datetime

# Subjects
subjects = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi"
]

# Actions
actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on"
]

# Objects
places_or_things = [
    "a flying rickshaw",
    "a banana-powered scooter",
    "the Parliament building",
    "a cricket stadium",
    "a Bollywood movie set",
    "Mars colony plans"
]

# Emojis
emojis = ["😂", "🚨", "🛺", "🍌", "🎬", "🐒", "🗳️", "🏏", "🚀", "🇮🇳", "🔥", "😹", "💥"]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    emoji = random.choice(emojis)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    headline = f"{emoji} BREAKING at {timestamp}: {subject} {action} {place_or_thing}! {emoji}"
    
    # Truncate if too long
    if len(headline) > 280:
        headline = headline[:277] + "..."

    print("\n" + headline)

    user_input = input("\nWant another hilarious headline? (yes/no): ").strip().lower()
    if user_input == "no":
        break

print("\nThanks for using the  Fake News Headline Generator. Have a good day!")

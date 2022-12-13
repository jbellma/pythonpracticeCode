# Storing results from a poll in a dictionary

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# Looping through all key-value pairs in a dictionary

for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}.")

# Looping through all the keys in a dictionary

for name in favorite_languages.keys():
    print(name.title())

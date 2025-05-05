"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Kateřina Pokorná
email: k.mackova@email.cz
"""
import sys

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

sep_line = ("-" * 40)

user = input("username:")
pwd = input("password:")
print(sep_line)

allow_user = user in registered_users and registered_users[user] == pwd

if not allow_user:
    print("unregistered user, terminating the program..")
    sys.exit("unregistered user, terminating the program..")

print("Welcome to the app,", user)
print(f"We have {len(TEXTS)} texts to be analyzed.")
print(sep_line)


selected_text_no = input("Enter a number btw. 1 and 3 to select: ")

print(sep_line)

selection_ok = selected_text_no in ("1", "2", "3")

if not selection_ok:
    print("Number btw. 1 and 3 should have been selected, terminating the program..")
    sys.exit("Number btw. 1 and 3 should have been selected, terminating the program..")

selected_text = TEXTS[int(selected_text_no) - 1]

text_to_words = selected_text.split()

num_strings = 0
title_words = 0
upper_words = 0
lower_words = 0
sum_numbers = 0
words_count = len(text_to_words)

words_len = {}

for word in text_to_words:
    word_2 = word.strip(",.!?)('")
    if word_2.isnumeric():
        num_strings += 1
        sum_numbers += int(word_2)
    elif word_2.lower() == word_2:
        lower_words += 1
    elif word_2.title() == word_2:
        title_words += 1
    elif word_2.upper() == word_2:
        upper_words += 1

    word_len = len(word_2)
    words_len[word_len] = words_len.setdefault(word_len, 0) + 1

print(f"There are {words_count} words in the selected text.")
print(f"There are {title_words} titlecase words.")
print(f"There are {upper_words} uppercase words.")
print(f"There are {lower_words} lowercase words.")
print(f"There are {num_strings} numeric strings.")
print(f"The sum of all the numbers {sum_numbers}")
print(sep_line)

max_len = max(words_len.values())
occurences_len = max(len("  OCCURENCES  "), max_len + 2)
print(f"LEN|{"OCCURENCES".center(occurences_len)}|NR.")
for delka in range(1, max(words_len) + 1):
    print(f"{str(delka).rjust(3)}|{("*" * words_len.setdefault(delka, 0)).ljust(occurences_len)}|{words_len.setdefault(delka, 0)}")

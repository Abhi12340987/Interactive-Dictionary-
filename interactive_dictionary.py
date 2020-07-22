import json
from difflib import get_close_matches

data = json.load(open("My Python Applications/app_1_interactive/data.json"))

def define(w):
    w = w.lower()
    if w in data:
        return data[w]

    elif w.title() in data:
        return data[w.title()]

    elif w.upper() in data:
        return data[w.upper()]

    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word does not exist. Please double check it"

user_input = input("Enter a word: ")

output = define(user_input)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
  

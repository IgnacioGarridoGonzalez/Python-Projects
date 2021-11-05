text = input("Input your text: ").lower()
# N.B. how the input is automatically rendered to lowercase to prevent errors
# from arising once it goes through the Dictionary

# A function for separating every single character is defined:
def split(text):
    return [char for char in text]

# The split text is saved as a LIST in a variable:
split_text = split(text)

# We create a dictionary:

DICT = {
    "a": "·-",
    "b": "-···",
    "c": "-·-·",
    "d": "-··",
    "e": "·",
    "f": "··-·",
    "g": "--·",
    "h": "····",
    "I": "··",
    "j": "·---",
    "k": "-.-",
    "l": "·-··",
    "m": "—",
    "n": "-·",
    "o": "---",
    "p": "·--·",
    "q": "--·-",
    "r": "·-·",
    "s": "···",
    "t": "-",
    "u": "··-",
    "v": "···-",
    "w": "·--",
    "x": "-··-",
    "y": "-·--",
    "z": "--··",

    "1": "·----",
    "2": "··---",
    "3": "···--",
    "4": "····-",
    "5": "·····",
    "6": "-····",
    "7": "--···",
    "8": "---··",
    "9": "----·",
    "0": "-----",
    " ": "/",
    "ñ": "--·--",
    "?": "··--··",
    ",": "--··--",
    "!": "-·-·--"
}

# We can print the Dictionary if we please:
# print("This is the Morse dictionary: ", DICT)

Translation = [DICT[letter] for letter in split_text]

# The Translation is a list. We must first join the elements of the list before producing the translation.
# Then, we print the translation:

print("The translation is: ", " ".join(Translation))
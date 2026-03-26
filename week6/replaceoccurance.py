print("Replace alphabets (without case restrictions):")
try:
    word = input("Enter the word: ")
    target = input("Enter the target alphabet: ")
    alphabet = input("Enter the alphabet to replace the target alphabet: ")
    if len(word) == 0:
        raise ValueError("Empty word")
    if len(target) != 1 or len(alphabet) != 1:
        raise ValueError("Target and replacement must be single characters")
    new_word = ""
    for ch in word:
        if ch.lower() == target.lower():
            new_word += alphabet
        else:
            new_word += ch
    print("The word after replacement is:", new_word)
except ValueError as e:
    print("Input Error:", e)
except Exception as e:
    print("Unexpected Error:", e)
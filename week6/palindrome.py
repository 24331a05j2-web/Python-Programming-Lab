print("String Palindrome Checker(no case restrictions):")
word=input("Enter a word:").strip()
reversed_word=word[::-1]
if(word.lower()==reversed_word.lower()):
    print("The given word is palindrome")
else:
    print("The given word isnt a palindrome")
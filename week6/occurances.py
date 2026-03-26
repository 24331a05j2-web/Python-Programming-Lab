print("Alphabet Occurrence Counter (without case restrictions):")
word = input("Enter a word: ").strip()
alphabet = input("Enter a single alphabet: ").strip()
if len(alphabet) != 1:
    print("Please enter exactly ONE alphabet.")
elif len(word) == 0:
    print("Word cannot be empty.")
else:
    count = 0
    for ch in word:
        if ch.lower() == alphabet.lower():
            count += 1
    print("The number of occurrences of the alphabet in the word is:", count)
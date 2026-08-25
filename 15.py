text = input("Enter a string: ")
counts = {}

for char in text:
    if char.isalpha():
        char = char.lower()
        counts[char] = counts.get(char, 0) + 1

for letter, count in counts.items():
    print(f"{letter}: {count}")   

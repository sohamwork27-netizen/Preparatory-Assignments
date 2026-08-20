names = ["Aarav", "Riya", "Soham", "Aarav", "Neha", "Riya", "Aditya"]

seen = set()

for name in names:
    if name in seen:
        print(name)
    else:
        seen.add(name)

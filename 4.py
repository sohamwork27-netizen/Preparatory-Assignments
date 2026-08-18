marks = []

for i in range(5):
    mark = int(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

total = sum(marks)

if total >= 90:
    grade = "Ex"
elif total >= 80:
    grade = "A"
elif total >= 70:
    grade = "B"
elif total >= 60:
    grade = "C"
else:
    grade = "F"

print("Total Marks:", total)
print("Grade:", grade)

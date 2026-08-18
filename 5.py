
string = input("Enter a string: ")
upper_count=0
lower_count=0
digit_count=0
other_count=0
for character in string:
    if character.islower():
        lower_count+=1
    elif( character.isupper()):
        upper_count+=1
    elif (character.isdigit()):
        digit_count+=1
    else:
        other_count+=1
print(f"upper count is ",upper_count)
print(f"lower count is ",lower_count)
print(f"digit count is ",digit_count)
print(f"other count is ",other_count)

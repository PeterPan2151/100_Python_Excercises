# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
text_input = input("Enter text: ").lower()
if text_input == "yes":
    print("Yes")
else:
    print("No")
    